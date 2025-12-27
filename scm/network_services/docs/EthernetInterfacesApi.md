# scm_network_services.EthernetInterfacesApi

All URIs are relative to *https://api.strata.paloaltonetworks.com/config/network/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_ethernet_interfaces**](EthernetInterfacesApi.md#create_ethernet_interfaces) | **POST** /ethernet-interfaces | Create an ethernet interface
[**delete_ethernet_interfaces_by_id**](EthernetInterfacesApi.md#delete_ethernet_interfaces_by_id) | **DELETE** /ethernet-interfaces/{id} | Delete an ethernet interface
[**get_ethernet_interfaces_by_id**](EthernetInterfacesApi.md#get_ethernet_interfaces_by_id) | **GET** /ethernet-interfaces/{id} | Get an ethernet interface
[**list_ethernet_interfaces**](EthernetInterfacesApi.md#list_ethernet_interfaces) | **GET** /ethernet-interfaces | List ethernet interfaces
[**update_ethernet_interfaces_by_id**](EthernetInterfacesApi.md#update_ethernet_interfaces_by_id) | **PUT** /ethernet-interfaces/{id} | Update an ethernet interface


# **create_ethernet_interfaces**
> EthernetInterfaces create_ethernet_interfaces(ethernet_interfaces=ethernet_interfaces)

Create an ethernet interface

Create a new ethernet interface. 

### Example

* Bearer (JWT) Authentication (scmToken):

```python
import scm_network_services
from scm_network_services.models.ethernet_interfaces import EthernetInterfaces
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
    api_instance = scm_network_services.EthernetInterfacesApi(api_client)
    ethernet_interfaces = scm_network_services.EthernetInterfaces() # EthernetInterfaces | Created (optional)

    try:
        # Create an ethernet interface
        api_response = api_instance.create_ethernet_interfaces(ethernet_interfaces=ethernet_interfaces)
        print("The response of EthernetInterfacesApi->create_ethernet_interfaces:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EthernetInterfacesApi->create_ethernet_interfaces: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ethernet_interfaces** | [**EthernetInterfaces**](EthernetInterfaces.md)| Created | [optional] 

### Return type

[**EthernetInterfaces**](EthernetInterfaces.md)

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

# **delete_ethernet_interfaces_by_id**
> delete_ethernet_interfaces_by_id(id)

Delete an ethernet interface

Delete an ethernet interface. 

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
    api_instance = scm_network_services.EthernetInterfacesApi(api_client)
    id = '123e4567-e89b-12d3-a456-426655440000' # str | The UUID of the configuration resource

    try:
        # Delete an ethernet interface
        api_instance.delete_ethernet_interfaces_by_id(id)
    except Exception as e:
        print("Exception when calling EthernetInterfacesApi->delete_ethernet_interfaces_by_id: %s\n" % e)
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

# **get_ethernet_interfaces_by_id**
> EthernetInterfaces get_ethernet_interfaces_by_id(id)

Get an ethernet interface

Get an existing ethernet interface. 

### Example

* Bearer (JWT) Authentication (scmToken):

```python
import scm_network_services
from scm_network_services.models.ethernet_interfaces import EthernetInterfaces
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
    api_instance = scm_network_services.EthernetInterfacesApi(api_client)
    id = '123e4567-e89b-12d3-a456-426655440000' # str | The UUID of the configuration resource

    try:
        # Get an ethernet interface
        api_response = api_instance.get_ethernet_interfaces_by_id(id)
        print("The response of EthernetInterfacesApi->get_ethernet_interfaces_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EthernetInterfacesApi->get_ethernet_interfaces_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The UUID of the configuration resource | 

### Return type

[**EthernetInterfaces**](EthernetInterfaces.md)

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

# **list_ethernet_interfaces**
> EthernetInterfacesListResponse list_ethernet_interfaces(limit=limit, offset=offset, name=name, folder=folder, snippet=snippet, device=device)

List ethernet interfaces

Retrieve a list of ethernet interfaces. 

### Example

* Bearer (JWT) Authentication (scmToken):

```python
import scm_network_services
from scm_network_services.models.ethernet_interfaces_list_response import EthernetInterfacesListResponse
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
    api_instance = scm_network_services.EthernetInterfacesApi(api_client)
    limit = 200 # int | The maximum number of results per page (optional) (default to 200)
    offset = 0 # int | The offset into the list of results returned (optional) (default to 0)
    name = 'name_example' # str | The name of the configuration resource (optional)
    folder = 'folder_example' # str | The folder in which the resource is defined  (optional)
    snippet = 'snippet_example' # str | The snippet in which the resource is defined  (optional)
    device = 'device_example' # str | The device in which the resource is defined  (optional)

    try:
        # List ethernet interfaces
        api_response = api_instance.list_ethernet_interfaces(limit=limit, offset=offset, name=name, folder=folder, snippet=snippet, device=device)
        print("The response of EthernetInterfacesApi->list_ethernet_interfaces:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EthernetInterfacesApi->list_ethernet_interfaces: %s\n" % e)
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

[**EthernetInterfacesListResponse**](EthernetInterfacesListResponse.md)

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

# **update_ethernet_interfaces_by_id**
> EthernetInterfaces update_ethernet_interfaces_by_id(id, ethernet_interfaces=ethernet_interfaces)

Update an ethernet interface

Update an existing ethernet interface. 

### Example

* Bearer (JWT) Authentication (scmToken):

```python
import scm_network_services
from scm_network_services.models.ethernet_interfaces import EthernetInterfaces
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
    api_instance = scm_network_services.EthernetInterfacesApi(api_client)
    id = '123e4567-e89b-12d3-a456-426655440000' # str | The UUID of the configuration resource
    ethernet_interfaces = scm_network_services.EthernetInterfaces() # EthernetInterfaces | OK (optional)

    try:
        # Update an ethernet interface
        api_response = api_instance.update_ethernet_interfaces_by_id(id, ethernet_interfaces=ethernet_interfaces)
        print("The response of EthernetInterfacesApi->update_ethernet_interfaces_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EthernetInterfacesApi->update_ethernet_interfaces_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The UUID of the configuration resource | 
 **ethernet_interfaces** | [**EthernetInterfaces**](EthernetInterfaces.md)| OK | [optional] 

### Return type

[**EthernetInterfaces**](EthernetInterfaces.md)

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

