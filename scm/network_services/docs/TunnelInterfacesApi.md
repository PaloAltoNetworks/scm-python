# scm.network_services.TunnelInterfacesApi

All URIs are relative to *https://api.strata.paloaltonetworks.com/config/network/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_tunnel_interfaces**](TunnelInterfacesApi.md#create_tunnel_interfaces) | **POST** /tunnel-interfaces | Create a tunnel interface
[**delete_tunnel_interfaces_by_id**](TunnelInterfacesApi.md#delete_tunnel_interfaces_by_id) | **DELETE** /tunnel-interfaces/{id} | Delete a tunnel interface
[**get_tunnel_interfaces_by_id**](TunnelInterfacesApi.md#get_tunnel_interfaces_by_id) | **GET** /tunnel-interfaces/{id} | Get a tunnel interface
[**list_tunnel_interfaces**](TunnelInterfacesApi.md#list_tunnel_interfaces) | **GET** /tunnel-interfaces | List tunnel interfaces
[**update_tunnel_interfaces_by_id**](TunnelInterfacesApi.md#update_tunnel_interfaces_by_id) | **PUT** /tunnel-interfaces/{id} | Update a tunnel interface


# **create_tunnel_interfaces**
> TunnelInterfaces create_tunnel_interfaces(tunnel_interfaces=tunnel_interfaces)

Create a tunnel interface

Create a new tunnel interface. 

### Example

* Bearer (JWT) Authentication (scmToken):

```python
import scm.network_services
from scm.network_services.models.tunnel_interfaces import TunnelInterfaces
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
    api_instance = scm.network_services.TunnelInterfacesApi(api_client)
    tunnel_interfaces = scm.network_services.TunnelInterfaces() # TunnelInterfaces | Created (optional)

    try:
        # Create a tunnel interface
        api_response = api_instance.create_tunnel_interfaces(tunnel_interfaces=tunnel_interfaces)
        print("The response of TunnelInterfacesApi->create_tunnel_interfaces:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TunnelInterfacesApi->create_tunnel_interfaces: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tunnel_interfaces** | [**TunnelInterfaces**](TunnelInterfaces.md)| Created | [optional] 

### Return type

[**TunnelInterfaces**](TunnelInterfaces.md)

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

# **delete_tunnel_interfaces_by_id**
> delete_tunnel_interfaces_by_id(id)

Delete a tunnel interface

Delete a tunnel interface. 

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
    api_instance = scm.network_services.TunnelInterfacesApi(api_client)
    id = '123e4567-e89b-12d3-a456-426655440000' # str | The UUID of the configuration resource

    try:
        # Delete a tunnel interface
        api_instance.delete_tunnel_interfaces_by_id(id)
    except Exception as e:
        print("Exception when calling TunnelInterfacesApi->delete_tunnel_interfaces_by_id: %s\n" % e)
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

# **get_tunnel_interfaces_by_id**
> TunnelInterfaces get_tunnel_interfaces_by_id(id)

Get a tunnel interface

Get an existing tunnel interface. 

### Example

* Bearer (JWT) Authentication (scmToken):

```python
import scm.network_services
from scm.network_services.models.tunnel_interfaces import TunnelInterfaces
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
    api_instance = scm.network_services.TunnelInterfacesApi(api_client)
    id = '123e4567-e89b-12d3-a456-426655440000' # str | The UUID of the configuration resource

    try:
        # Get a tunnel interface
        api_response = api_instance.get_tunnel_interfaces_by_id(id)
        print("The response of TunnelInterfacesApi->get_tunnel_interfaces_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TunnelInterfacesApi->get_tunnel_interfaces_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The UUID of the configuration resource | 

### Return type

[**TunnelInterfaces**](TunnelInterfaces.md)

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

# **list_tunnel_interfaces**
> TunnelInterfacesListResponse list_tunnel_interfaces(limit=limit, offset=offset, name=name, folder=folder, snippet=snippet, device=device)

List tunnel interfaces

Retrieve a list of tunnel interfaces. 

### Example

* Bearer (JWT) Authentication (scmToken):

```python
import scm.network_services
from scm.network_services.models.tunnel_interfaces_list_response import TunnelInterfacesListResponse
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
    api_instance = scm.network_services.TunnelInterfacesApi(api_client)
    limit = 200 # int | The maximum number of results per page (optional) (default to 200)
    offset = 0 # int | The offset into the list of results returned (optional) (default to 0)
    name = 'name_example' # str | The name of the configuration resource (optional)
    folder = 'folder_example' # str | The folder in which the resource is defined  (optional)
    snippet = 'snippet_example' # str | The snippet in which the resource is defined  (optional)
    device = 'device_example' # str | The device in which the resource is defined  (optional)

    try:
        # List tunnel interfaces
        api_response = api_instance.list_tunnel_interfaces(limit=limit, offset=offset, name=name, folder=folder, snippet=snippet, device=device)
        print("The response of TunnelInterfacesApi->list_tunnel_interfaces:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TunnelInterfacesApi->list_tunnel_interfaces: %s\n" % e)
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

[**TunnelInterfacesListResponse**](TunnelInterfacesListResponse.md)

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

# **update_tunnel_interfaces_by_id**
> TunnelInterfaces update_tunnel_interfaces_by_id(id, tunnel_interfaces=tunnel_interfaces)

Update a tunnel interface

Update an existing tunnel interface. 

### Example

* Bearer (JWT) Authentication (scmToken):

```python
import scm.network_services
from scm.network_services.models.tunnel_interfaces import TunnelInterfaces
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
    api_instance = scm.network_services.TunnelInterfacesApi(api_client)
    id = '123e4567-e89b-12d3-a456-426655440000' # str | The UUID of the configuration resource
    tunnel_interfaces = scm.network_services.TunnelInterfaces() # TunnelInterfaces | OK (optional)

    try:
        # Update a tunnel interface
        api_response = api_instance.update_tunnel_interfaces_by_id(id, tunnel_interfaces=tunnel_interfaces)
        print("The response of TunnelInterfacesApi->update_tunnel_interfaces_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TunnelInterfacesApi->update_tunnel_interfaces_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The UUID of the configuration resource | 
 **tunnel_interfaces** | [**TunnelInterfaces**](TunnelInterfaces.md)| OK | [optional] 

### Return type

[**TunnelInterfaces**](TunnelInterfaces.md)

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

