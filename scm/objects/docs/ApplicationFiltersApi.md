# scm.objects.ApplicationFiltersApi

All URIs are relative to *https://api.strata.paloaltonetworks.com/config/objects/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_application_filters**](ApplicationFiltersApi.md#create_application_filters) | **POST** /application-filters | Create an application filter
[**delete_application_filters_by_id**](ApplicationFiltersApi.md#delete_application_filters_by_id) | **DELETE** /application-filters/{id} | Delete an application filter
[**get_application_filters_by_id**](ApplicationFiltersApi.md#get_application_filters_by_id) | **GET** /application-filters/{id} | Get an application filter
[**list_application_filters**](ApplicationFiltersApi.md#list_application_filters) | **GET** /application-filters | List application filters
[**update_application_filters_by_id**](ApplicationFiltersApi.md#update_application_filters_by_id) | **PUT** /application-filters/{id} | Update an application filter


# **create_application_filters**
> ApplicationFilters create_application_filters(application_filters=application_filters)

Create an application filter

Create a new application filter. 

### Example

* Bearer (JWT) Authentication (scmToken):

```python
import scm.objects
from scm.objects.models.application_filters import ApplicationFilters
from scm.objects.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.strata.paloaltonetworks.com/config/objects/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = scm.objects.Configuration(
    host = "https://api.strata.paloaltonetworks.com/config/objects/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): scmToken
configuration = scm.objects.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with scm.objects.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = scm.objects.ApplicationFiltersApi(api_client)
    application_filters = scm.objects.ApplicationFilters() # ApplicationFilters | Created (optional)

    try:
        # Create an application filter
        api_response = api_instance.create_application_filters(application_filters=application_filters)
        print("The response of ApplicationFiltersApi->create_application_filters:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApplicationFiltersApi->create_application_filters: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_filters** | [**ApplicationFilters**](ApplicationFilters.md)| Created | [optional] 

### Return type

[**ApplicationFilters**](ApplicationFilters.md)

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

# **delete_application_filters_by_id**
> delete_application_filters_by_id(id)

Delete an application filter

Delete an application filter. 

### Example

* Bearer (JWT) Authentication (scmToken):

```python
import scm.objects
from scm.objects.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.strata.paloaltonetworks.com/config/objects/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = scm.objects.Configuration(
    host = "https://api.strata.paloaltonetworks.com/config/objects/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): scmToken
configuration = scm.objects.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with scm.objects.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = scm.objects.ApplicationFiltersApi(api_client)
    id = '123e4567-e89b-12d3-a456-426655440000' # str | The UUID of the configuration resource

    try:
        # Delete an application filter
        api_instance.delete_application_filters_by_id(id)
    except Exception as e:
        print("Exception when calling ApplicationFiltersApi->delete_application_filters_by_id: %s\n" % e)
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

# **get_application_filters_by_id**
> ApplicationFilters get_application_filters_by_id(id)

Get an application filter

Get an existing application filter. 

### Example

* Bearer (JWT) Authentication (scmToken):

```python
import scm.objects
from scm.objects.models.application_filters import ApplicationFilters
from scm.objects.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.strata.paloaltonetworks.com/config/objects/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = scm.objects.Configuration(
    host = "https://api.strata.paloaltonetworks.com/config/objects/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): scmToken
configuration = scm.objects.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with scm.objects.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = scm.objects.ApplicationFiltersApi(api_client)
    id = '123e4567-e89b-12d3-a456-426655440000' # str | The UUID of the configuration resource

    try:
        # Get an application filter
        api_response = api_instance.get_application_filters_by_id(id)
        print("The response of ApplicationFiltersApi->get_application_filters_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApplicationFiltersApi->get_application_filters_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The UUID of the configuration resource | 

### Return type

[**ApplicationFilters**](ApplicationFilters.md)

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

# **list_application_filters**
> ApplicationFiltersListResponse list_application_filters(name=name, folder=folder, snippet=snippet, device=device, offset=offset, limit=limit)

List application filters

Retrieve a list of application filters. 

### Example

* Bearer (JWT) Authentication (scmToken):

```python
import scm.objects
from scm.objects.models.application_filters_list_response import ApplicationFiltersListResponse
from scm.objects.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.strata.paloaltonetworks.com/config/objects/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = scm.objects.Configuration(
    host = "https://api.strata.paloaltonetworks.com/config/objects/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): scmToken
configuration = scm.objects.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with scm.objects.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = scm.objects.ApplicationFiltersApi(api_client)
    name = 'name_example' # str | The name of the configuration resource (optional)
    folder = 'folder_example' # str | The folder in which the resource is defined  (optional)
    snippet = 'snippet_example' # str | The snippet in which the resource is defined  (optional)
    device = 'device_example' # str | The device in which the resource is defined  (optional)
    offset = 0 # int | The offset into the list of results returned (optional) (default to 0)
    limit = 200 # int | The maximum number of results per page (optional) (default to 200)

    try:
        # List application filters
        api_response = api_instance.list_application_filters(name=name, folder=folder, snippet=snippet, device=device, offset=offset, limit=limit)
        print("The response of ApplicationFiltersApi->list_application_filters:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApplicationFiltersApi->list_application_filters: %s\n" % e)
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

[**ApplicationFiltersListResponse**](ApplicationFiltersListResponse.md)

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

# **update_application_filters_by_id**
> ApplicationFilters update_application_filters_by_id(id, application_filters=application_filters)

Update an application filter

Update an existing application filter. 

### Example

* Bearer (JWT) Authentication (scmToken):

```python
import scm.objects
from scm.objects.models.application_filters import ApplicationFilters
from scm.objects.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.strata.paloaltonetworks.com/config/objects/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = scm.objects.Configuration(
    host = "https://api.strata.paloaltonetworks.com/config/objects/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): scmToken
configuration = scm.objects.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with scm.objects.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = scm.objects.ApplicationFiltersApi(api_client)
    id = '123e4567-e89b-12d3-a456-426655440000' # str | The UUID of the configuration resource
    application_filters = scm.objects.ApplicationFilters() # ApplicationFilters | OK (optional)

    try:
        # Update an application filter
        api_response = api_instance.update_application_filters_by_id(id, application_filters=application_filters)
        print("The response of ApplicationFiltersApi->update_application_filters_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApplicationFiltersApi->update_application_filters_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The UUID of the configuration resource | 
 **application_filters** | [**ApplicationFilters**](ApplicationFilters.md)| OK | [optional] 

### Return type

[**ApplicationFilters**](ApplicationFilters.md)

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

