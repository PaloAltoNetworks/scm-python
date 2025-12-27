# scm_network_services.AutoVPNMonitorApi

All URIs are relative to *https://api.strata.paloaltonetworks.com/config/network/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_auto_vpn_monitor**](AutoVPNMonitorApi.md#get_auto_vpn_monitor) | **GET** /auto-vpn-monitor | Get Auto VPN status


# **get_auto_vpn_monitor**
> GetAutoVPNMonitor200Response get_auto_vpn_monitor()

Get Auto VPN status

Get the status of the Auto VPN clusters. 

### Example

* Bearer (JWT) Authentication (scmToken):

```python
import scm_network_services
from scm_network_services.models.get_auto_vpn_monitor200_response import GetAutoVPNMonitor200Response
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
    api_instance = scm_network_services.AutoVPNMonitorApi(api_client)

    try:
        # Get Auto VPN status
        api_response = api_instance.get_auto_vpn_monitor()
        print("The response of AutoVPNMonitorApi->get_auto_vpn_monitor:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AutoVPNMonitorApi->get_auto_vpn_monitor: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**GetAutoVPNMonitor200Response**](GetAutoVPNMonitor200Response.md)

### Authorization

[scmToken](../README.md#scmToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

