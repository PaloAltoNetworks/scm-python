# scm_objects.AddressesApi

All URIs are relative to *https://api.strata.paloaltonetworks.com/config/objects/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_addresses**](AddressesApi.md#create_addresses) | **POST** /addresses | Create an address
[**delete_addresses_by_id**](AddressesApi.md#delete_addresses_by_id) | **DELETE** /addresses/{id} | Delete an address
[**get_addresses_by_id**](AddressesApi.md#get_addresses_by_id) | **GET** /addresses/{id} | Get an address
[**list_addresses**](AddressesApi.md#list_addresses) | **GET** /addresses | List addresses
[**update_addresses_by_id**](AddressesApi.md#update_addresses_by_id) | **PUT** /addresses/{id} | Update an address


# **create_addresses**
> Addresses create_addresses(addresses=addresses)

Create an address

Create a new address. 

### Example

* Bearer (JWT) Authentication (scmToken):

```python
import scm_objects
from scm_objects.models.addresses import Addresses
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
    api_instance = scm_objects.AddressesApi(api_client)
    addresses = scm_objects.Addresses() # Addresses | Created (optional)

    try:
        # Create an address
        api_response = api_instance.create_addresses(addresses=addresses)
        print("The response of AddressesApi->create_addresses:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AddressesApi->create_addresses: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **addresses** | [**Addresses**](Addresses.md)| Created | [optional] 

### Return type

[**Addresses**](Addresses.md)

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

# **delete_addresses_by_id**
> delete_addresses_by_id(id)

Delete an address

Delete an address. 

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
    api_instance = scm_objects.AddressesApi(api_client)
    id = '123e4567-e89b-12d3-a456-426655440000' # str | The UUID of the configuration resource

    try:
        # Delete an address
        api_instance.delete_addresses_by_id(id)
    except Exception as e:
        print("Exception when calling AddressesApi->delete_addresses_by_id: %s\n" % e)
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

# **get_addresses_by_id**
> Addresses get_addresses_by_id(id)

Get an address

Retrieve an existing address. 

### Example

* Bearer (JWT) Authentication (scmToken):

```python
import scm_objects
from scm_objects.models.addresses import Addresses
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
    api_instance = scm_objects.AddressesApi(api_client)
    id = '123e4567-e89b-12d3-a456-426655440000' # str | The UUID of the configuration resource

    try:
        # Get an address
        api_response = api_instance.get_addresses_by_id(id)
        print("The response of AddressesApi->get_addresses_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AddressesApi->get_addresses_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The UUID of the configuration resource | 

### Return type

[**Addresses**](Addresses.md)

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

# **list_addresses**
> AddressesListResponse list_addresses(name=name, folder=folder, snippet=snippet, device=device, offset=offset, limit=limit)

List addresses

Retrieve a list of addresses. 

### Example

* Bearer (JWT) Authentication (scmToken):

```python
import scm_objects
from scm_objects.models.addresses_list_response import AddressesListResponse
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
    api_instance = scm_objects.AddressesApi(api_client)
    name = 'name_example' # str | The name of the configuration resource (optional)
    folder = 'folder_example' # str | The folder in which the resource is defined  (optional)
    snippet = 'snippet_example' # str | The snippet in which the resource is defined  (optional)
    device = 'device_example' # str | The device in which the resource is defined  (optional)
    offset = 0 # int | The offset into the list of results returned (optional) (default to 0)
    limit = 200 # int | The maximum number of results per page (optional) (default to 200)

    try:
        # List addresses
        api_response = api_instance.list_addresses(name=name, folder=folder, snippet=snippet, device=device, offset=offset, limit=limit)
        print("The response of AddressesApi->list_addresses:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AddressesApi->list_addresses: %s\n" % e)
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

[**AddressesListResponse**](AddressesListResponse.md)

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

# **update_addresses_by_id**
> Addresses update_addresses_by_id(id, addresses=addresses)

Update an address

Update an existing address. 

### Example

* Bearer (JWT) Authentication (scmToken):

```python
import scm_objects
from scm_objects.models.addresses import Addresses
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
    api_instance = scm_objects.AddressesApi(api_client)
    id = '123e4567-e89b-12d3-a456-426655440000' # str | The UUID of the configuration resource
    addresses = scm_objects.Addresses() # Addresses | OK (optional)

    try:
        # Update an address
        api_response = api_instance.update_addresses_by_id(id, addresses=addresses)
        print("The response of AddressesApi->update_addresses_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AddressesApi->update_addresses_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The UUID of the configuration resource | 
 **addresses** | [**Addresses**](Addresses.md)| OK | [optional] 

### Return type

[**Addresses**](Addresses.md)

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

