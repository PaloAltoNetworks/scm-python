# scm_objects.HIPObjectsApi

All URIs are relative to *https://api.strata.paloaltonetworks.com/config/objects/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_hip_objects**](HIPObjectsApi.md#create_hip_objects) | **POST** /hip-objects | Create a HIP object
[**delete_hip_objects_by_id**](HIPObjectsApi.md#delete_hip_objects_by_id) | **DELETE** /hip-objects/{id} | Delete a HIP object
[**get_hip_objects_by_id**](HIPObjectsApi.md#get_hip_objects_by_id) | **GET** /hip-objects/{id} | Get a HIP object
[**list_hip_objects**](HIPObjectsApi.md#list_hip_objects) | **GET** /hip-objects | List HIP objects
[**update_hip_objects_by_id**](HIPObjectsApi.md#update_hip_objects_by_id) | **PUT** /hip-objects/{id} | Update a HIP object


# **create_hip_objects**
> HipObjects create_hip_objects(hip_objects=hip_objects)

Create a HIP object

Create a new HIP object. 

### Example

* Bearer (JWT) Authentication (scmToken):

```python
import scm_objects
from scm_objects.models.hip_objects import HipObjects
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
    api_instance = scm_objects.HIPObjectsApi(api_client)
    hip_objects = scm_objects.HipObjects() # HipObjects | Created (optional)

    try:
        # Create a HIP object
        api_response = api_instance.create_hip_objects(hip_objects=hip_objects)
        print("The response of HIPObjectsApi->create_hip_objects:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HIPObjectsApi->create_hip_objects: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **hip_objects** | [**HipObjects**](HipObjects.md)| Created | [optional] 

### Return type

[**HipObjects**](HipObjects.md)

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

# **delete_hip_objects_by_id**
> delete_hip_objects_by_id(id)

Delete a HIP object

Delete a HIP object. 

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
    api_instance = scm_objects.HIPObjectsApi(api_client)
    id = '123e4567-e89b-12d3-a456-426655440000' # str | The UUID of the configuration resource

    try:
        # Delete a HIP object
        api_instance.delete_hip_objects_by_id(id)
    except Exception as e:
        print("Exception when calling HIPObjectsApi->delete_hip_objects_by_id: %s\n" % e)
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

# **get_hip_objects_by_id**
> HipObjects get_hip_objects_by_id(id)

Get a HIP object

Get an existing HIP object. 

### Example

* Bearer (JWT) Authentication (scmToken):

```python
import scm_objects
from scm_objects.models.hip_objects import HipObjects
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
    api_instance = scm_objects.HIPObjectsApi(api_client)
    id = '123e4567-e89b-12d3-a456-426655440000' # str | The UUID of the configuration resource

    try:
        # Get a HIP object
        api_response = api_instance.get_hip_objects_by_id(id)
        print("The response of HIPObjectsApi->get_hip_objects_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HIPObjectsApi->get_hip_objects_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The UUID of the configuration resource | 

### Return type

[**HipObjects**](HipObjects.md)

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

# **list_hip_objects**
> HIPObjectsListResponse list_hip_objects(name=name, folder=folder, snippet=snippet, device=device, offset=offset, limit=limit)

List HIP objects

Retrieve a list HIP objects. 

### Example

* Bearer (JWT) Authentication (scmToken):

```python
import scm_objects
from scm_objects.models.hip_objects_list_response import HIPObjectsListResponse
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
    api_instance = scm_objects.HIPObjectsApi(api_client)
    name = 'name_example' # str | The name of the configuration resource (optional)
    folder = 'folder_example' # str | The folder in which the resource is defined  (optional)
    snippet = 'snippet_example' # str | The snippet in which the resource is defined  (optional)
    device = 'device_example' # str | The device in which the resource is defined  (optional)
    offset = 0 # int | The offset into the list of results returned (optional) (default to 0)
    limit = 200 # int | The maximum number of results per page (optional) (default to 200)

    try:
        # List HIP objects
        api_response = api_instance.list_hip_objects(name=name, folder=folder, snippet=snippet, device=device, offset=offset, limit=limit)
        print("The response of HIPObjectsApi->list_hip_objects:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HIPObjectsApi->list_hip_objects: %s\n" % e)
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

[**HIPObjectsListResponse**](HIPObjectsListResponse.md)

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

# **update_hip_objects_by_id**
> HipObjects update_hip_objects_by_id(id, hip_objects=hip_objects)

Update a HIP object

Update an existing HIP object. 

### Example

* Bearer (JWT) Authentication (scmToken):

```python
import scm_objects
from scm_objects.models.hip_objects import HipObjects
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
    api_instance = scm_objects.HIPObjectsApi(api_client)
    id = '123e4567-e89b-12d3-a456-426655440000' # str | The UUID of the configuration resource
    hip_objects = scm_objects.HipObjects() # HipObjects | OK (optional)

    try:
        # Update a HIP object
        api_response = api_instance.update_hip_objects_by_id(id, hip_objects=hip_objects)
        print("The response of HIPObjectsApi->update_hip_objects_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HIPObjectsApi->update_hip_objects_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The UUID of the configuration resource | 
 **hip_objects** | [**HipObjects**](HipObjects.md)| OK | [optional] 

### Return type

[**HipObjects**](HipObjects.md)

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

