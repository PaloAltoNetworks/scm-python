
import os
import json
import logging
from typing import Optional, Dict, Any
from pathlib import Path
from oauthlib.oauth2 import BackendApplicationClient
from requests_oauthlib import OAuth2Session

# Import all sub-clients
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
    """
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
        self.tsg_id = (
            tsg_id 
            or os.environ.get("SCM_TSG_ID") 
            or file_config.get("tsg_id")
            or file_config.get("scope", "").replace("tsg_id:", "")
        )
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
        
        # Handle log level
        _log_level_str = (
            log_level 
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

        # Authenticate immediately
        self._access_token = self._fetch_access_token()

        # Initialize sub-clients
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

    def _fetch_access_token(self) -> str:
        """
        Fetches the OAuth2 access token using requests-oauthlib.
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
        
        # 2. Create the session
        oauth = OAuth2Session(client=client)
        
        # 3. Fetch the token
        try:
            token = oauth.fetch_token(
                token_url=token_url, 
                client_id=self.client_id, 
                client_secret=self.client_secret,
                verify=self.verify_ssl
            )
            logger.info("Authentication successful.")
            return token["access_token"]
        except Exception as e:
            logger.error(f"Authentication Failed: {str(e)}")
            raise ValueError(f"Failed to authenticate with SCM via OAuth2: {str(e)}")
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
