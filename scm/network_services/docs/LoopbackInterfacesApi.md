# scm_network_services.LoopbackInterfacesApi

All URIs are relative to *https://api.strata.paloaltonetworks.com/config/network/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_loopback_interfaces**](LoopbackInterfacesApi.md#create_loopback_interfaces) | **POST** /loopback-interfaces | Create a loopback interface
[**delete_loopback_interfaces_by_id**](LoopbackInterfacesApi.md#delete_loopback_interfaces_by_id) | **DELETE** /loopback-interfaces/{id} | Delete a loopback interface
[**get_loopback_interfaces_by_id**](LoopbackInterfacesApi.md#get_loopback_interfaces_by_id) | **GET** /loopback-interfaces/{id} | Get a loopback interface
[**list_loopback_interfaces**](LoopbackInterfacesApi.md#list_loopback_interfaces) | **GET** /loopback-interfaces | List loopback interfaces
[**update_loopback_interfaces_by_id**](LoopbackInterfacesApi.md#update_loopback_interfaces_by_id) | **PUT** /loopback-interfaces/{id} | Update a loopback interface


# **create_loopback_interfaces**
> LoopbackInterfaces create_loopback_interfaces(loopback_interfaces=loopback_interfaces)

Create a loopback interface

Create a new loopback interface. 

### Example

* Bearer (JWT) Authentication (scmToken):

```python
import scm_network_services
from scm_network_services.models.loopback_interfaces import LoopbackInterfaces
from scm_network_services.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.strata.paloaltonetworks.com/config/network/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = scm_network_services.Configuration(
    host = "https://api.strata.paloaltonetworks.com/config/network/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): scmToken
configuration = scm_network_services.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with scm_network_services.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = scm_network_services.LoopbackInterfacesApi(api_client)
    loopback_interfaces = scm_network_services.LoopbackInterfaces() # LoopbackInterfaces | Created (optional)

    try:
        # Create a loopback interface
        api_response = api_instance.create_loopback_interfaces(loopback_interfaces=loopback_interfaces)
        print("The response of LoopbackInterfacesApi->create_loopback_interfaces:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LoopbackInterfacesApi->create_loopback_interfaces: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **loopback_interfaces** | [**LoopbackInterfaces**](LoopbackInterfaces.md)| Created | [optional] 

### Return type

[**LoopbackInterfaces**](LoopbackInterfaces.md)

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

# **delete_loopback_interfaces_by_id**
> delete_loopback_interfaces_by_id(id)

Delete a loopback interface

Delete a loopback interface. 

### Example

* Bearer (JWT) Authentication (scmToken):

```python
import scm_network_services
from scm_network_services.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.strata.paloaltonetworks.com/config/network/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = scm_network_services.Configuration(
    host = "https://api.strata.paloaltonetworks.com/config/network/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): scmToken
configuration = scm_network_services.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with scm_network_services.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = scm_network_services.LoopbackInterfacesApi(api_client)
    id = '123e4567-e89b-12d3-a456-426655440000' # str | The UUID of the configuration resource

    try:
        # Delete a loopback interface
        api_instance.delete_loopback_interfaces_by_id(id)
    except Exception as e:
        print("Exception when calling LoopbackInterfacesApi->delete_loopback_interfaces_by_id: %s\n" % e)
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

# **get_loopback_interfaces_by_id**
> LoopbackInterfaces get_loopback_interfaces_by_id(id)

Get a loopback interface

Get an existing loopback interface. 

### Example

* Bearer (JWT) Authentication (scmToken):

```python
import scm_network_services
from scm_network_services.models.loopback_interfaces import LoopbackInterfaces
from scm_network_services.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.strata.paloaltonetworks.com/config/network/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = scm_network_services.Configuration(
    host = "https://api.strata.paloaltonetworks.com/config/network/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): scmToken
configuration = scm_network_services.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with scm_network_services.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = scm_network_services.LoopbackInterfacesApi(api_client)
    id = '123e4567-e89b-12d3-a456-426655440000' # str | The UUID of the configuration resource

    try:
        # Get a loopback interface
        api_response = api_instance.get_loopback_interfaces_by_id(id)
        print("The response of LoopbackInterfacesApi->get_loopback_interfaces_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LoopbackInterfacesApi->get_loopback_interfaces_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The UUID of the configuration resource | 

### Return type

[**LoopbackInterfaces**](LoopbackInterfaces.md)

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

# **list_loopback_interfaces**
> LoopbackInterfacesListResponse list_loopback_interfaces(limit=limit, offset=offset, name=name, folder=folder, snippet=snippet, device=device)

List loopback interfaces

Retrieve a list of loopback interfaces. 

### Example

* Bearer (JWT) Authentication (scmToken):

```python
import scm_network_services
from scm_network_services.models.loopback_interfaces_list_response import LoopbackInterfacesListResponse
from scm_network_services.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.strata.paloaltonetworks.com/config/network/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = scm_network_services.Configuration(
    host = "https://api.strata.paloaltonetworks.com/config/network/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): scmToken
configuration = scm_network_services.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with scm_network_services.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = scm_network_services.LoopbackInterfacesApi(api_client)
    limit = 200 # int | The maximum number of results per page (optional) (default to 200)
    offset = 0 # int | The offset into the list of results returned (optional) (default to 0)
    name = 'name_example' # str | The name of the configuration resource (optional)
    folder = 'folder_example' # str | The folder in which the resource is defined  (optional)
    snippet = 'snippet_example' # str | The snippet in which the resource is defined  (optional)
    device = 'device_example' # str | The device in which the resource is defined  (optional)

    try:
        # List loopback interfaces
        api_response = api_instance.list_loopback_interfaces(limit=limit, offset=offset, name=name, folder=folder, snippet=snippet, device=device)
        print("The response of LoopbackInterfacesApi->list_loopback_interfaces:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LoopbackInterfacesApi->list_loopback_interfaces: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| The maximum number of results per page | [optional] [default to 200]
 **offset** | **int**| The offset into the list of results returned | [optional] [default to 0]
 **name** | **str**| The name of the configuration resource | [optional] 
 **folder** | **str**| The folder in which the resource is defined  | [optional] 
 **snippet** | **str**| The snippet in which the resource is defined  | [optional] 
 **device** | **str**| The device in which the resource is defined  | [optional] 

### Return type

[**LoopbackInterfacesListResponse**](LoopbackInterfacesListResponse.md)

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

# **update_loopback_interfaces_by_id**
> LoopbackInterfaces update_loopback_interfaces_by_id(id, loopback_interfaces=loopback_interfaces)

Update a loopback interface

Update an existing loopback interface. 

### Example

* Bearer (JWT) Authentication (scmToken):

```python
import scm_network_services
from scm_network_services.models.loopback_interfaces import LoopbackInterfaces
from scm_network_services.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.strata.paloaltonetworks.com/config/network/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = scm_network_services.Configuration(
    host = "https://api.strata.paloaltonetworks.com/config/network/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): scmToken
configuration = scm_network_services.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with scm_network_services.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = scm_network_services.LoopbackInterfacesApi(api_client)
    id = '123e4567-e89b-12d3-a456-426655440000' # str | The UUID of the configuration resource
    loopback_interfaces = scm_network_services.LoopbackInterfaces() # LoopbackInterfaces | OK (optional)

    try:
        # Update a loopback interface
        api_response = api_instance.update_loopback_interfaces_by_id(id, loopback_interfaces=loopback_interfaces)
        print("The response of LoopbackInterfacesApi->update_loopback_interfaces_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LoopbackInterfacesApi->update_loopback_interfaces_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The UUID of the configuration resource | 
 **loopback_interfaces** | [**LoopbackInterfaces**](LoopbackInterfaces.md)| OK | [optional] 

### Return type

[**LoopbackInterfaces**](LoopbackInterfaces.md)

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

