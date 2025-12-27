# scm_network_services.AutoVPNConfigPushApi

All URIs are relative to *https://api.strata.paloaltonetworks.com/config/network/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_auto_vpn_push_configs**](AutoVPNConfigPushApi.md#create_auto_vpn_push_configs) | **POST** /auto-vpn-push | Push Auto VPN configs


# **create_auto_vpn_push_configs**
> AutoVpnPushResponse create_auto_vpn_push_configs(auto_vpn_push_config=auto_vpn_push_config)

Push Auto VPN configs

Push Auto VPN configs. 

### Example

* Bearer (JWT) Authentication (scmToken):

```python
import scm_network_services
from scm_network_services.models.auto_vpn_push_config import AutoVpnPushConfig
from scm_network_services.models.auto_vpn_push_response import AutoVpnPushResponse
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
    api_instance = scm_network_services.AutoVPNConfigPushApi(api_client)
    auto_vpn_push_config = scm_network_services.AutoVpnPushConfig() # AutoVpnPushConfig | Created (optional)

    try:
        # Push Auto VPN configs
        api_response = api_instance.create_auto_vpn_push_configs(auto_vpn_push_config=auto_vpn_push_config)
        print("The response of AutoVPNConfigPushApi->create_auto_vpn_push_configs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AutoVPNConfigPushApi->create_auto_vpn_push_configs: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **auto_vpn_push_config** | [**AutoVpnPushConfig**](AutoVpnPushConfig.md)| Created | [optional] 

### Return type

[**AutoVpnPushResponse**](AutoVpnPushResponse.md)

### Authorization

[scmToken](../README.md#scmToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | OK |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**409** |  |  -  |
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

