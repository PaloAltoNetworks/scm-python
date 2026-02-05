
import os
import json
import logging
import time
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

class Scm:
    """
    Unified SCM Client that provides access to all services.

    Configuration Priority:
    1. Constructor arguments
    2. Environment variables
    3. JSON configuration file (~/.scm/config.json or SCM_CONFIG_FILE)

    Environment Variables (consistent with scm-go):
    - SCM_CLIENT_ID: Client ID for authentication
    - SCM_CLIENT_SECRET: Client secret for authentication
    - SCM_SCOPE: Scope in format "tsg_id:XXXXX" (preferred over SCM_TSG_ID)
    - SCM_TSG_ID: TSG ID (backward compatibility, internally converted to scope)
    - SCM_HOST: API host (default: api.sase.paloaltonetworks.com)
    - SCM_AUTH_URL: Auth URL (default: https://auth.apps.paloaltonetworks.com)
    - SCM_LOGGING: Log level - quiet, basic, or detailed (preferred over SCM_LOG_LEVEL)
    - SCM_LOG_LEVEL: Log level - ERROR, WARNING, INFO, DEBUG (backward compatibility)
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
        log_level: Optional[str] = None
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

        # Check for cached JWT token from config file (consistent with scm-go field names)
        # Support both "jwt" (preferred) and "access_token" (backward compat)
        cached_token = file_config.get("jwt") or file_config.get("access_token")
        token_expires_at_str = file_config.get("jwt_expires_at") or file_config.get("token_expires_at")
        jwt_lifetime = file_config.get("jwt_lifetime")

        # Store token metadata
        self._access_token: Optional[str] = None
        self._token_expires_at: Optional[datetime] = None
        self._jwt_lifetime: Optional[int] = jwt_lifetime

        # Determine if we need to fetch a new token
        needs_new_token = True
        if cached_token and token_expires_at_str:
            try:
                # Parse expiration time (handle both with and without 'Z' suffix)
                expires_at = datetime.fromisoformat(token_expires_at_str.replace('Z', '+00:00'))

                # Check if token is still valid with expiration buffer (like scm-go)
                buffer_time = timedelta(seconds=self.TOKEN_EXPIRY_BUFFER)
                if datetime.now(expires_at.tzinfo) < (expires_at - buffer_time):
                    self._access_token = cached_token
                    self._token_expires_at = expires_at
                    needs_new_token = False
                    logger.info(f"Using cached JWT from config file (expires at {expires_at.isoformat()})")
                else:
                    logger.info("Cached token has expired or expiring soon, fetching new token")
            except (ValueError, TypeError) as e:
                logger.warning(f"Failed to parse token expiration time: {e}, fetching new token")

        # Fetch new token if needed
        if needs_new_token:
            self._fetch_and_store_token()

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
        """
        config_path = os.environ.get("SCM_CONFIG_FILE", os.path.expanduser("~/.scm/config.json"))
        path = Path(config_path)

        if not path.exists():
            return {}

        try:
            with open(path, "r") as f:
                return json.load(f)
        except Exception as e:
            logger.warning(f"Failed to load config file at {config_path}: {e}")
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

        # Configure retry strategy (similar to scm-go)
        retry_strategy = Retry(
            total=3,
            backoff_factor=0.3,
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

        Returns:
            str: The new access token

        Raises:
            ValueError: If token refresh fails
        """
        logger.info("Manually refreshing access token...")
        self._fetch_and_store_token()

        # Update all sub-clients with new token
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

        return self._access_token

    @property
    def token_expires_soon(self) -> bool:
        """
        Check if the token will expire soon.

        Returns:
            bool: True if token is missing or expiring within TOKEN_EXPIRY_BUFFER seconds
        """
        if not self._access_token or not self._token_expires_at:
            return True

        return datetime.now(self._token_expires_at.tzinfo) >= self._token_expires_at

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
        security_services_api.api_client = client
        return security_services_api
