
import os
from typing import Optional

# Import all sub-clients
from scm.config_setup import api as config_setup_api
# CHANGE: Explicitly import ApiClient and Configuration from their specific modules
# because the generated __init__.py in sub-packages often does not expose them.
from scm.config_setup.api_client import ApiClient as ConfigSetupApiClient
from scm.config_setup.configuration import Configuration as ConfigSetupConfiguration
from scm.deployment_services import api as deployment_services_api
# CHANGE: Explicitly import ApiClient and Configuration from their specific modules
# because the generated __init__.py in sub-packages often does not expose them.
from scm.deployment_services.api_client import ApiClient as DeploymentServicesApiClient
from scm.deployment_services.configuration import Configuration as DeploymentServicesConfiguration
from scm.device_settings import api as device_settings_api
# CHANGE: Explicitly import ApiClient and Configuration from their specific modules
# because the generated __init__.py in sub-packages often does not expose them.
from scm.device_settings.api_client import ApiClient as DeviceSettingsApiClient
from scm.device_settings.configuration import Configuration as DeviceSettingsConfiguration
from scm.identity_services import api as identity_services_api
# CHANGE: Explicitly import ApiClient and Configuration from their specific modules
# because the generated __init__.py in sub-packages often does not expose them.
from scm.identity_services.api_client import ApiClient as IdentityServicesApiClient
from scm.identity_services.configuration import Configuration as IdentityServicesConfiguration
from scm.network_services import api as network_services_api
# CHANGE: Explicitly import ApiClient and Configuration from their specific modules
# because the generated __init__.py in sub-packages often does not expose them.
from scm.network_services.api_client import ApiClient as NetworkServicesApiClient
from scm.network_services.configuration import Configuration as NetworkServicesConfiguration
from scm.objects import api as objects_api
# CHANGE: Explicitly import ApiClient and Configuration from their specific modules
# because the generated __init__.py in sub-packages often does not expose them.
from scm.objects.api_client import ApiClient as ObjectsApiClient
from scm.objects.configuration import Configuration as ObjectsConfiguration
from scm.security_services import api as security_services_api
# CHANGE: Explicitly import ApiClient and Configuration from their specific modules
# because the generated __init__.py in sub-packages often does not expose them.
from scm.security_services.api_client import ApiClient as SecurityServicesApiClient
from scm.security_services.configuration import Configuration as SecurityServicesConfiguration

class Scm:
    """
    Unified SCM Client that provides access to all services.
    """
    def __init__(
        self, 
        client_id: Optional[str] = None, 
        client_secret: Optional[str] = None, 
        tsg_id: Optional[str] = None,
        host: str = "api.sase.paloaltonetworks.com",
        verify_ssl: bool = True,
        log_level: str = "ERROR"
    ):
        self.client_id = client_id or os.environ.get("SCM_CLIENT_ID")
        self.client_secret = client_secret or os.environ.get("SCM_CLIENT_SECRET")
        self.tsg_id = tsg_id or os.environ.get("SCM_TSG_ID")
        self.host = host
        self.verify_ssl = verify_ssl

        if not self.client_id or not self.client_secret:
            raise ValueError("client_id and client_secret must be provided or set in environment variables.")

        # Shared OAuth setup would go here (getting the token once)
        # For now, we configure each sub-client individually
        
        self._access_token = self._fetch_access_token()

        # Initialize sub-clients
        self.config_setup = self._init_config_setup_client()
        self.deployment_services = self._init_deployment_services_client()
        self.device_settings = self._init_device_settings_client()
        self.identity_services = self._init_identity_services_client()
        self.network_services = self._init_network_services_client()
        self.objects = self._init_objects_client()
        self.security_services = self._init_security_services_client()

    def _fetch_access_token(self) -> str:
        # TODO: Implement actual OAuth2 flow here using requests
        # For generated SDKs, we might pass the token directly if the generator supports it,
        # or configure the ApiClient to handle it.
        # Placeholder return:
        return "PLACEHOLDER_TOKEN"
    def _init_config_setup_client(self):
        config = ConfigSetupConfiguration(
            host=f"https://{self.host}"
        )
        config.verify_ssl = self.verify_ssl
        config.access_token = self._access_token
        
        # Instantiate the client
        client = ConfigSetupApiClient(config)
        
        # Return the API module. 
        # Note: Users will still need to instantiate the specific APIs themselves
        # e.g., client.objects.AddressesApi(client.objects.api_client) 
        # unless we wrap this further.
        return config_setup_api
    def _init_deployment_services_client(self):
        config = DeploymentServicesConfiguration(
            host=f"https://{self.host}"
        )
        config.verify_ssl = self.verify_ssl
        config.access_token = self._access_token
        
        # Instantiate the client
        client = DeploymentServicesApiClient(config)
        
        # Return the API module. 
        # Note: Users will still need to instantiate the specific APIs themselves
        # e.g., client.objects.AddressesApi(client.objects.api_client) 
        # unless we wrap this further.
        return deployment_services_api
    def _init_device_settings_client(self):
        config = DeviceSettingsConfiguration(
            host=f"https://{self.host}"
        )
        config.verify_ssl = self.verify_ssl
        config.access_token = self._access_token
        
        # Instantiate the client
        client = DeviceSettingsApiClient(config)
        
        # Return the API module. 
        # Note: Users will still need to instantiate the specific APIs themselves
        # e.g., client.objects.AddressesApi(client.objects.api_client) 
        # unless we wrap this further.
        return device_settings_api
    def _init_identity_services_client(self):
        config = IdentityServicesConfiguration(
            host=f"https://{self.host}"
        )
        config.verify_ssl = self.verify_ssl
        config.access_token = self._access_token
        
        # Instantiate the client
        client = IdentityServicesApiClient(config)
        
        # Return the API module. 
        # Note: Users will still need to instantiate the specific APIs themselves
        # e.g., client.objects.AddressesApi(client.objects.api_client) 
        # unless we wrap this further.
        return identity_services_api
    def _init_network_services_client(self):
        config = NetworkServicesConfiguration(
            host=f"https://{self.host}"
        )
        config.verify_ssl = self.verify_ssl
        config.access_token = self._access_token
        
        # Instantiate the client
        client = NetworkServicesApiClient(config)
        
        # Return the API module. 
        # Note: Users will still need to instantiate the specific APIs themselves
        # e.g., client.objects.AddressesApi(client.objects.api_client) 
        # unless we wrap this further.
        return network_services_api
    def _init_objects_client(self):
        config = ObjectsConfiguration(
            host=f"https://{self.host}"
        )
        config.verify_ssl = self.verify_ssl
        config.access_token = self._access_token
        
        # Instantiate the client
        client = ObjectsApiClient(config)
        
        # Return the API module. 
        # Note: Users will still need to instantiate the specific APIs themselves
        # e.g., client.objects.AddressesApi(client.objects.api_client) 
        # unless we wrap this further.
        return objects_api
    def _init_security_services_client(self):
        config = SecurityServicesConfiguration(
            host=f"https://{self.host}"
        )
        config.verify_ssl = self.verify_ssl
        config.access_token = self._access_token
        
        # Instantiate the client
        client = SecurityServicesApiClient(config)
        
        # Return the API module. 
        # Note: Users will still need to instantiate the specific APIs themselves
        # e.g., client.objects.AddressesApi(client.objects.api_client) 
        # unless we wrap this further.
        return security_services_api
