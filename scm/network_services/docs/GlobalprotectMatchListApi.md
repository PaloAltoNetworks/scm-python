# scm.network_services.GlobalprotectMatchListApi

All URIs are relative to *https://api.strata.paloaltonetworks.com/config/network/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_globalprotect_match_list**](GlobalprotectMatchListApi.md#create_globalprotect_match_list) | **POST** /globalprotect-match-list | Create a globalprotect match list entry
[**delete_globalprotect_match_list_by_id**](GlobalprotectMatchListApi.md#delete_globalprotect_match_list_by_id) | **DELETE** /globalprotect-match-list/{id} | Delete a globalprotect match list entry
[**get_globalprotect_match_list_by_id**](GlobalprotectMatchListApi.md#get_globalprotect_match_list_by_id) | **GET** /globalprotect-match-list/{id} | Get a globalprotect match list entry
[**list_globalprotect_match_list**](GlobalprotectMatchListApi.md#list_globalprotect_match_list) | **GET** /globalprotect-match-list | List globalprotect match list entries
[**update_globalprotect_match_list_by_id**](GlobalprotectMatchListApi.md#update_globalprotect_match_list_by_id) | **PUT** /globalprotect-match-list/{id} | Update a globalprotect match list entry


# **create_globalprotect_match_list**
> GlobalprotectMatchList create_globalprotect_match_list(globalprotect_match_list=globalprotect_match_list)

Create a globalprotect match list entry

Create a new globalprotect match list entry. 

### Example

* Bearer (JWT) Authentication (scmToken):

```python
import scm.network_services
from scm.network_services.models.globalprotect_match_list import GlobalprotectMatchList
from scm.network_services.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.strata.paloaltonetworks.com/config/network/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = scm.network_services.Configuration(
    host = "https://api.strata.paloaltonetworks.com/config/network/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): scmToken
configuration = scm.network_services.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with scm.network_services.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = scm.network_services.GlobalprotectMatchListApi(api_client)
    globalprotect_match_list = scm.network_services.GlobalprotectMatchList() # GlobalprotectMatchList | Created (optional)

    try:
        # Create a globalprotect match list entry
        api_response = api_instance.create_globalprotect_match_list(globalprotect_match_list=globalprotect_match_list)
        print("The response of GlobalprotectMatchListApi->create_globalprotect_match_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GlobalprotectMatchListApi->create_globalprotect_match_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **globalprotect_match_list** | [**GlobalprotectMatchList**](GlobalprotectMatchList.md)| Created | [optional] 

### Return type

[**GlobalprotectMatchList**](GlobalprotectMatchList.md)

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

# **delete_globalprotect_match_list_by_id**
> delete_globalprotect_match_list_by_id(id)

Delete a globalprotect match list entry

Delete a globalprotect match list entry. 

### Example

* Bearer (JWT) Authentication (scmToken):

```python
import scm.network_services
from scm.network_services.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.strata.paloaltonetworks.com/config/network/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = scm.network_services.Configuration(
    host = "https://api.strata.paloaltonetworks.com/config/network/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): scmToken
configuration = scm.network_services.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with scm.network_services.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = scm.network_services.GlobalprotectMatchListApi(api_client)
    id = '123e4567-e89b-12d3-a456-426655440000' # str | The UUID of the configuration resource

    try:
        # Delete a globalprotect match list entry
        api_instance.delete_globalprotect_match_list_by_id(id)
    except Exception as e:
        print("Exception when calling GlobalprotectMatchListApi->delete_globalprotect_match_list_by_id: %s\n" % e)
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

# **get_globalprotect_match_list_by_id**
> GlobalprotectMatchList get_globalprotect_match_list_by_id(id)

Get a globalprotect match list entry

Get an existing globalprotect match list entry. 

### Example

* Bearer (JWT) Authentication (scmToken):

```python
import scm.network_services
from scm.network_services.models.globalprotect_match_list import GlobalprotectMatchList
from scm.network_services.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.strata.paloaltonetworks.com/config/network/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = scm.network_services.Configuration(
    host = "https://api.strata.paloaltonetworks.com/config/network/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): scmToken
configuration = scm.network_services.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with scm.network_services.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = scm.network_services.GlobalprotectMatchListApi(api_client)
    id = '123e4567-e89b-12d3-a456-426655440000' # str | The UUID of the configuration resource

    try:
        # Get a globalprotect match list entry
        api_response = api_instance.get_globalprotect_match_list_by_id(id)
        print("The response of GlobalprotectMatchListApi->get_globalprotect_match_list_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GlobalprotectMatchListApi->get_globalprotect_match_list_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The UUID of the configuration resource | 

### Return type

[**GlobalprotectMatchList**](GlobalprotectMatchList.md)

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

# **list_globalprotect_match_list**
> GlobalprotectMatchListListResponse list_globalprotect_match_list(name=name, folder=folder, snippet=snippet, device=device, offset=offset, limit=limit)

List globalprotect match list entries

Retrieve a list of globalprotect match list entries. 

### Example

* Bearer (JWT) Authentication (scmToken):

```python
import scm.network_services
from scm.network_services.models.globalprotect_match_list_list_response import GlobalprotectMatchListListResponse
from scm.network_services.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.strata.paloaltonetworks.com/config/network/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = scm.network_services.Configuration(
    host = "https://api.strata.paloaltonetworks.com/config/network/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): scmToken
configuration = scm.network_services.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with scm.network_services.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = scm.network_services.GlobalprotectMatchListApi(api_client)
    name = 'name_example' # str | The name of the configuration resource (optional)
    folder = 'folder_example' # str | The folder in which the resource is defined  (optional)
    snippet = 'snippet_example' # str | The snippet in which the resource is defined  (optional)
    device = 'device_example' # str | The device in which the resource is defined  (optional)
    offset = 0 # int | The offset into the list of results returned (optional) (default to 0)
    limit = 200 # int | The maximum number of results per page (optional) (default to 200)

    try:
        # List globalprotect match list entries
        api_response = api_instance.list_globalprotect_match_list(name=name, folder=folder, snippet=snippet, device=device, offset=offset, limit=limit)
        print("The response of GlobalprotectMatchListApi->list_globalprotect_match_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GlobalprotectMatchListApi->list_globalprotect_match_list: %s\n" % e)
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

[**GlobalprotectMatchListListResponse**](GlobalprotectMatchListListResponse.md)

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

# **update_globalprotect_match_list_by_id**
> GlobalprotectMatchList update_globalprotect_match_list_by_id(id, globalprotect_match_list=globalprotect_match_list)

Update a globalprotect match list entry

Update an existing globalprotect match list entry. 

### Example

* Bearer (JWT) Authentication (scmToken):

```python
import scm.network_services
from scm.network_services.models.globalprotect_match_list import GlobalprotectMatchList
from scm.network_services.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.strata.paloaltonetworks.com/config/network/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = scm.network_services.Configuration(
    host = "https://api.strata.paloaltonetworks.com/config/network/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): scmToken
configuration = scm.network_services.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with scm.network_services.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = scm.network_services.GlobalprotectMatchListApi(api_client)
    id = '123e4567-e89b-12d3-a456-426655440000' # str | The UUID of the configuration resource
    globalprotect_match_list = scm.network_services.GlobalprotectMatchList() # GlobalprotectMatchList | OK (optional)

    try:
        # Update a globalprotect match list entry
        api_response = api_instance.update_globalprotect_match_list_by_id(id, globalprotect_match_list=globalprotect_match_list)
        print("The response of GlobalprotectMatchListApi->update_globalprotect_match_list_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GlobalprotectMatchListApi->update_globalprotect_match_list_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The UUID of the configuration resource | 
 **globalprotect_match_list** | [**GlobalprotectMatchList**](GlobalprotectMatchList.md)| OK | [optional] 

### Return type

[**GlobalprotectMatchList**](GlobalprotectMatchList.md)

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

