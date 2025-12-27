# scm_network_services.RemoteNetworksLicenseApi

All URIs are relative to *https://api.strata.paloaltonetworks.com/config/network/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_remote_networks_license_info**](RemoteNetworksLicenseApi.md#get_remote_networks_license_info) | **GET** /remote-networks-license-info | Get Remote Networks License Info


# **get_remote_networks_license_info**
> LicenseResult get_remote_networks_license_info()

Get Remote Networks License Info

Returns operational license model and site license counts.

### Example

* Bearer (JWT) Authentication (scmToken):

```python
import scm_network_services
from scm_network_services.models.license_result import LicenseResult
from scm_network_services.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.strata.paloaltonetworks.com/config/network/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = scm_network_services.Configuration(
    host = "https://api.strata.paloaltonetworks.com/config/network/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): scmToken
configuration = scm_network_services.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with scm_network_services.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = scm_network_services.RemoteNetworksLicenseApi(api_client)

    try:
        # Get Remote Networks License Info
        api_response = api_instance.get_remote_networks_license_info()
        print("The response of RemoteNetworksLicenseApi->get_remote_networks_license_info:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RemoteNetworksLicenseApi->get_remote_networks_license_info: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**LicenseResult**](LicenseResult.md)

### Authorization

[scmToken](../README.md#scmToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | License information retrieved successfully. |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |
**409** |  |  -  |
**500** | Failed to fetch license information. |  -  |
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

