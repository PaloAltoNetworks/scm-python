# scm_objects.ApplicationsApi

All URIs are relative to *https://api.strata.paloaltonetworks.com/config/objects/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_applications**](ApplicationsApi.md#create_applications) | **POST** /applications | Create an application
[**delete_applications_by_id**](ApplicationsApi.md#delete_applications_by_id) | **DELETE** /applications/{id} | Delete an application
[**get_applications_by_id**](ApplicationsApi.md#get_applications_by_id) | **GET** /applications/{id} | Get the application by id
[**list_applications**](ApplicationsApi.md#list_applications) | **GET** /applications | List applications
[**update_applications_by_id**](ApplicationsApi.md#update_applications_by_id) | **PUT** /applications/{id} | Update an application


# **create_applications**
> Applications create_applications(applications=applications)

Create an application

Create a new application. 

### Example

* Bearer (JWT) Authentication (scmToken):

```python
import scm_objects
from scm_objects.models.applications import Applications
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
    api_instance = scm_objects.ApplicationsApi(api_client)
    applications = scm_objects.Applications() # Applications | Created (optional)

    try:
        # Create an application
        api_response = api_instance.create_applications(applications=applications)
        print("The response of ApplicationsApi->create_applications:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApplicationsApi->create_applications: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **applications** | [**Applications**](Applications.md)| Created | [optional] 

### Return type

[**Applications**](Applications.md)

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

# **delete_applications_by_id**
> delete_applications_by_id(id)

Delete an application

Delete an application. 

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
    api_instance = scm_objects.ApplicationsApi(api_client)
    id = '123e4567-e89b-12d3-a456-426655440000' # str | The UUID of the configuration resource

    try:
        # Delete an application
        api_instance.delete_applications_by_id(id)
    except Exception as e:
        print("Exception when calling ApplicationsApi->delete_applications_by_id: %s\n" % e)
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

# **get_applications_by_id**
> Applications get_applications_by_id(id)

Get the application by id

Get an existing application. 

### Example

* Bearer (JWT) Authentication (scmToken):

```python
import scm_objects
from scm_objects.models.applications import Applications
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
    api_instance = scm_objects.ApplicationsApi(api_client)
    id = '123e4567-e89b-12d3-a456-426655440000' # str | The UUID of the configuration resource

    try:
        # Get the application by id
        api_response = api_instance.get_applications_by_id(id)
        print("The response of ApplicationsApi->get_applications_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApplicationsApi->get_applications_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The UUID of the configuration resource | 

### Return type

[**Applications**](Applications.md)

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

# **list_applications**
> ApplicationsListResponse list_applications(name=name, folder=folder, snippet=snippet, device=device, offset=offset, limit=limit)

List applications

Retrieve a list of applications. 

### Example

* Bearer (JWT) Authentication (scmToken):

```python
import scm_objects
from scm_objects.models.applications_list_response import ApplicationsListResponse
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
    api_instance = scm_objects.ApplicationsApi(api_client)
    name = 'name_example' # str | The name of the configuration resource (optional)
    folder = 'folder_example' # str | The folder in which the resource is defined  (optional)
    snippet = 'snippet_example' # str | The snippet in which the resource is defined  (optional)
    device = 'device_example' # str | The device in which the resource is defined  (optional)
    offset = 0 # int | The offset into the list of results returned (optional) (default to 0)
    limit = 200 # int | The maximum number of results per page (optional) (default to 200)

    try:
        # List applications
        api_response = api_instance.list_applications(name=name, folder=folder, snippet=snippet, device=device, offset=offset, limit=limit)
        print("The response of ApplicationsApi->list_applications:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApplicationsApi->list_applications: %s\n" % e)
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

[**ApplicationsListResponse**](ApplicationsListResponse.md)

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

# **update_applications_by_id**
> Applications update_applications_by_id(id, applications=applications)

Update an application

Update an existing application. 

### Example

* Bearer (JWT) Authentication (scmToken):

```python
import scm_objects
from scm_objects.models.applications import Applications
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
    api_instance = scm_objects.ApplicationsApi(api_client)
    id = '123e4567-e89b-12d3-a456-426655440000' # str | The UUID of the configuration resource
    applications = scm_objects.Applications() # Applications | OK (optional)

    try:
        # Update an application
        api_response = api_instance.update_applications_by_id(id, applications=applications)
        print("The response of ApplicationsApi->update_applications_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApplicationsApi->update_applications_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The UUID of the configuration resource | 
 **applications** | [**Applications**](Applications.md)| OK | [optional] 

### Return type

[**Applications**](Applications.md)

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

