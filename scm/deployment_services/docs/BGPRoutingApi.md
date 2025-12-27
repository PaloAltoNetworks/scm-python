# scm_deployment_services.BGPRoutingApi

All URIs are relative to *https://api.strata.paloaltonetworks.com/config/deployment/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_bgp_routing**](BGPRoutingApi.md#get_bgp_routing) | **GET** /bgp-routing | Get BGP routing settings
[**update_bgp_routing**](BGPRoutingApi.md#update_bgp_routing) | **PUT** /bgp-routing | Update BGP routing settings


# **get_bgp_routing**
> BgpRouting get_bgp_routing()

Get BGP routing settings

Get Service Connection BGP routing settings. 

### Example

* Bearer (JWT) Authentication (scmToken):

```python
import scm_deployment_services
from scm_deployment_services.models.bgp_routing import BgpRouting
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
    api_instance = scm_deployment_services.BGPRoutingApi(api_client)

    try:
        # Get BGP routing settings
        api_response = api_instance.get_bgp_routing()
        print("The response of BGPRoutingApi->get_bgp_routing:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BGPRoutingApi->get_bgp_routing: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**BgpRouting**](BgpRouting.md)

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

# **update_bgp_routing**
> BgpRouting update_bgp_routing(bgp_routing=bgp_routing)

Update BGP routing settings

Update Service Connection BGP routing settings. 

### Example

* Bearer (JWT) Authentication (scmToken):

```python
import scm_deployment_services
from scm_deployment_services.models.bgp_routing import BgpRouting
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
    api_instance = scm_deployment_services.BGPRoutingApi(api_client)
    bgp_routing = scm_deployment_services.BgpRouting() # BgpRouting | OK (optional)

    try:
        # Update BGP routing settings
        api_response = api_instance.update_bgp_routing(bgp_routing=bgp_routing)
        print("The response of BGPRoutingApi->update_bgp_routing:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BGPRoutingApi->update_bgp_routing: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bgp_routing** | [**BgpRouting**](BgpRouting.md)| OK | [optional] 

### Return type

[**BgpRouting**](BgpRouting.md)

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

