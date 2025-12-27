# scm.config_setup.FoldersApi

All URIs are relative to *https://api.strata.paloaltonetworks.com/config/setup/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_folder**](FoldersApi.md#create_folder) | **POST** /folders | Create a folder
[**delete_folder_by_id**](FoldersApi.md#delete_folder_by_id) | **DELETE** /folders/{id} | Delete a folder
[**get_folder_by_id**](FoldersApi.md#get_folder_by_id) | **GET** /folders/{id} | Get a folder
[**list_folders**](FoldersApi.md#list_folders) | **GET** /folders | List folders
[**update_folder_by_id**](FoldersApi.md#update_folder_by_id) | **PUT** /folders/{id} | Update a folder


# **create_folder**
> Folders create_folder(folders=folders)

Create a folder

Create a new folder. 

### Example

* Bearer (JWT) Authentication (scmToken):

```python
import scm.config_setup
from scm.config_setup.models.folders import Folders
from scm.config_setup.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.strata.paloaltonetworks.com/config/setup/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = scm.config_setup.Configuration(
    host = "https://api.strata.paloaltonetworks.com/config/setup/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): scmToken
configuration = scm.config_setup.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with scm.config_setup.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = scm.config_setup.FoldersApi(api_client)
    folders = scm.config_setup.Folders() # Folders | The `folder` resource definition (optional)

    try:
        # Create a folder
        api_response = api_instance.create_folder(folders=folders)
        print("The response of FoldersApi->create_folder:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FoldersApi->create_folder: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **folders** | [**Folders**](Folders.md)| The &#x60;folder&#x60; resource definition | [optional] 

### Return type

[**Folders**](Folders.md)

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

# **delete_folder_by_id**
> delete_folder_by_id(id)

Delete a folder

Delete an existing folder. 

### Example

* Bearer (JWT) Authentication (scmToken):

```python
import scm.config_setup
from scm.config_setup.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.strata.paloaltonetworks.com/config/setup/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = scm.config_setup.Configuration(
    host = "https://api.strata.paloaltonetworks.com/config/setup/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): scmToken
configuration = scm.config_setup.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with scm.config_setup.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = scm.config_setup.FoldersApi(api_client)
    id = 'id_example' # str | The UUID of the resource

    try:
        # Delete a folder
        api_instance.delete_folder_by_id(id)
    except Exception as e:
        print("Exception when calling FoldersApi->delete_folder_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The UUID of the resource | 

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

# **get_folder_by_id**
> Folders get_folder_by_id(id)

Get a folder

Retrieve an existing folder. 

### Example

* Bearer (JWT) Authentication (scmToken):

```python
import scm.config_setup
from scm.config_setup.models.folders import Folders
from scm.config_setup.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.strata.paloaltonetworks.com/config/setup/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = scm.config_setup.Configuration(
    host = "https://api.strata.paloaltonetworks.com/config/setup/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): scmToken
configuration = scm.config_setup.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with scm.config_setup.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = scm.config_setup.FoldersApi(api_client)
    id = 'id_example' # str | The UUID of the resource

    try:
        # Get a folder
        api_response = api_instance.get_folder_by_id(id)
        print("The response of FoldersApi->get_folder_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FoldersApi->get_folder_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The UUID of the resource | 

### Return type

[**Folders**](Folders.md)

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

# **list_folders**
> FoldersListResponse list_folders(limit=limit, offset=offset, name=name)

List folders

Retrieve a list of folders. 

### Example

* Bearer (JWT) Authentication (scmToken):

```python
import scm.config_setup
from scm.config_setup.models.folders_list_response import FoldersListResponse
from scm.config_setup.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.strata.paloaltonetworks.com/config/setup/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = scm.config_setup.Configuration(
    host = "https://api.strata.paloaltonetworks.com/config/setup/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): scmToken
configuration = scm.config_setup.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with scm.config_setup.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = scm.config_setup.FoldersApi(api_client)
    limit = 56 # int | The maximum number of resources to return (optional)
    offset = 56 # int | The offset into the list of resources returned (optional)
    name = 'name_example' # str | The name of the resource (optional)

    try:
        # List folders
        api_response = api_instance.list_folders(limit=limit, offset=offset, name=name)
        print("The response of FoldersApi->list_folders:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FoldersApi->list_folders: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| The maximum number of resources to return | [optional] 
 **offset** | **int**| The offset into the list of resources returned | [optional] 
 **name** | **str**| The name of the resource | [optional] 

### Return type

[**FoldersListResponse**](FoldersListResponse.md)

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

# **update_folder_by_id**
> Folders update_folder_by_id(id, folders=folders)

Update a folder

Update an existing folder. 

### Example

* Bearer (JWT) Authentication (scmToken):

```python
import scm.config_setup
from scm.config_setup.models.folders import Folders
from scm.config_setup.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.strata.paloaltonetworks.com/config/setup/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = scm.config_setup.Configuration(
    host = "https://api.strata.paloaltonetworks.com/config/setup/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): scmToken
configuration = scm.config_setup.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with scm.config_setup.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = scm.config_setup.FoldersApi(api_client)
    id = 'id_example' # str | The UUID of the resource
    folders = scm.config_setup.Folders() # Folders | The `folder` resource definition. (optional)

    try:
        # Update a folder
        api_response = api_instance.update_folder_by_id(id, folders=folders)
        print("The response of FoldersApi->update_folder_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FoldersApi->update_folder_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The UUID of the resource | 
 **folders** | [**Folders**](Folders.md)| The &#x60;folder&#x60; resource definition. | [optional] 

### Return type

[**Folders**](Folders.md)

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

