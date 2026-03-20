# scm.network_services.AutoVPNSettingsApi

All URIs are relative to *https://api.strata.paloaltonetworks.com/config/network/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_auto_vpn_settings**](AutoVPNSettingsApi.md#get_auto_vpn_settings) | **GET** /auto-vpn-settings | Get Auto VPN settings
[**update_auto_vpn_settings**](AutoVPNSettingsApi.md#update_auto_vpn_settings) | **PUT** /auto-vpn-settings | Update Auto VPN settings


# **get_auto_vpn_settings**
> AutoVpnSettings get_auto_vpn_settings()

Get Auto VPN settings

Retrieve the Auto VPN settings. 

### Example

* Bearer (JWT) Authentication (scmToken):

```python
import scm.network_services
from scm.network_services.models.auto_vpn_settings import AutoVpnSettings
from scm.network_services.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.strata.paloaltonetworks.com/config/network/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = scm.network_services.Configuration(
    host = "https://api.strata.paloaltonetworks.com/config/network/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): scmToken
configuration = scm.network_services.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with scm.network_services.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = scm.network_services.AutoVPNSettingsApi(api_client)

    try:
        # Get Auto VPN settings
        api_response = api_instance.get_auto_vpn_settings()
        print("The response of AutoVPNSettingsApi->get_auto_vpn_settings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AutoVPNSettingsApi->get_auto_vpn_settings: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**AutoVpnSettings**](AutoVpnSettings.md)

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

# **update_auto_vpn_settings**
> AutoVpnSettings update_auto_vpn_settings(auto_vpn_settings=auto_vpn_settings)

Update Auto VPN settings

Update Auto VPN settings. 

### Example

* Bearer (JWT) Authentication (scmToken):

```python
import scm.network_services
from scm.network_services.models.auto_vpn_settings import AutoVpnSettings
from scm.network_services.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.strata.paloaltonetworks.com/config/network/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = scm.network_services.Configuration(
    host = "https://api.strata.paloaltonetworks.com/config/network/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): scmToken
configuration = scm.network_services.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with scm.network_services.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = scm.network_services.AutoVPNSettingsApi(api_client)
    auto_vpn_settings = scm.network_services.AutoVpnSettings() # AutoVpnSettings | OK (optional)

    try:
        # Update Auto VPN settings
        api_response = api_instance.update_auto_vpn_settings(auto_vpn_settings=auto_vpn_settings)
        print("The response of AutoVPNSettingsApi->update_auto_vpn_settings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AutoVPNSettingsApi->update_auto_vpn_settings: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **auto_vpn_settings** | [**AutoVpnSettings**](AutoVpnSettings.md)| OK | [optional] 

### Return type

[**AutoVpnSettings**](AutoVpnSettings.md)

### Authorization

[scmToken](../README.md#scmToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |
**409** |  |  -  |
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

