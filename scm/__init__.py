
import os
import json
import logging
import time
import threading
from typing import Optional, Dict, Any
from pathlib import Path
from datetime import datetime, timedelta
from oauthlib.oauth2 import BackendApplicationClient
from requests_oauthlib import OAuth2Session
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

# Import all sub-clients
from scm.config_operations import api as config_operations_api
from scm.config_operations.api_client import ApiClient as ConfigOperationsApiClient
from scm.config_operations.configuration import Configuration as ConfigOperationsConfiguration
from scm.config_setup import api as config_setup_api
from scm.config_setup.api_client import ApiClient as ConfigSetupApiClient
from scm.config_setup.configuration import Configuration as ConfigSetupConfiguration
from scm.deployment_services import api as deployment_services_api
from scm.deployment_services.api_client import ApiClient as DeploymentServicesApiClient
from scm.deployment_services.configuration import Configuration as DeploymentServicesConfiguration
from scm.device_settings import api as device_settings_api
from scm.device_settings.api_client import ApiClient as DeviceSettingsApiClient
from scm.device_settings.configuration import Configuration as DeviceSettingsConfiguration
from scm.identity_services import api as identity_services_api
from scm.identity_services.api_client import ApiClient as IdentityServicesApiClient
from scm.identity_services.configuration import Configuration as IdentityServicesConfiguration
from scm.network_services import api as network_services_api
from scm.network_services.api_client import ApiClient as NetworkServicesApiClient
from scm.network_services.configuration import Configuration as NetworkServicesConfiguration
from scm.objects import api as objects_api
from scm.objects.api_client import ApiClient as ObjectsApiClient
from scm.objects.configuration import Configuration as ObjectsConfiguration
from scm.security_services import api as security_services_api
from scm.security_services.api_client import ApiClient as SecurityServicesApiClient
from scm.security_services.configuration import Configuration as SecurityServicesConfiguration

# Set up logging
logging.basicConfig(level=logging.ERROR)
logger = logging.getLogger("scm")


def _create_auto_refresh_wrapper(scm_client, original_request_method):
    """
    Create a wrapper around the RESTClientObject.request() method that automatically
    refreshes the token before each API call and retries on 401 errors.

    This matches scm-go's behavior where the Do() method:
    - Checks token expiry before every API request (line 490-497)
    - Retries once on 401 errors (line 585-598)
    - Prevents back-to-back 401 retries (line 586-591)

    Args:
        scm_client: Reference to the parent Scm instance
        original_request_method: The original request() method to wrap

    Returns:
        Wrapped request method with automatic token refresh and 401 retry
    """
    # Track last error to prevent back-to-back 401 retries (like scm-go)
    last_error = {'status': None}

    def request_with_auto_refresh(method, url, headers=None, *args, **kwargs):
        """
        Wrapped request method that auto-refreshes token before each request
        and retries once on 401 errors.
        """
        # Check if token needs refresh (like scm-go's Do() method line 490-497)
        if scm_client.token_expires_soon:
            logger.debug("Token expires soon, automatically refreshing before request")
            scm_client.refresh_token()

        # Update Authorization header with current token
        if headers is None:
            headers = {}
        if scm_client._access_token:
            headers['Authorization'] = f'Bearer {scm_client._access_token}'

        # Call the original request method
        try:
            response = original_request_method(method, url, headers=headers, *args, **kwargs)
            # Clear last error on success
            last_error['status'] = None
            return response
        except Exception as e:
            # Check if this is a 401 Unauthorized error
            # OpenAPI rest client raises exceptions with status attribute
            if hasattr(e, 'status') and e.status == 401:
                # Check for back-to-back 401s (like scm-go line 586-591)
                if last_error['status'] == 401:
                    logger.warning("Getting 401s back-to-back, not retrying to prevent infinite loop")
                    raise

                # First 401, so refresh the token and retry (like scm-go line 594-598)
                logger.info(f"Got 401 Unauthorized, refreshing token and retrying request to {url}")
                last_error['status'] = 401

                try:
                    scm_client.refresh_token()
                except Exception as refresh_err:
                    logger.error(f"Failed to refresh token after 401: {refresh_err}")
                    raise e  # Re-raise original 401 error

                # Update headers with new token
                if scm_client._access_token:
                    headers['Authorization'] = f'Bearer {scm_client._access_token}'

                # Retry the request once
                try:
                    response = original_request_method(method, url, headers=headers, *args, **kwargs)
                    last_error['status'] = None  # Clear on success
                    return response
                except Exception as retry_error:
                    # Track the retry error status
                    if hasattr(retry_error, 'status'):
                        last_error['status'] = retry_error.status
                    raise
            else:
                # Not a 401, just re-raise
                raise

    return request_with_auto_refresh


class Scm:
    """
    Unified SCM Client that provides access to all services.

    Configuration Priority:
    1. Constructor arguments
    2. Environment variables
    3. JSON configuration file (config/scm-config.json or SCM_CONFIG_FILE)

    JWT Token Handling (matching scm-go behavior):
    - Can pass pre-existing JWT token to avoid auth API rate limits
    - Priority: Constructor args > Config file > Fetch new token
    - Example: Scm(jwt='...', jwt_expires_at='2026-01-01T12:00:00Z', jwt_lifetime=900)

    Environment Variables (consistent with scm-go):
    - SCM_CLIENT_ID: Client ID for authentication
    - SCM_CLIENT_SECRET: Client secret for authentication
    - SCM_SCOPE: Scope in format "tsg_id:XXXXX" (preferred over SCM_TSG_ID)
    - SCM_TSG_ID: TSG ID (backward compatibility, internally converted to scope)
    - SCM_HOST: API host (default: api.sase.paloaltonetworks.com)
    - SCM_AUTH_URL: Auth URL (default: https://auth.apps.paloaltonetworks.com)
    - SCM_LOGGING: Log level - quiet, basic, or detailed (preferred over SCM_LOG_LEVEL)
    - SCM_LOG_LEVEL: Log level - ERROR, WARNING, INFO, DEBUG (backward compatibility)

    Args:
        client_id: Client ID for OAuth2 authentication
        client_secret: Client secret for OAuth2 authentication
        tsg_id: Tenant Service Group ID
        host: API host (default: api.sase.paloaltonetworks.com)
        auth_url: Auth URL (default: https://auth.apps.paloaltonetworks.com)
        verify_ssl: Whether to verify SSL certificates (default: True)
        log_level: Logging level (ERROR, WARNING, INFO, DEBUG)
        jwt: Pre-existing JWT token (optional, for token caching)
        jwt_expires_at: JWT expiration time as ISO format string or datetime object
        jwt_lifetime: JWT lifetime in seconds (optional)
    """

    # Token expiration buffer - refresh 60 seconds before actual expiry
    TOKEN_EXPIRY_BUFFER = 60

    def __init__(
        self,
        client_id: Optional[str] = None,
        client_secret: Optional[str] = None,
        tsg_id: Optional[str] = None,
        host: Optional[str] = None,
        auth_url: Optional[str] = None,
        verify_ssl: bool = True,
        log_level: Optional[str] = None,
        jwt: Optional[str] = None,
        jwt_expires_at: Optional[str] = None,
        jwt_lifetime: Optional[int] = None
    ):
        # 1. Load File Configuration
        file_config = self._load_config_from_file()

        # 2. Resolve Configuration (Args > Env > File > Default)
        self.client_id = (
            client_id
            or os.environ.get("SCM_CLIENT_ID")
            or file_config.get("client_id")
        )
        self.client_secret = (
            client_secret
            or os.environ.get("SCM_CLIENT_SECRET")
            or file_config.get("client_secret")
        )

        # Support both SCM_SCOPE (preferred, consistent with Go) and SCM_TSG_ID (backward compat)
        scope_env = os.environ.get("SCM_SCOPE", "")
        tsg_id_env = os.environ.get("SCM_TSG_ID", "")

        # Extract TSG ID from scope format or use direct TSG ID
        if tsg_id:
            self.tsg_id = tsg_id
        elif scope_env:
            # Extract from "tsg_id:XXXXX" format
            self.tsg_id = scope_env.replace("tsg_id:", "")
        elif tsg_id_env:
            self.tsg_id = tsg_id_env
        elif file_config.get("scope"):
            # Extract from config file scope field
            self.tsg_id = file_config.get("scope", "").replace("tsg_id:", "")
        elif file_config.get("tsg_id"):
            self.tsg_id = file_config.get("tsg_id")
        else:
            self.tsg_id = None

        self.host = (
            host
            or os.environ.get("SCM_HOST")
            or file_config.get("host")
            or "api.sase.paloaltonetworks.com"
        )
        self.auth_url = (
            auth_url
            or os.environ.get("SCM_AUTH_URL")
            or file_config.get("auth_url")
            or "https://auth.apps.paloaltonetworks.com"
        )

        # Support both SCM_LOGGING (preferred) and SCM_LOG_LEVEL (backward compat)
        _log_level_str = (
            log_level
            or os.environ.get("SCM_LOGGING")
            or os.environ.get("SCM_LOG_LEVEL")
            or file_config.get("logging")
            or "ERROR"
        ).upper()

        self.verify_ssl = verify_ssl

        # Configure logger
        try:
            logger.setLevel(_log_level_str)
        except ValueError:
            logger.setLevel(logging.ERROR)
            logger.warning(f"Invalid log level '{_log_level_str}', defaulting to ERROR")

        if not self.client_id or not self.client_secret:
            raise ValueError(
                "client_id and client_secret must be provided via args, environment variables, or config file."
            )

        # Remove /oauth2/access_token from auth_url if present
        if "/oauth2/access_token" in self.auth_url:
            self.auth_url = self.auth_url.split("/oauth2/access_token")[0]

        # JWT token handling with priority (like scm-go client.go:238-246)
        # Priority: 1. Constructor args, 2. Config file, 3. Fetch new token

        # Load from config file first (for fallback)
        # Support both "jwt" (preferred) and "access_token" (backward compat)
        file_jwt = file_config.get("jwt") or file_config.get("access_token")
        file_jwt_expires_at_str = file_config.get("jwt_expires_at") or file_config.get("token_expires_at")
        file_jwt_lifetime = file_config.get("jwt_lifetime")

        # Store token metadata
        self._access_token: Optional[str] = None
        self._token_expires_at: Optional[datetime] = None
        self._jwt_lifetime: Optional[int] = None

        # Thread lock for atomic token refresh (like scm-go's atomic counter)
        self._refresh_lock = threading.Lock()

        # Determine if we need to fetch a new token
        needs_new_token = True
        token_source = None

        # Priority 1: JWT passed directly as constructor argument (like scm-go)
        if jwt and jwt_expires_at:
            try:
                # Parse expiration time if string, otherwise use datetime object
                if isinstance(jwt_expires_at, str):
                    expires_at = datetime.fromisoformat(jwt_expires_at.replace('Z', '+00:00'))
                else:
                    expires_at = jwt_expires_at

                # Check if token is still valid with expiration buffer (like scm-go)
                buffer_time = timedelta(seconds=self.TOKEN_EXPIRY_BUFFER)
                if datetime.now(expires_at.tzinfo) < (expires_at - buffer_time):
                    self._access_token = jwt
                    self._token_expires_at = expires_at
                    self._jwt_lifetime = jwt_lifetime
                    needs_new_token = False
                    token_source = "constructor argument"
                    logger.info(f"Using JWT from constructor argument (expires at {expires_at.isoformat()})")
                else:
                    logger.info("JWT from constructor argument has expired or expiring soon, will fetch new token")
            except (ValueError, TypeError) as e:
                logger.warning(f"Failed to parse JWT from constructor argument: {e}, will fetch new token")

        # Priority 2: JWT from config file (if not provided as constructor arg)
        if needs_new_token and file_jwt and file_jwt_expires_at_str:
            try:
                # Parse expiration time (handle both with and without 'Z' suffix)
                expires_at = datetime.fromisoformat(file_jwt_expires_at_str.replace('Z', '+00:00'))

                # Check if token is still valid with expiration buffer (like scm-go)
                buffer_time = timedelta(seconds=self.TOKEN_EXPIRY_BUFFER)
                if datetime.now(expires_at.tzinfo) < (expires_at - buffer_time):
                    self._access_token = file_jwt
                    self._token_expires_at = expires_at
                    self._jwt_lifetime = file_jwt_lifetime
                    needs_new_token = False
                    token_source = "config file"
                    logger.info(f"Using cached JWT from config file (expires at {expires_at.isoformat()})")
                else:
                    logger.info("Cached token from config file has expired or expiring soon, fetching new token")
            except (ValueError, TypeError) as e:
                logger.warning(f"Failed to parse token expiration time from config file: {e}, fetching new token")

        # Priority 3: Fetch new token if none provided or all expired
        if needs_new_token:
            self._fetch_and_store_token()
            token_source = "auth API"

        # Initialize sub-clients
        self.config_operations = self._init_config_operations_client()
        self.config_setup = self._init_config_setup_client()
        self.deployment_services = self._init_deployment_services_client()
        self.device_settings = self._init_device_settings_client()
        self.identity_services = self._init_identity_services_client()
        self.network_services = self._init_network_services_client()
        self.objects = self._init_objects_client()
        self.security_services = self._init_security_services_client()

    def _load_config_from_file(self) -> Dict[str, Any]:
        """
        Loads configuration from a JSON file.

        Search order:
        1. SCM_CONFIG_FILE environment variable
        2. config/scm-config.json (project-local, matches scm-go layout)
        """
        # Explicit env var takes priority
        env_path = os.environ.get("SCM_CONFIG_FILE")
        if env_path:
            path = Path(env_path)
            if path.exists():
                try:
                    with open(path, "r") as f:
                        return json.load(f)
                except Exception as e:
                    logger.warning(f"Failed to load config file at {env_path}: {e}")
                    return {}
            return {}

        # Check project-local config/scm-config.json (matches scm-go)
        local_path = Path("config/scm-config.json")
        if local_path.exists():
            try:
                with open(local_path, "r") as f:
                    return json.load(f)
            except Exception as e:
                logger.warning(f"Failed to load config file at {local_path}: {e}")

        return {}

    def _fetch_and_store_token(self) -> None:
        """
        Fetches a new OAuth2 access token and stores metadata.
        """
        token_url = f"{self.auth_url}/oauth2/access_token"

        # SCM requires tsg_id in the scope
        scope = [f"tsg_id:{self.tsg_id}"] if self.tsg_id else None

        logger.debug(f"Attempting Authentication to: {token_url}")
        logger.debug(f"Client ID: {self.client_id[:4]}...{self.client_id[-4:] if len(self.client_id) > 4 else ''}")
        logger.debug(f"Scope: {scope}")

        # FIX: Tell oauthlib to relax scope validation.
        os.environ["OAUTHLIB_RELAX_TOKEN_SCOPE"] = "1"

        # 1. Create the standard OAuth2 Client
        client = BackendApplicationClient(client_id=self.client_id, scope=scope)

        # 2. Create the session with retry logic
        oauth = OAuth2Session(client=client)

        # Configure retry strategy with exponential backoff (matching scm-go)
        # scm-go uses: 5 retries, exponential backoff (1s, 2s, 4s, 8s, 10s capped)
        # See client.go lines 321-324
        retry_strategy = Retry(
            total=5,                    # Match scm-go's 5 retries (vs previous 3)
            backoff_factor=1,           # Exponential: 1s, 2s, 4s, 8s, 16s... (vs previous linear 0.3)
            backoff_max=10,             # Cap at 10 seconds (like scm-go's WithCappedDuration)
            status_forcelist=[408, 429, 500, 502, 503, 504],
            allowed_methods=["POST"],
        )
        adapter = HTTPAdapter(max_retries=retry_strategy)
        oauth.mount("https://", adapter)
        oauth.mount("http://", adapter)

        # 3. Fetch the token with timeout
        try:
            token_response = oauth.fetch_token(
                token_url=token_url,
                client_id=self.client_id,
                client_secret=self.client_secret,
                verify=self.verify_ssl,
                timeout=30
            )

            self._access_token = token_response["access_token"]

            # Store token lifetime if available
            if "expires_in" in token_response:
                self._jwt_lifetime = int(token_response["expires_in"])
                # Calculate expiration time with buffer (like scm-go: 60 second buffer)
                self._token_expires_at = datetime.now(datetime.now().astimezone().tzinfo) + timedelta(
                    seconds=self._jwt_lifetime - self.TOKEN_EXPIRY_BUFFER
                )
                logger.debug(f"Token expires in {self._jwt_lifetime}s, will refresh at {self._token_expires_at.isoformat()}")

            logger.info("Authentication successful.")

        except Exception as e:
            logger.error(f"Authentication Failed: {str(e)}")
            raise ValueError(f"Failed to authenticate with SCM via OAuth2: {str(e)}")

    def refresh_token(self) -> str:
        """
        Refresh the OAuth2 access token.

        This method is thread-safe using a lock to prevent concurrent refresh attempts.
        If multiple threads/requests call this simultaneously, only one will refresh
        and the others will wait then return the newly refreshed token.

        Before calling the auth API, checks if a valid token exists in config.json
        (e.g., from automatic refresh via cron job) to avoid unnecessary API calls.

        Returns:
            str: The new access token

        Raises:
            ValueError: If token refresh fails
        """
        # Atomic refresh using lock (like scm-go's atomic counter pattern)
        with self._refresh_lock:
            # Double-check: another thread might have just refreshed
            # (avoids unnecessary refresh if token was just updated)
            if not self.token_expires_soon:
                logger.debug("Token already refreshed by another thread, skipping refresh")
                return self._access_token

            # OPTIMIZATION: Before calling auth API, check if config file has a newer valid token
            # This avoids unnecessary auth API calls when cron jobs or other processes
            # have already refreshed the token in config.json
            config_path = os.environ.get("SCM_CONFIG_FILE", os.path.expanduser("~/.scm/config.json"))
            if Path(config_path).exists():
                try:
                    config = self._load_config_from_file()
                    if config.get("jwt") and config.get("jwt_expires_at"):
                        # Check if this is a different token than what we have
                        if config.get("jwt") != self._access_token:
                            # Parse expiration time
                            cached_expires_at = datetime.fromisoformat(
                                config["jwt_expires_at"].replace('Z', '+00:00')
                            )
                            now = datetime.now(cached_expires_at.tzinfo)
                            time_until_expiry = (cached_expires_at - now).total_seconds()

                            # If cached token is still valid (not expiring within buffer), use it
                            if time_until_expiry > self.TOKEN_EXPIRY_BUFFER:
                                logger.info(
                                    f"Found valid cached token in config file (expires in {int(time_until_expiry)}s), "
                                    f"using it instead of fetching new token"
                                )
                                self._access_token = config["jwt"]
                                self._token_expires_at = cached_expires_at
                                self._jwt_lifetime = config.get("jwt_lifetime", 900)

                                # Update all sub-clients with the cached token
                                self._update_all_sub_clients()

                                return self._access_token
                            else:
                                logger.debug(
                                    f"Cached token in config file expires soon ({int(time_until_expiry)}s), "
                                    f"will fetch new token"
                                )
                except Exception as e:
                    logger.debug(f"Could not load token from config file: {e}, will fetch new token")

            logger.info("Refreshing access token...")
            self._fetch_and_store_token()

            # Update all sub-clients with the new token
            self._update_all_sub_clients()

            return self._access_token

    def _update_all_sub_clients(self) -> None:
        """
        Update all sub-client configurations with the current access token.

        This is called after token refresh to ensure all API clients use the new token.
        """
        if hasattr(self, 'config_operations') and hasattr(self.config_operations, 'api_client'):
            self.config_operations.api_client.configuration.access_token = self._access_token
        if hasattr(self, 'config_setup') and hasattr(self.config_setup, 'api_client'):
            self.config_setup.api_client.configuration.access_token = self._access_token
        if hasattr(self, 'deployment_services') and hasattr(self.deployment_services, 'api_client'):
            self.deployment_services.api_client.configuration.access_token = self._access_token
        if hasattr(self, 'device_settings') and hasattr(self.device_settings, 'api_client'):
            self.device_settings.api_client.configuration.access_token = self._access_token
        if hasattr(self, 'identity_services') and hasattr(self.identity_services, 'api_client'):
            self.identity_services.api_client.configuration.access_token = self._access_token
        if hasattr(self, 'network_services') and hasattr(self.network_services, 'api_client'):
            self.network_services.api_client.configuration.access_token = self._access_token
        if hasattr(self, 'objects') and hasattr(self.objects, 'api_client'):
            self.objects.api_client.configuration.access_token = self._access_token
        if hasattr(self, 'security_services') and hasattr(self.security_services, 'api_client'):
            self.security_services.api_client.configuration.access_token = self._access_token

    @property
    def token_expires_soon(self) -> bool:
        """
        Check if the token will expire soon.

        Returns:
            bool: True if token is missing or expiring within TOKEN_EXPIRY_BUFFER seconds
        """
        if not self._access_token or not self._token_expires_at:
            return True

        # Check if current time is within TOKEN_EXPIRY_BUFFER seconds of expiry
        buffer_time = timedelta(seconds=self.TOKEN_EXPIRY_BUFFER)
        return datetime.now(self._token_expires_at.tzinfo) >= (self._token_expires_at - buffer_time)

    @property
    def access_token(self) -> Optional[str]:
        """Get the current access token."""
        return self._access_token
    def _init_config_operations_client(self):
        # Construct base URL by appending the service-specific path suffix
        # Host: https://api.sase.paloaltonetworks.com
        # Suffix: /config/operations/v1
        config = ConfigOperationsConfiguration(
            host=f"https://{self.host}/config/operations/v1"
        )
        config.verify_ssl = self.verify_ssl
        config.access_token = self._access_token

        client = ConfigOperationsApiClient(config)

        # Wrap the rest client's request method to auto-refresh tokens
        client.rest_client.request = _create_auto_refresh_wrapper(
            self, client.rest_client.request
        )

        config_operations_api.api_client = client
        return config_operations_api
    def _init_config_setup_client(self):
        # Construct base URL by appending the service-specific path suffix
        # Host: https://api.sase.paloaltonetworks.com
        # Suffix: /config/setup/v1
        config = ConfigSetupConfiguration(
            host=f"https://{self.host}/config/setup/v1"
        )
        config.verify_ssl = self.verify_ssl
        config.access_token = self._access_token

        client = ConfigSetupApiClient(config)

        # Wrap the rest client's request method to auto-refresh tokens
        client.rest_client.request = _create_auto_refresh_wrapper(
            self, client.rest_client.request
        )

        config_setup_api.api_client = client
        return config_setup_api
    def _init_deployment_services_client(self):
        # Construct base URL by appending the service-specific path suffix
        # Host: https://api.sase.paloaltonetworks.com
        # Suffix: /config/deployment/v1
        config = DeploymentServicesConfiguration(
            host=f"https://{self.host}/config/deployment/v1"
        )
        config.verify_ssl = self.verify_ssl
        config.access_token = self._access_token

        client = DeploymentServicesApiClient(config)

        # Wrap the rest client's request method to auto-refresh tokens
        client.rest_client.request = _create_auto_refresh_wrapper(
            self, client.rest_client.request
        )

        deployment_services_api.api_client = client
        return deployment_services_api
    def _init_device_settings_client(self):
        # Construct base URL by appending the service-specific path suffix
        # Host: https://api.sase.paloaltonetworks.com
        # Suffix: /config/device/v1
        config = DeviceSettingsConfiguration(
            host=f"https://{self.host}/config/device/v1"
        )
        config.verify_ssl = self.verify_ssl
        config.access_token = self._access_token

        client = DeviceSettingsApiClient(config)

        # Wrap the rest client's request method to auto-refresh tokens
        client.rest_client.request = _create_auto_refresh_wrapper(
            self, client.rest_client.request
        )

        device_settings_api.api_client = client
        return device_settings_api
    def _init_identity_services_client(self):
        # Construct base URL by appending the service-specific path suffix
        # Host: https://api.sase.paloaltonetworks.com
        # Suffix: /config/identity/v1
        config = IdentityServicesConfiguration(
            host=f"https://{self.host}/config/identity/v1"
        )
        config.verify_ssl = self.verify_ssl
        config.access_token = self._access_token

        client = IdentityServicesApiClient(config)

        # Wrap the rest client's request method to auto-refresh tokens
        client.rest_client.request = _create_auto_refresh_wrapper(
            self, client.rest_client.request
        )

        identity_services_api.api_client = client
        return identity_services_api
    def _init_network_services_client(self):
        # Construct base URL by appending the service-specific path suffix
        # Host: https://api.sase.paloaltonetworks.com
        # Suffix: /config/network/v1
        config = NetworkServicesConfiguration(
            host=f"https://{self.host}/config/network/v1"
        )
        config.verify_ssl = self.verify_ssl
        config.access_token = self._access_token

        client = NetworkServicesApiClient(config)

        # Wrap the rest client's request method to auto-refresh tokens
        client.rest_client.request = _create_auto_refresh_wrapper(
            self, client.rest_client.request
        )

        network_services_api.api_client = client
        return network_services_api
    def _init_objects_client(self):
        # Construct base URL by appending the service-specific path suffix
        # Host: https://api.sase.paloaltonetworks.com
        # Suffix: /config/objects/v1
        config = ObjectsConfiguration(
            host=f"https://{self.host}/config/objects/v1"
        )
        config.verify_ssl = self.verify_ssl
        config.access_token = self._access_token

        client = ObjectsApiClient(config)

        # Wrap the rest client's request method to auto-refresh tokens
        client.rest_client.request = _create_auto_refresh_wrapper(
            self, client.rest_client.request
        )

        objects_api.api_client = client
        return objects_api
    def _init_security_services_client(self):
        # Construct base URL by appending the service-specific path suffix
        # Host: https://api.sase.paloaltonetworks.com
        # Suffix: /config/security/v1
        config = SecurityServicesConfiguration(
            host=f"https://{self.host}/config/security/v1"
        )
        config.verify_ssl = self.verify_ssl
        config.access_token = self._access_token

        client = SecurityServicesApiClient(config)

        # Wrap the rest client's request method to auto-refresh tokens
        client.rest_client.request = _create_auto_refresh_wrapper(
            self, client.rest_client.request
        )

        security_services_api.api_client = client
        return security_services_api
