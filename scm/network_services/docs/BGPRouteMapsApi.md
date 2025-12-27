# scm_network_services.BGPRouteMapsApi

All URIs are relative to *https://api.strata.paloaltonetworks.com/config/network/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_bgp_route_maps**](BGPRouteMapsApi.md#create_bgp_route_maps) | **POST** /bgp-route-maps | Create a BGP route map
[**delete_bgp_route_maps_by_id**](BGPRouteMapsApi.md#delete_bgp_route_maps_by_id) | **DELETE** /bgp-route-maps/{id} | Delete a BGP route map
[**get_bgp_route_maps_by_id**](BGPRouteMapsApi.md#get_bgp_route_maps_by_id) | **GET** /bgp-route-maps/{id} | Get a BGP route map
[**list_bgp_route_maps**](BGPRouteMapsApi.md#list_bgp_route_maps) | **GET** /bgp-route-maps | List BGP route maps
[**update_bgp_route_maps_by_id**](BGPRouteMapsApi.md#update_bgp_route_maps_by_id) | **PUT** /bgp-route-maps/{id} | Update a BGP route map


# **create_bgp_route_maps**
> BgpRouteMaps create_bgp_route_maps(bgp_route_maps=bgp_route_maps)

Create a BGP route map

Create a new BGP route map. 

### Example

* Bearer (JWT) Authentication (scmToken):

```python
import scm_network_services
from scm_network_services.models.bgp_route_maps import BgpRouteMaps
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
    api_instance = scm_network_services.BGPRouteMapsApi(api_client)
    bgp_route_maps = scm_network_services.BgpRouteMaps() # BgpRouteMaps | Created (optional)

    try:
        # Create a BGP route map
        api_response = api_instance.create_bgp_route_maps(bgp_route_maps=bgp_route_maps)
        print("The response of BGPRouteMapsApi->create_bgp_route_maps:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BGPRouteMapsApi->create_bgp_route_maps: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bgp_route_maps** | [**BgpRouteMaps**](BgpRouteMaps.md)| Created | [optional] 

### Return type

[**BgpRouteMaps**](BgpRouteMaps.md)

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

# **delete_bgp_route_maps_by_id**
> delete_bgp_route_maps_by_id(id)

Delete a BGP route map

Delete a BGP route map. 

### Example

* Bearer (JWT) Authentication (scmToken):

```python
import scm_network_services
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
    api_instance = scm_network_services.BGPRouteMapsApi(api_client)
    id = '123e4567-e89b-12d3-a456-426655440000' # str | The UUID of the configuration resource

    try:
        # Delete a BGP route map
        api_instance.delete_bgp_route_maps_by_id(id)
    except Exception as e:
        print("Exception when calling BGPRouteMapsApi->delete_bgp_route_maps_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The UUID of the configuration resource | 

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
**200** |  |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |
**409** |  |  -  |
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_bgp_route_maps_by_id**
> BgpRouteMaps get_bgp_route_maps_by_id(id)

Get a BGP route map

Get an existing BGP route map. 

### Example

* Bearer (JWT) Authentication (scmToken):

```python
import scm_network_services
from scm_network_services.models.bgp_route_maps import BgpRouteMaps
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
    api_instance = scm_network_services.BGPRouteMapsApi(api_client)
    id = '123e4567-e89b-12d3-a456-426655440000' # str | The UUID of the configuration resource

    try:
        # Get a BGP route map
        api_response = api_instance.get_bgp_route_maps_by_id(id)
        print("The response of BGPRouteMapsApi->get_bgp_route_maps_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BGPRouteMapsApi->get_bgp_route_maps_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The UUID of the configuration resource | 

### Return type

[**BgpRouteMaps**](BgpRouteMaps.md)

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

# **list_bgp_route_maps**
> BGPRouteMapsListResponse list_bgp_route_maps(limit=limit, offset=offset, name=name, folder=folder, snippet=snippet, device=device)

List BGP route maps

Retrieve a list of BGP route maps. 

### Example

* Bearer (JWT) Authentication (scmToken):

```python
import scm_network_services
from scm_network_services.models.bgp_route_maps_list_response import BGPRouteMapsListResponse
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
    api_instance = scm_network_services.BGPRouteMapsApi(api_client)
    limit = 200 # int | The maximum number of results per page (optional) (default to 200)
    offset = 0 # int | The offset into the list of results returned (optional) (default to 0)
    name = 'name_example' # str | The name of the configuration resource (optional)
    folder = 'folder_example' # str | The folder in which the resource is defined  (optional)
    snippet = 'snippet_example' # str | The snippet in which the resource is defined  (optional)
    device = 'device_example' # str | The device in which the resource is defined  (optional)

    try:
        # List BGP route maps
        api_response = api_instance.list_bgp_route_maps(limit=limit, offset=offset, name=name, folder=folder, snippet=snippet, device=device)
        print("The response of BGPRouteMapsApi->list_bgp_route_maps:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BGPRouteMapsApi->list_bgp_route_maps: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| The maximum number of results per page | [optional] [default to 200]
 **offset** | **int**| The offset into the list of results returned | [optional] [default to 0]
 **name** | **str**| The name of the configuration resource | [optional] 
 **folder** | **str**| The folder in which the resource is defined  | [optional] 
 **snippet** | **str**| The snippet in which the resource is defined  | [optional] 
 **device** | **str**| The device in which the resource is defined  | [optional] 

### Return type

[**BGPRouteMapsListResponse**](BGPRouteMapsListResponse.md)

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

# **update_bgp_route_maps_by_id**
> BgpRouteMaps update_bgp_route_maps_by_id(id, bgp_route_maps=bgp_route_maps)

Update a BGP route map

Update an existing BGP route map. 

### Example

* Bearer (JWT) Authentication (scmToken):

```python
import scm_network_services
from scm_network_services.models.bgp_route_maps import BgpRouteMaps
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
    api_instance = scm_network_services.BGPRouteMapsApi(api_client)
    id = '123e4567-e89b-12d3-a456-426655440000' # str | The UUID of the configuration resource
    bgp_route_maps = scm_network_services.BgpRouteMaps() # BgpRouteMaps | OK (optional)

    try:
        # Update a BGP route map
        api_response = api_instance.update_bgp_route_maps_by_id(id, bgp_route_maps=bgp_route_maps)
        print("The response of BGPRouteMapsApi->update_bgp_route_maps_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BGPRouteMapsApi->update_bgp_route_maps_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The UUID of the configuration resource | 
 **bgp_route_maps** | [**BgpRouteMaps**](BgpRouteMaps.md)| OK | [optional] 

### Return type

[**BgpRouteMaps**](BgpRouteMaps.md)

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

