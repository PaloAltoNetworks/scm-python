# scm_objects.ExternalDynamicListsApi

All URIs are relative to *https://api.strata.paloaltonetworks.com/config/objects/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_external_dynamic_lists**](ExternalDynamicListsApi.md#create_external_dynamic_lists) | **POST** /external-dynamic-lists | Create an External Dynamic List
[**delete_external_dynamic_lists_by_id**](ExternalDynamicListsApi.md#delete_external_dynamic_lists_by_id) | **DELETE** /external-dynamic-lists/{id} | Delete an External Dynamic List
[**get_external_dynamic_lists_by_id**](ExternalDynamicListsApi.md#get_external_dynamic_lists_by_id) | **GET** /external-dynamic-lists/{id} | Get an External Dynamic List
[**list_external_dynamic_lists**](ExternalDynamicListsApi.md#list_external_dynamic_lists) | **GET** /external-dynamic-lists | List External Dynamic Lists
[**update_external_dynamic_lists_by_id**](ExternalDynamicListsApi.md#update_external_dynamic_lists_by_id) | **PUT** /external-dynamic-lists/{id} | Update an External Dynamic List


# **create_external_dynamic_lists**
> ExternalDynamicLists create_external_dynamic_lists(external_dynamic_lists=external_dynamic_lists)

Create an External Dynamic List

Create a new External Dynamic List. 

### Example

* Bearer (JWT) Authentication (scmToken):

```python
import scm_objects
from scm_objects.models.external_dynamic_lists import ExternalDynamicLists
from scm_objects.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.strata.paloaltonetworks.com/config/objects/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = scm_objects.Configuration(
    host = "https://api.strata.paloaltonetworks.com/config/objects/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): scmToken
configuration = scm_objects.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with scm_objects.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = scm_objects.ExternalDynamicListsApi(api_client)
    external_dynamic_lists = scm_objects.ExternalDynamicLists() # ExternalDynamicLists | Created (optional)

    try:
        # Create an External Dynamic List
        api_response = api_instance.create_external_dynamic_lists(external_dynamic_lists=external_dynamic_lists)
        print("The response of ExternalDynamicListsApi->create_external_dynamic_lists:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ExternalDynamicListsApi->create_external_dynamic_lists: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **external_dynamic_lists** | [**ExternalDynamicLists**](ExternalDynamicLists.md)| Created | [optional] 

### Return type

[**ExternalDynamicLists**](ExternalDynamicLists.md)

### Authorization

[scmToken](../README.md#scmToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | OK |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**409** | Conflict |  -  |
**0** | General Errors |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_external_dynamic_lists_by_id**
> delete_external_dynamic_lists_by_id(id)

Delete an External Dynamic List

Delete an External Dynamic List. 

### Example

* Bearer (JWT) Authentication (scmToken):

```python
import scm_objects
from scm_objects.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.strata.paloaltonetworks.com/config/objects/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = scm_objects.Configuration(
    host = "https://api.strata.paloaltonetworks.com/config/objects/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): scmToken
configuration = scm_objects.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with scm_objects.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = scm_objects.ExternalDynamicListsApi(api_client)
    id = '123e4567-e89b-12d3-a456-426655440000' # str | The UUID of the configuration resource

    try:
        # Delete an External Dynamic List
        api_instance.delete_external_dynamic_lists_by_id(id)
    except Exception as e:
        print("Exception when calling ExternalDynamicListsApi->delete_external_dynamic_lists_by_id: %s\n" % e)
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
**200** | OK |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**409** | Conflict |  -  |
**0** | General Errors |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_external_dynamic_lists_by_id**
> ExternalDynamicLists get_external_dynamic_lists_by_id(id)

Get an External Dynamic List

Get an existing External Dynamic List. 

### Example

* Bearer (JWT) Authentication (scmToken):

```python
import scm_objects
from scm_objects.models.external_dynamic_lists import ExternalDynamicLists
from scm_objects.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.strata.paloaltonetworks.com/config/objects/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = scm_objects.Configuration(
    host = "https://api.strata.paloaltonetworks.com/config/objects/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): scmToken
configuration = scm_objects.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with scm_objects.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = scm_objects.ExternalDynamicListsApi(api_client)
    id = '123e4567-e89b-12d3-a456-426655440000' # str | The UUID of the configuration resource

    try:
        # Get an External Dynamic List
        api_response = api_instance.get_external_dynamic_lists_by_id(id)
        print("The response of ExternalDynamicListsApi->get_external_dynamic_lists_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ExternalDynamicListsApi->get_external_dynamic_lists_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The UUID of the configuration resource | 

### Return type

[**ExternalDynamicLists**](ExternalDynamicLists.md)

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

# **list_external_dynamic_lists**
> ExternalDynamicListsListResponse list_external_dynamic_lists(name=name, folder=folder, snippet=snippet, device=device, offset=offset, limit=limit)

List External Dynamic Lists

Retrieve a list of External Dynamic Lists. 

### Example

* Bearer (JWT) Authentication (scmToken):

```python
import scm_objects
from scm_objects.models.external_dynamic_lists_list_response import ExternalDynamicListsListResponse
from scm_objects.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.strata.paloaltonetworks.com/config/objects/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = scm_objects.Configuration(
    host = "https://api.strata.paloaltonetworks.com/config/objects/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): scmToken
configuration = scm_objects.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with scm_objects.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = scm_objects.ExternalDynamicListsApi(api_client)
    name = 'name_example' # str | The name of the configuration resource (optional)
    folder = 'folder_example' # str | The folder in which the resource is defined  (optional)
    snippet = 'snippet_example' # str | The snippet in which the resource is defined  (optional)
    device = 'device_example' # str | The device in which the resource is defined  (optional)
    offset = 0 # int | The offset into the list of results returned (optional) (default to 0)
    limit = 200 # int | The maximum number of results per page (optional) (default to 200)

    try:
        # List External Dynamic Lists
        api_response = api_instance.list_external_dynamic_lists(name=name, folder=folder, snippet=snippet, device=device, offset=offset, limit=limit)
        print("The response of ExternalDynamicListsApi->list_external_dynamic_lists:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ExternalDynamicListsApi->list_external_dynamic_lists: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The name of the configuration resource | [optional] 
 **folder** | **str**| The folder in which the resource is defined  | [optional] 
 **snippet** | **str**| The snippet in which the resource is defined  | [optional] 
 **device** | **str**| The device in which the resource is defined  | [optional] 
 **offset** | **int**| The offset into the list of results returned | [optional] [default to 0]
 **limit** | **int**| The maximum number of results per page | [optional] [default to 200]

### Return type

[**ExternalDynamicListsListResponse**](ExternalDynamicListsListResponse.md)

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

# **update_external_dynamic_lists_by_id**
> ExternalDynamicLists update_external_dynamic_lists_by_id(id, external_dynamic_lists=external_dynamic_lists)

Update an External Dynamic List

Update an existing External Dynamic List. 

### Example

* Bearer (JWT) Authentication (scmToken):

```python
import scm_objects
from scm_objects.models.external_dynamic_lists import ExternalDynamicLists
from scm_objects.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.strata.paloaltonetworks.com/config/objects/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = scm_objects.Configuration(
    host = "https://api.strata.paloaltonetworks.com/config/objects/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): scmToken
configuration = scm_objects.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with scm_objects.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = scm_objects.ExternalDynamicListsApi(api_client)
    id = '123e4567-e89b-12d3-a456-426655440000' # str | The UUID of the configuration resource
    external_dynamic_lists = scm_objects.ExternalDynamicLists() # ExternalDynamicLists | OK (optional)

    try:
        # Update an External Dynamic List
        api_response = api_instance.update_external_dynamic_lists_by_id(id, external_dynamic_lists=external_dynamic_lists)
        print("The response of ExternalDynamicListsApi->update_external_dynamic_lists_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ExternalDynamicListsApi->update_external_dynamic_lists_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The UUID of the configuration resource | 
 **external_dynamic_lists** | [**ExternalDynamicLists**](ExternalDynamicLists.md)| OK | [optional] 

### Return type

[**ExternalDynamicLists**](ExternalDynamicLists.md)

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

