# scm_objects.ApplicationGroupsApi

All URIs are relative to *https://api.strata.paloaltonetworks.com/config/objects/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_application_groups**](ApplicationGroupsApi.md#create_application_groups) | **POST** /application-groups | Create an application group
[**delete_application_groups_by_id**](ApplicationGroupsApi.md#delete_application_groups_by_id) | **DELETE** /application-groups/{id} | Delete an application group
[**get_application_groups_by_id**](ApplicationGroupsApi.md#get_application_groups_by_id) | **GET** /application-groups/{id} | Get an application group
[**list_application_groups**](ApplicationGroupsApi.md#list_application_groups) | **GET** /application-groups | List application groups
[**update_application_groups_by_id**](ApplicationGroupsApi.md#update_application_groups_by_id) | **PUT** /application-groups/{id} | Update an application group


# **create_application_groups**
> ApplicationGroups create_application_groups(application_groups=application_groups)

Create an application group

Create a new application group. 

### Example

* Bearer (JWT) Authentication (scmToken):

```python
import scm_objects
from scm_objects.models.application_groups import ApplicationGroups
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
    api_instance = scm_objects.ApplicationGroupsApi(api_client)
    application_groups = scm_objects.ApplicationGroups() # ApplicationGroups | Created (optional)

    try:
        # Create an application group
        api_response = api_instance.create_application_groups(application_groups=application_groups)
        print("The response of ApplicationGroupsApi->create_application_groups:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApplicationGroupsApi->create_application_groups: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_groups** | [**ApplicationGroups**](ApplicationGroups.md)| Created | [optional] 

### Return type

[**ApplicationGroups**](ApplicationGroups.md)

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
**409** | Conflict |  -  |
**0** | General Errors |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_application_groups_by_id**
> delete_application_groups_by_id(id)

Delete an application group

Delete an application group. 

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
    api_instance = scm_objects.ApplicationGroupsApi(api_client)
    id = '123e4567-e89b-12d3-a456-426655440000' # str | The UUID of the configuration resource

    try:
        # Delete an application group
        api_instance.delete_application_groups_by_id(id)
    except Exception as e:
        print("Exception when calling ApplicationGroupsApi->delete_application_groups_by_id: %s\n" % e)
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

# **get_application_groups_by_id**
> ApplicationGroups get_application_groups_by_id(id)

Get an application group

Get an existing application group. 

### Example

* Bearer (JWT) Authentication (scmToken):

```python
import scm_objects
from scm_objects.models.application_groups import ApplicationGroups
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
    api_instance = scm_objects.ApplicationGroupsApi(api_client)
    id = '123e4567-e89b-12d3-a456-426655440000' # str | The UUID of the configuration resource

    try:
        # Get an application group
        api_response = api_instance.get_application_groups_by_id(id)
        print("The response of ApplicationGroupsApi->get_application_groups_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApplicationGroupsApi->get_application_groups_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The UUID of the configuration resource | 

### Return type

[**ApplicationGroups**](ApplicationGroups.md)

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

# **list_application_groups**
> ApplicationGroupsListResponse list_application_groups(name=name, folder=folder, snippet=snippet, device=device, offset=offset, limit=limit)

List application groups

Retrieve a list of application groups. 

### Example

* Bearer (JWT) Authentication (scmToken):

```python
import scm_objects
from scm_objects.models.application_groups_list_response import ApplicationGroupsListResponse
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
    api_instance = scm_objects.ApplicationGroupsApi(api_client)
    name = 'name_example' # str | The name of the configuration resource (optional)
    folder = 'folder_example' # str | The folder in which the resource is defined  (optional)
    snippet = 'snippet_example' # str | The snippet in which the resource is defined  (optional)
    device = 'device_example' # str | The device in which the resource is defined  (optional)
    offset = 0 # int | The offset into the list of results returned (optional) (default to 0)
    limit = 200 # int | The maximum number of results per page (optional) (default to 200)

    try:
        # List application groups
        api_response = api_instance.list_application_groups(name=name, folder=folder, snippet=snippet, device=device, offset=offset, limit=limit)
        print("The response of ApplicationGroupsApi->list_application_groups:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApplicationGroupsApi->list_application_groups: %s\n" % e)
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

[**ApplicationGroupsListResponse**](ApplicationGroupsListResponse.md)

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

# **update_application_groups_by_id**
> ApplicationGroups update_application_groups_by_id(id, application_groups=application_groups)

Update an application group

Update an existing application group. 

### Example

* Bearer (JWT) Authentication (scmToken):

```python
import scm_objects
from scm_objects.models.application_groups import ApplicationGroups
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
    api_instance = scm_objects.ApplicationGroupsApi(api_client)
    id = '123e4567-e89b-12d3-a456-426655440000' # str | The UUID of the configuration resource
    application_groups = scm_objects.ApplicationGroups() # ApplicationGroups | OK (optional)

    try:
        # Update an application group
        api_response = api_instance.update_application_groups_by_id(id, application_groups=application_groups)
        print("The response of ApplicationGroupsApi->update_application_groups_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApplicationGroupsApi->update_application_groups_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The UUID of the configuration resource | 
 **application_groups** | [**ApplicationGroups**](ApplicationGroups.md)| OK | [optional] 

### Return type

[**ApplicationGroups**](ApplicationGroups.md)

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

