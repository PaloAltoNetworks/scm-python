# scm.identity_services.LocalUsersApi

All URIs are relative to *https://api.strata.paloaltonetworks.com/config/identity/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_local_users**](LocalUsersApi.md#create_local_users) | **POST** /local-users | Create a local user
[**delete_local_users_by_id**](LocalUsersApi.md#delete_local_users_by_id) | **DELETE** /local-users/{id} | Delete a local user
[**get_local_users_by_id**](LocalUsersApi.md#get_local_users_by_id) | **GET** /local-users/{id} | Get a local user
[**list_local_users**](LocalUsersApi.md#list_local_users) | **GET** /local-users | List local users
[**update_local_users_by_id**](LocalUsersApi.md#update_local_users_by_id) | **PUT** /local-users/{id} | Update a local user


# **create_local_users**
> LocalUsers create_local_users(local_users=local_users)

Create a local user

Create a new local user. 

### Example

* Bearer (JWT) Authentication (scmToken):

```python
import scm.identity_services
from scm.identity_services.models.local_users import LocalUsers
from scm.identity_services.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.strata.paloaltonetworks.com/config/identity/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = scm.identity_services.Configuration(
    host = "https://api.strata.paloaltonetworks.com/config/identity/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): scmToken
configuration = scm.identity_services.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with scm.identity_services.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = scm.identity_services.LocalUsersApi(api_client)
    local_users = scm.identity_services.LocalUsers() # LocalUsers | Created (optional)

    try:
        # Create a local user
        api_response = api_instance.create_local_users(local_users=local_users)
        print("The response of LocalUsersApi->create_local_users:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LocalUsersApi->create_local_users: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **local_users** | [**LocalUsers**](LocalUsers.md)| Created | [optional] 

### Return type

[**LocalUsers**](LocalUsers.md)

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

# **delete_local_users_by_id**
> delete_local_users_by_id(id)

Delete a local user

Delete a local user. 

### Example

* Bearer (JWT) Authentication (scmToken):

```python
import scm.identity_services
from scm.identity_services.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.strata.paloaltonetworks.com/config/identity/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = scm.identity_services.Configuration(
    host = "https://api.strata.paloaltonetworks.com/config/identity/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): scmToken
configuration = scm.identity_services.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with scm.identity_services.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = scm.identity_services.LocalUsersApi(api_client)
    id = '123e4567-e89b-12d3-a456-426655440000' # str | The UUID of the configuration resource

    try:
        # Delete a local user
        api_instance.delete_local_users_by_id(id)
    except Exception as e:
        print("Exception when calling LocalUsersApi->delete_local_users_by_id: %s\n" % e)
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

# **get_local_users_by_id**
> LocalUsers get_local_users_by_id(id)

Get a local user

Get an existing local user. 

### Example

* Bearer (JWT) Authentication (scmToken):

```python
import scm.identity_services
from scm.identity_services.models.local_users import LocalUsers
from scm.identity_services.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.strata.paloaltonetworks.com/config/identity/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = scm.identity_services.Configuration(
    host = "https://api.strata.paloaltonetworks.com/config/identity/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): scmToken
configuration = scm.identity_services.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with scm.identity_services.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = scm.identity_services.LocalUsersApi(api_client)
    id = '123e4567-e89b-12d3-a456-426655440000' # str | The UUID of the configuration resource

    try:
        # Get a local user
        api_response = api_instance.get_local_users_by_id(id)
        print("The response of LocalUsersApi->get_local_users_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LocalUsersApi->get_local_users_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The UUID of the configuration resource | 

### Return type

[**LocalUsers**](LocalUsers.md)

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

# **list_local_users**
> LocalUsersListResponse list_local_users(name=name, folder=folder, snippet=snippet, device=device, limit=limit, offset=offset)

List local users

Retrieve a list of local users. 

### Example

* Bearer (JWT) Authentication (scmToken):

```python
import scm.identity_services
from scm.identity_services.models.local_users_list_response import LocalUsersListResponse
from scm.identity_services.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.strata.paloaltonetworks.com/config/identity/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = scm.identity_services.Configuration(
    host = "https://api.strata.paloaltonetworks.com/config/identity/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): scmToken
configuration = scm.identity_services.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with scm.identity_services.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = scm.identity_services.LocalUsersApi(api_client)
    name = 'name_example' # str | The name of the configuration resource (optional)
    folder = 'folder_example' # str | The folder in which the resource is defined  (optional)
    snippet = 'snippet_example' # str | The snippet in which the resource is defined  (optional)
    device = 'device_example' # str | The device in which the resource is defined  (optional)
    limit = 200 # int | The maximum number of results per page (optional) (default to 200)
    offset = 0 # int | The offset into the list of results returned (optional) (default to 0)

    try:
        # List local users
        api_response = api_instance.list_local_users(name=name, folder=folder, snippet=snippet, device=device, limit=limit, offset=offset)
        print("The response of LocalUsersApi->list_local_users:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LocalUsersApi->list_local_users: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The name of the configuration resource | [optional] 
 **folder** | **str**| The folder in which the resource is defined  | [optional] 
 **snippet** | **str**| The snippet in which the resource is defined  | [optional] 
 **device** | **str**| The device in which the resource is defined  | [optional] 
 **limit** | **int**| The maximum number of results per page | [optional] [default to 200]
 **offset** | **int**| The offset into the list of results returned | [optional] [default to 0]

### Return type

[**LocalUsersListResponse**](LocalUsersListResponse.md)

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

# **update_local_users_by_id**
> LocalUsers update_local_users_by_id(id, local_users=local_users)

Update a local user

Update an existing local user. 

### Example

* Bearer (JWT) Authentication (scmToken):

```python
import scm.identity_services
from scm.identity_services.models.local_users import LocalUsers
from scm.identity_services.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.strata.paloaltonetworks.com/config/identity/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = scm.identity_services.Configuration(
    host = "https://api.strata.paloaltonetworks.com/config/identity/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): scmToken
configuration = scm.identity_services.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with scm.identity_services.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = scm.identity_services.LocalUsersApi(api_client)
    id = '123e4567-e89b-12d3-a456-426655440000' # str | The UUID of the configuration resource
    local_users = scm.identity_services.LocalUsers() # LocalUsers | OK (optional)

    try:
        # Update a local user
        api_response = api_instance.update_local_users_by_id(id, local_users=local_users)
        print("The response of LocalUsersApi->update_local_users_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LocalUsersApi->update_local_users_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The UUID of the configuration resource | 
 **local_users** | [**LocalUsers**](LocalUsers.md)| OK | [optional] 

### Return type

[**LocalUsers**](LocalUsers.md)

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

