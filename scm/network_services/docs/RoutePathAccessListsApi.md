# scm_network_services.RoutePathAccessListsApi

All URIs are relative to *https://api.strata.paloaltonetworks.com/config/network/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_route_path_access_lists**](RoutePathAccessListsApi.md#create_route_path_access_lists) | **POST** /route-path-access-lists | Create a route path access list
[**delete_route_path_access_lists_by_id**](RoutePathAccessListsApi.md#delete_route_path_access_lists_by_id) | **DELETE** /route-path-access-lists/{id} | Delete a route path access list
[**get_route_path_access_lists_by_id**](RoutePathAccessListsApi.md#get_route_path_access_lists_by_id) | **GET** /route-path-access-lists/{id} | Get a route path access list
[**list_route_path_access_lists**](RoutePathAccessListsApi.md#list_route_path_access_lists) | **GET** /route-path-access-lists | List route path access lists
[**update_route_path_access_lists_by_id**](RoutePathAccessListsApi.md#update_route_path_access_lists_by_id) | **PUT** /route-path-access-lists/{id} | Update a route path access list


# **create_route_path_access_lists**
> RoutePathAccessLists create_route_path_access_lists(route_path_access_lists=route_path_access_lists)

Create a route path access list

Create a new route path access list. 

### Example

* Bearer (JWT) Authentication (scmToken):

```python
import scm_network_services
from scm_network_services.models.route_path_access_lists import RoutePathAccessLists
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
    api_instance = scm_network_services.RoutePathAccessListsApi(api_client)
    route_path_access_lists = scm_network_services.RoutePathAccessLists() # RoutePathAccessLists | Created (optional)

    try:
        # Create a route path access list
        api_response = api_instance.create_route_path_access_lists(route_path_access_lists=route_path_access_lists)
        print("The response of RoutePathAccessListsApi->create_route_path_access_lists:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RoutePathAccessListsApi->create_route_path_access_lists: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **route_path_access_lists** | [**RoutePathAccessLists**](RoutePathAccessLists.md)| Created | [optional] 

### Return type

[**RoutePathAccessLists**](RoutePathAccessLists.md)

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

# **delete_route_path_access_lists_by_id**
> delete_route_path_access_lists_by_id(id)

Delete a route path access list

Delete a route path access list. 

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
    api_instance = scm_network_services.RoutePathAccessListsApi(api_client)
    id = '123e4567-e89b-12d3-a456-426655440000' # str | The UUID of the configuration resource

    try:
        # Delete a route path access list
        api_instance.delete_route_path_access_lists_by_id(id)
    except Exception as e:
        print("Exception when calling RoutePathAccessListsApi->delete_route_path_access_lists_by_id: %s\n" % e)
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

# **get_route_path_access_lists_by_id**
> RoutePathAccessLists get_route_path_access_lists_by_id(id)

Get a route path access list

Get an existing route path access list. 

### Example

* Bearer (JWT) Authentication (scmToken):

```python
import scm_network_services
from scm_network_services.models.route_path_access_lists import RoutePathAccessLists
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
    api_instance = scm_network_services.RoutePathAccessListsApi(api_client)
    id = '123e4567-e89b-12d3-a456-426655440000' # str | The UUID of the configuration resource

    try:
        # Get a route path access list
        api_response = api_instance.get_route_path_access_lists_by_id(id)
        print("The response of RoutePathAccessListsApi->get_route_path_access_lists_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RoutePathAccessListsApi->get_route_path_access_lists_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The UUID of the configuration resource | 

### Return type

[**RoutePathAccessLists**](RoutePathAccessLists.md)

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

# **list_route_path_access_lists**
> RoutePathAccessListsListResponse list_route_path_access_lists(limit=limit, offset=offset, name=name, folder=folder, snippet=snippet, device=device)

List route path access lists

Retrieve a list of route path access lists. 

### Example

* Bearer (JWT) Authentication (scmToken):

```python
import scm_network_services
from scm_network_services.models.route_path_access_lists_list_response import RoutePathAccessListsListResponse
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
    api_instance = scm_network_services.RoutePathAccessListsApi(api_client)
    limit = 200 # int | The maximum number of results per page (optional) (default to 200)
    offset = 0 # int | The offset into the list of results returned (optional) (default to 0)
    name = 'name_example' # str | The name of the configuration resource (optional)
    folder = 'folder_example' # str | The folder in which the resource is defined  (optional)
    snippet = 'snippet_example' # str | The snippet in which the resource is defined  (optional)
    device = 'device_example' # str | The device in which the resource is defined  (optional)

    try:
        # List route path access lists
        api_response = api_instance.list_route_path_access_lists(limit=limit, offset=offset, name=name, folder=folder, snippet=snippet, device=device)
        print("The response of RoutePathAccessListsApi->list_route_path_access_lists:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RoutePathAccessListsApi->list_route_path_access_lists: %s\n" % e)
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

[**RoutePathAccessListsListResponse**](RoutePathAccessListsListResponse.md)

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

# **update_route_path_access_lists_by_id**
> RoutePathAccessLists update_route_path_access_lists_by_id(id, route_path_access_lists=route_path_access_lists)

Update a route path access list

Update an existing route path access list. 

### Example

* Bearer (JWT) Authentication (scmToken):

```python
import scm_network_services
from scm_network_services.models.route_path_access_lists import RoutePathAccessLists
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
    api_instance = scm_network_services.RoutePathAccessListsApi(api_client)
    id = '123e4567-e89b-12d3-a456-426655440000' # str | The UUID of the configuration resource
    route_path_access_lists = scm_network_services.RoutePathAccessLists() # RoutePathAccessLists | OK (optional)

    try:
        # Update a route path access list
        api_response = api_instance.update_route_path_access_lists_by_id(id, route_path_access_lists=route_path_access_lists)
        print("The response of RoutePathAccessListsApi->update_route_path_access_lists_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RoutePathAccessListsApi->update_route_path_access_lists_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The UUID of the configuration resource | 
 **route_path_access_lists** | [**RoutePathAccessLists**](RoutePathAccessLists.md)| OK | [optional] 

### Return type

[**RoutePathAccessLists**](RoutePathAccessLists.md)

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

