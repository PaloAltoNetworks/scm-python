# scm.network_services.HipmatchMatchListApi

All URIs are relative to *https://api.strata.paloaltonetworks.com/config/network/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_hipmatch_match_list**](HipmatchMatchListApi.md#create_hipmatch_match_list) | **POST** /hipmatch-match-list | Create a hipmatch match list entry
[**delete_hipmatch_match_list_by_id**](HipmatchMatchListApi.md#delete_hipmatch_match_list_by_id) | **DELETE** /hipmatch-match-list/{id} | Delete a hipmatch match list entry
[**get_hipmatch_match_list_by_id**](HipmatchMatchListApi.md#get_hipmatch_match_list_by_id) | **GET** /hipmatch-match-list/{id} | Get a hipmatch match list entry
[**list_hipmatch_match_list**](HipmatchMatchListApi.md#list_hipmatch_match_list) | **GET** /hipmatch-match-list | List hipmatch match list entries
[**update_hipmatch_match_list_by_id**](HipmatchMatchListApi.md#update_hipmatch_match_list_by_id) | **PUT** /hipmatch-match-list/{id} | Update a hipmatch match list entry


# **create_hipmatch_match_list**
> HipmatchMatchList create_hipmatch_match_list(hipmatch_match_list=hipmatch_match_list)

Create a hipmatch match list entry

Create a new hipmatch match list entry. 

### Example

* Bearer (JWT) Authentication (scmToken):

```python
import scm.network_services
from scm.network_services.models.hipmatch_match_list import HipmatchMatchList
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
    api_instance = scm.network_services.HipmatchMatchListApi(api_client)
    hipmatch_match_list = scm.network_services.HipmatchMatchList() # HipmatchMatchList | Created (optional)

    try:
        # Create a hipmatch match list entry
        api_response = api_instance.create_hipmatch_match_list(hipmatch_match_list=hipmatch_match_list)
        print("The response of HipmatchMatchListApi->create_hipmatch_match_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HipmatchMatchListApi->create_hipmatch_match_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **hipmatch_match_list** | [**HipmatchMatchList**](HipmatchMatchList.md)| Created | [optional] 

### Return type

[**HipmatchMatchList**](HipmatchMatchList.md)

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

# **delete_hipmatch_match_list_by_id**
> delete_hipmatch_match_list_by_id(id)

Delete a hipmatch match list entry

Delete a hipmatch match list entry. 

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
    api_instance = scm.network_services.HipmatchMatchListApi(api_client)
    id = '123e4567-e89b-12d3-a456-426655440000' # str | The UUID of the configuration resource

    try:
        # Delete a hipmatch match list entry
        api_instance.delete_hipmatch_match_list_by_id(id)
    except Exception as e:
        print("Exception when calling HipmatchMatchListApi->delete_hipmatch_match_list_by_id: %s\n" % e)
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

# **get_hipmatch_match_list_by_id**
> HipmatchMatchList get_hipmatch_match_list_by_id(id)

Get a hipmatch match list entry

Get an existing hipmatch match list entry. 

### Example

* Bearer (JWT) Authentication (scmToken):

```python
import scm.network_services
from scm.network_services.models.hipmatch_match_list import HipmatchMatchList
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
    api_instance = scm.network_services.HipmatchMatchListApi(api_client)
    id = '123e4567-e89b-12d3-a456-426655440000' # str | The UUID of the configuration resource

    try:
        # Get a hipmatch match list entry
        api_response = api_instance.get_hipmatch_match_list_by_id(id)
        print("The response of HipmatchMatchListApi->get_hipmatch_match_list_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HipmatchMatchListApi->get_hipmatch_match_list_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The UUID of the configuration resource | 

### Return type

[**HipmatchMatchList**](HipmatchMatchList.md)

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

# **list_hipmatch_match_list**
> HipmatchMatchListListResponse list_hipmatch_match_list(name=name, folder=folder, snippet=snippet, device=device, offset=offset, limit=limit)

List hipmatch match list entries

Retrieve a list of hipmatch match list entries. 

### Example

* Bearer (JWT) Authentication (scmToken):

```python
import scm.network_services
from scm.network_services.models.hipmatch_match_list_list_response import HipmatchMatchListListResponse
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
    api_instance = scm.network_services.HipmatchMatchListApi(api_client)
    name = 'name_example' # str | The name of the configuration resource (optional)
    folder = 'folder_example' # str | The folder in which the resource is defined  (optional)
    snippet = 'snippet_example' # str | The snippet in which the resource is defined  (optional)
    device = 'device_example' # str | The device in which the resource is defined  (optional)
    offset = 0 # int | The offset into the list of results returned (optional) (default to 0)
    limit = 200 # int | The maximum number of results per page (optional) (default to 200)

    try:
        # List hipmatch match list entries
        api_response = api_instance.list_hipmatch_match_list(name=name, folder=folder, snippet=snippet, device=device, offset=offset, limit=limit)
        print("The response of HipmatchMatchListApi->list_hipmatch_match_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HipmatchMatchListApi->list_hipmatch_match_list: %s\n" % e)
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

[**HipmatchMatchListListResponse**](HipmatchMatchListListResponse.md)

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

# **update_hipmatch_match_list_by_id**
> HipmatchMatchList update_hipmatch_match_list_by_id(id, hipmatch_match_list=hipmatch_match_list)

Update a hipmatch match list entry

Update an existing hipmatch match list entry. 

### Example

* Bearer (JWT) Authentication (scmToken):

```python
import scm.network_services
from scm.network_services.models.hipmatch_match_list import HipmatchMatchList
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
    api_instance = scm.network_services.HipmatchMatchListApi(api_client)
    id = '123e4567-e89b-12d3-a456-426655440000' # str | The UUID of the configuration resource
    hipmatch_match_list = scm.network_services.HipmatchMatchList() # HipmatchMatchList | OK (optional)

    try:
        # Update a hipmatch match list entry
        api_response = api_instance.update_hipmatch_match_list_by_id(id, hipmatch_match_list=hipmatch_match_list)
        print("The response of HipmatchMatchListApi->update_hipmatch_match_list_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HipmatchMatchListApi->update_hipmatch_match_list_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The UUID of the configuration resource | 
 **hipmatch_match_list** | [**HipmatchMatchList**](HipmatchMatchList.md)| OK | [optional] 

### Return type

[**HipmatchMatchList**](HipmatchMatchList.md)

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

