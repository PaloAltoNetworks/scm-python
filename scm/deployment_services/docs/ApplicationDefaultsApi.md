# scm.deployment_services.ApplicationDefaultsApi

All URIs are relative to *https://api.strata.paloaltonetworks.com/config/deployment/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_application_defaults**](ApplicationDefaultsApi.md#create_application_defaults) | **POST** /enable | Create application defaults


# **create_application_defaults**
> create_application_defaults()

Create application defaults

Create Prisma Access application defaults.  *These application defaults are normally created in the UI. This endpoint is necessary for customers that do not use the UI to create these application defaults such as certificates and configuration nodes.  This endpoint will be deprecated once the UI dependencies have been eliminated.* 

### Example

* Bearer (JWT) Authentication (scmToken):

```python
import scm.deployment_services
from scm.deployment_services.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.strata.paloaltonetworks.com/config/deployment/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = scm.deployment_services.Configuration(
    host = "https://api.strata.paloaltonetworks.com/config/deployment/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): scmToken
configuration = scm.deployment_services.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with scm.deployment_services.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = scm.deployment_services.ApplicationDefaultsApi(api_client)

    try:
        # Create application defaults
        api_instance.create_application_defaults()
    except Exception as e:
        print("Exception when calling ApplicationDefaultsApi->create_application_defaults: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[scmToken](../README.md#scmToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**409** | Conflict |  -  |
**0** | General Errors |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

