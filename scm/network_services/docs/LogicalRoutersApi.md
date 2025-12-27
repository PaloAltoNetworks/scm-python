# scm_network_services.LogicalRoutersApi

All URIs are relative to *https://api.strata.paloaltonetworks.com/config/network/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_logical_routers**](LogicalRoutersApi.md#create_logical_routers) | **POST** /logical-routers | Create a logical router
[**delete_logical_routers_by_id**](LogicalRoutersApi.md#delete_logical_routers_by_id) | **DELETE** /logical-routers/{id} | Delete a logical router
[**get_logical_routers_by_id**](LogicalRoutersApi.md#get_logical_routers_by_id) | **GET** /logical-routers/{id} | Get a logical router
[**list_logical_routers**](LogicalRoutersApi.md#list_logical_routers) | **GET** /logical-routers | List logical routers
[**update_logical_routers_by_id**](LogicalRoutersApi.md#update_logical_routers_by_id) | **PUT** /logical-routers/{id} | Update a logical router


# **create_logical_routers**
> LogicalRouters create_logical_routers(logical_routers=logical_routers)

Create a logical router

Create a new logical router. 

### Example

* Bearer (JWT) Authentication (scmToken):

```python
import scm_network_services
from scm_network_services.models.logical_routers import LogicalRouters
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
    api_instance = scm_network_services.LogicalRoutersApi(api_client)
    logical_routers = scm_network_services.LogicalRouters() # LogicalRouters | Created (optional)

    try:
        # Create a logical router
        api_response = api_instance.create_logical_routers(logical_routers=logical_routers)
        print("The response of LogicalRoutersApi->create_logical_routers:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LogicalRoutersApi->create_logical_routers: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **logical_routers** | [**LogicalRouters**](LogicalRouters.md)| Created | [optional] 

### Return type

[**LogicalRouters**](LogicalRouters.md)

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

# **delete_logical_routers_by_id**
> delete_logical_routers_by_id(id)

Delete a logical router

Delete a logical router. 

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
    api_instance = scm_network_services.LogicalRoutersApi(api_client)
    id = '123e4567-e89b-12d3-a456-426655440000' # str | The UUID of the configuration resource

    try:
        # Delete a logical router
        api_instance.delete_logical_routers_by_id(id)
    except Exception as e:
        print("Exception when calling LogicalRoutersApi->delete_logical_routers_by_id: %s\n" % e)
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

# **get_logical_routers_by_id**
> LogicalRouters get_logical_routers_by_id(id)

Get a logical router

Get an existing logical router. 

### Example

* Bearer (JWT) Authentication (scmToken):

```python
import scm_network_services
from scm_network_services.models.logical_routers import LogicalRouters
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
    api_instance = scm_network_services.LogicalRoutersApi(api_client)
    id = '123e4567-e89b-12d3-a456-426655440000' # str | The UUID of the configuration resource

    try:
        # Get a logical router
        api_response = api_instance.get_logical_routers_by_id(id)
        print("The response of LogicalRoutersApi->get_logical_routers_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LogicalRoutersApi->get_logical_routers_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The UUID of the configuration resource | 

### Return type

[**LogicalRouters**](LogicalRouters.md)

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

# **list_logical_routers**
> LogicalRoutersListResponse list_logical_routers(pagination=pagination, limit=limit, offset=offset, name=name, folder=folder, snippet=snippet, device=device)

List logical routers

Retrieve a list of logical routers. 

### Example

* Bearer (JWT) Authentication (scmToken):

```python
import scm_network_services
from scm_network_services.models.logical_routers_list_response import LogicalRoutersListResponse
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
    api_instance = scm_network_services.LogicalRoutersApi(api_client)
    pagination = True # bool | The parameter to mention if the response should be paginated. By default, its set to false (optional)
    limit = 200 # int | The maximum number of results per page (optional) (default to 200)
    offset = 0 # int | The offset into the list of results returned (optional) (default to 0)
    name = 'name_example' # str | The name of the configuration resource (optional)
    folder = 'folder_example' # str | The folder in which the resource is defined  (optional)
    snippet = 'snippet_example' # str | The snippet in which the resource is defined  (optional)
    device = 'device_example' # str | The device in which the resource is defined  (optional)

    try:
        # List logical routers
        api_response = api_instance.list_logical_routers(pagination=pagination, limit=limit, offset=offset, name=name, folder=folder, snippet=snippet, device=device)
        print("The response of LogicalRoutersApi->list_logical_routers:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LogicalRoutersApi->list_logical_routers: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pagination** | **bool**| The parameter to mention if the response should be paginated. By default, its set to false | [optional] 
 **limit** | **int**| The maximum number of results per page | [optional] [default to 200]
 **offset** | **int**| The offset into the list of results returned | [optional] [default to 0]
 **name** | **str**| The name of the configuration resource | [optional] 
 **folder** | **str**| The folder in which the resource is defined  | [optional] 
 **snippet** | **str**| The snippet in which the resource is defined  | [optional] 
 **device** | **str**| The device in which the resource is defined  | [optional] 

### Return type

[**LogicalRoutersListResponse**](LogicalRoutersListResponse.md)

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

# **update_logical_routers_by_id**
> LogicalRouters update_logical_routers_by_id(id, logical_routers=logical_routers)

Update a logical router

Update an existing logical router. 

### Example

* Bearer (JWT) Authentication (scmToken):

```python
import scm_network_services
from scm_network_services.models.logical_routers import LogicalRouters
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
    api_instance = scm_network_services.LogicalRoutersApi(api_client)
    id = '123e4567-e89b-12d3-a456-426655440000' # str | The UUID of the configuration resource
    logical_routers = scm_network_services.LogicalRouters() # LogicalRouters | OK (optional)

    try:
        # Update a logical router
        api_response = api_instance.update_logical_routers_by_id(id, logical_routers=logical_routers)
        print("The response of LogicalRoutersApi->update_logical_routers_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LogicalRoutersApi->update_logical_routers_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The UUID of the configuration resource | 
 **logical_routers** | [**LogicalRouters**](LogicalRouters.md)| OK | [optional] 

### Return type

[**LogicalRouters**](LogicalRouters.md)

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

