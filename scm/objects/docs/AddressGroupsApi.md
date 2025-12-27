# scm.objects.AddressGroupsApi

All URIs are relative to *https://api.strata.paloaltonetworks.com/config/objects/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_address_groups**](AddressGroupsApi.md#create_address_groups) | **POST** /address-groups | Create an address group
[**delete_address_groups_by_id**](AddressGroupsApi.md#delete_address_groups_by_id) | **DELETE** /address-groups/{id} | Delete an address group
[**get_address_groups_by_id**](AddressGroupsApi.md#get_address_groups_by_id) | **GET** /address-groups/{id} | Get an address group
[**list_address_groups**](AddressGroupsApi.md#list_address_groups) | **GET** /address-groups | List address groups
[**update_address_groups_by_id**](AddressGroupsApi.md#update_address_groups_by_id) | **PUT** /address-groups/{id} | Update an address group


# **create_address_groups**
> AddressGroups create_address_groups(address_groups=address_groups)

Create an address group

Create a new address group. 

### Example

* Bearer (JWT) Authentication (scmToken):

```python
import scm.objects
from scm.objects.models.address_groups import AddressGroups
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
    api_instance = scm.objects.AddressGroupsApi(api_client)
    address_groups = scm.objects.AddressGroups() # AddressGroups | Created (optional)

    try:
        # Create an address group
        api_response = api_instance.create_address_groups(address_groups=address_groups)
        print("The response of AddressGroupsApi->create_address_groups:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AddressGroupsApi->create_address_groups: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **address_groups** | [**AddressGroups**](AddressGroups.md)| Created | [optional] 

### Return type

[**AddressGroups**](AddressGroups.md)

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

# **delete_address_groups_by_id**
> delete_address_groups_by_id(id)

Delete an address group

Delete an address group. 

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
    api_instance = scm.objects.AddressGroupsApi(api_client)
    id = '123e4567-e89b-12d3-a456-426655440000' # str | The UUID of the configuration resource

    try:
        # Delete an address group
        api_instance.delete_address_groups_by_id(id)
    except Exception as e:
        print("Exception when calling AddressGroupsApi->delete_address_groups_by_id: %s\n" % e)
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

# **get_address_groups_by_id**
> AddressGroups get_address_groups_by_id(id)

Get an address group

Retrieve an existing address group. 

### Example

* Bearer (JWT) Authentication (scmToken):

```python
import scm.objects
from scm.objects.models.address_groups import AddressGroups
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
    api_instance = scm.objects.AddressGroupsApi(api_client)
    id = '123e4567-e89b-12d3-a456-426655440000' # str | The UUID of the configuration resource

    try:
        # Get an address group
        api_response = api_instance.get_address_groups_by_id(id)
        print("The response of AddressGroupsApi->get_address_groups_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AddressGroupsApi->get_address_groups_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The UUID of the configuration resource | 

### Return type

[**AddressGroups**](AddressGroups.md)

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

# **list_address_groups**
> AddressGroupsListResponse list_address_groups(name=name, folder=folder, snippet=snippet, device=device, offset=offset, limit=limit)

List address groups

Retrieve a list of address groups. 

### Example

* Bearer (JWT) Authentication (scmToken):

```python
import scm.objects
from scm.objects.models.address_groups_list_response import AddressGroupsListResponse
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
    api_instance = scm.objects.AddressGroupsApi(api_client)
    name = 'name_example' # str | The name of the configuration resource (optional)
    folder = 'folder_example' # str | The folder in which the resource is defined  (optional)
    snippet = 'snippet_example' # str | The snippet in which the resource is defined  (optional)
    device = 'device_example' # str | The device in which the resource is defined  (optional)
    offset = 0 # int | The offset into the list of results returned (optional) (default to 0)
    limit = 200 # int | The maximum number of results per page (optional) (default to 200)

    try:
        # List address groups
        api_response = api_instance.list_address_groups(name=name, folder=folder, snippet=snippet, device=device, offset=offset, limit=limit)
        print("The response of AddressGroupsApi->list_address_groups:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AddressGroupsApi->list_address_groups: %s\n" % e)
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

[**AddressGroupsListResponse**](AddressGroupsListResponse.md)

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

# **update_address_groups_by_id**
> AddressGroups update_address_groups_by_id(id, address_groups=address_groups)

Update an address group

Update an existing address group. 

### Example

* Bearer (JWT) Authentication (scmToken):

```python
import scm.objects
from scm.objects.models.address_groups import AddressGroups
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
    api_instance = scm.objects.AddressGroupsApi(api_client)
    id = '123e4567-e89b-12d3-a456-426655440000' # str | The UUID of the configuration resource
    address_groups = scm.objects.AddressGroups() # AddressGroups | OK (optional)

    try:
        # Update an address group
        api_response = api_instance.update_address_groups_by_id(id, address_groups=address_groups)
        print("The response of AddressGroupsApi->update_address_groups_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AddressGroupsApi->update_address_groups_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The UUID of the configuration resource | 
 **address_groups** | [**AddressGroups**](AddressGroups.md)| OK | [optional] 

### Return type

[**AddressGroups**](AddressGroups.md)

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

