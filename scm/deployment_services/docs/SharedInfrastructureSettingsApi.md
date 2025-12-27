# scm_deployment_services.SharedInfrastructureSettingsApi

All URIs are relative to *https://api.strata.paloaltonetworks.com/config/deployment/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_shared_infrastructure_settings**](SharedInfrastructureSettingsApi.md#get_shared_infrastructure_settings) | **GET** /shared-infrastructure-settings | Get shared infrastructure settings
[**update_shared_infrastructure_settings**](SharedInfrastructureSettingsApi.md#update_shared_infrastructure_settings) | **PUT** /shared-infrastructure-settings | Update infrastructure settings


# **get_shared_infrastructure_settings**
> SharedInfrastructureSettings get_shared_infrastructure_settings()

Get shared infrastructure settings

Get the Prisma Access shared infrastructure settings. 

### Example

* Bearer (JWT) Authentication (scmToken):

```python
import scm_deployment_services
from scm_deployment_services.models.shared_infrastructure_settings import SharedInfrastructureSettings
from scm_deployment_services.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.strata.paloaltonetworks.com/config/deployment/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = scm_deployment_services.Configuration(
    host = "https://api.strata.paloaltonetworks.com/config/deployment/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): scmToken
configuration = scm_deployment_services.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with scm_deployment_services.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = scm_deployment_services.SharedInfrastructureSettingsApi(api_client)

    try:
        # Get shared infrastructure settings
        api_response = api_instance.get_shared_infrastructure_settings()
        print("The response of SharedInfrastructureSettingsApi->get_shared_infrastructure_settings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SharedInfrastructureSettingsApi->get_shared_infrastructure_settings: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**SharedInfrastructureSettings**](SharedInfrastructureSettings.md)

### Authorization

[scmToken](../README.md#scmToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**0** | General Errors |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_shared_infrastructure_settings**
> SharedInfrastructureSettings update_shared_infrastructure_settings(edit_shared_infrastructure_settings=edit_shared_infrastructure_settings)

Update infrastructure settings

Update the Prisma Access shared infrastructure settings. 

### Example

* Bearer (JWT) Authentication (scmToken):

```python
import scm_deployment_services
from scm_deployment_services.models.edit_shared_infrastructure_settings import EditSharedInfrastructureSettings
from scm_deployment_services.models.shared_infrastructure_settings import SharedInfrastructureSettings
from scm_deployment_services.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.strata.paloaltonetworks.com/config/deployment/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = scm_deployment_services.Configuration(
    host = "https://api.strata.paloaltonetworks.com/config/deployment/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): scmToken
configuration = scm_deployment_services.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with scm_deployment_services.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = scm_deployment_services.SharedInfrastructureSettingsApi(api_client)
    edit_shared_infrastructure_settings = scm_deployment_services.EditSharedInfrastructureSettings() # EditSharedInfrastructureSettings | OK (optional)

    try:
        # Update infrastructure settings
        api_response = api_instance.update_shared_infrastructure_settings(edit_shared_infrastructure_settings=edit_shared_infrastructure_settings)
        print("The response of SharedInfrastructureSettingsApi->update_shared_infrastructure_settings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SharedInfrastructureSettingsApi->update_shared_infrastructure_settings: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **edit_shared_infrastructure_settings** | [**EditSharedInfrastructureSettings**](EditSharedInfrastructureSettings.md)| OK | [optional] 

### Return type

[**SharedInfrastructureSettings**](SharedInfrastructureSettings.md)

### Authorization

[scmToken](../README.md#scmToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**409** | Conflict |  -  |
**0** | General Errors |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

