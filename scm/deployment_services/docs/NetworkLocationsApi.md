# scm_deployment_services.NetworkLocationsApi

All URIs are relative to *https://api.strata.paloaltonetworks.com/config/deployment/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_locations**](NetworkLocationsApi.md#list_locations) | **GET** /locations | List locations


# **list_locations**
> object list_locations()

List locations

Retrieve a list of Prisma Access locations. 

### Example

* Bearer (JWT) Authentication (scmToken):

```python
import scm_deployment_services
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
    api_instance = scm_deployment_services.NetworkLocationsApi(api_client)

    try:
        # List locations
        api_response = api_instance.list_locations()
        print("The response of NetworkLocationsApi->list_locations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NetworkLocationsApi->list_locations: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

**object**

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
**409** | Conflict |  -  |
**0** | General Errors |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

