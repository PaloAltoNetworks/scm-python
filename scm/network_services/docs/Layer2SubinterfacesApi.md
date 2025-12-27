# scm.network_services.Layer2SubinterfacesApi

All URIs are relative to *https://api.strata.paloaltonetworks.com/config/network/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_layer2_subinterfaces**](Layer2SubinterfacesApi.md#create_layer2_subinterfaces) | **POST** /layer2-subinterfaces | Create a layer 2 subinterface
[**delete_layer2_subinterfaces_by_id**](Layer2SubinterfacesApi.md#delete_layer2_subinterfaces_by_id) | **DELETE** /layer2-subinterfaces/{id} | Delete a layer 2 subinterface
[**get_layer2_subinterfaces_by_id**](Layer2SubinterfacesApi.md#get_layer2_subinterfaces_by_id) | **GET** /layer2-subinterfaces/{id} | Get a layer 2 subinterface
[**list_layer2_subinterfaces**](Layer2SubinterfacesApi.md#list_layer2_subinterfaces) | **GET** /layer2-subinterfaces | List layer 2 subinterfaces
[**update_layer2_subinterfaces_by_id**](Layer2SubinterfacesApi.md#update_layer2_subinterfaces_by_id) | **PUT** /layer2-subinterfaces/{id} | Update a layer 2 subinterface


# **create_layer2_subinterfaces**
> Layer2Subinterfaces create_layer2_subinterfaces(layer2_subinterfaces=layer2_subinterfaces)

Create a layer 2 subinterface

Create a new layer 2 subinterface. 

### Example

* Bearer (JWT) Authentication (scmToken):

```python
import scm.network_services
from scm.network_services.models.layer2_subinterfaces import Layer2Subinterfaces
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
    api_instance = scm.network_services.Layer2SubinterfacesApi(api_client)
    layer2_subinterfaces = scm.network_services.Layer2Subinterfaces() # Layer2Subinterfaces | Created (optional)

    try:
        # Create a layer 2 subinterface
        api_response = api_instance.create_layer2_subinterfaces(layer2_subinterfaces=layer2_subinterfaces)
        print("The response of Layer2SubinterfacesApi->create_layer2_subinterfaces:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling Layer2SubinterfacesApi->create_layer2_subinterfaces: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **layer2_subinterfaces** | [**Layer2Subinterfaces**](Layer2Subinterfaces.md)| Created | [optional] 

### Return type

[**Layer2Subinterfaces**](Layer2Subinterfaces.md)

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

# **delete_layer2_subinterfaces_by_id**
> delete_layer2_subinterfaces_by_id(id)

Delete a layer 2 subinterface

Delete a layer 2 subinterface. 

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
    api_instance = scm.network_services.Layer2SubinterfacesApi(api_client)
    id = '123e4567-e89b-12d3-a456-426655440000' # str | The UUID of the configuration resource

    try:
        # Delete a layer 2 subinterface
        api_instance.delete_layer2_subinterfaces_by_id(id)
    except Exception as e:
        print("Exception when calling Layer2SubinterfacesApi->delete_layer2_subinterfaces_by_id: %s\n" % e)
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

# **get_layer2_subinterfaces_by_id**
> Layer2Subinterfaces get_layer2_subinterfaces_by_id(id)

Get a layer 2 subinterface

Get an existing layer 2 subinterface. 

### Example

* Bearer (JWT) Authentication (scmToken):

```python
import scm.network_services
from scm.network_services.models.layer2_subinterfaces import Layer2Subinterfaces
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
    api_instance = scm.network_services.Layer2SubinterfacesApi(api_client)
    id = '123e4567-e89b-12d3-a456-426655440000' # str | The UUID of the configuration resource

    try:
        # Get a layer 2 subinterface
        api_response = api_instance.get_layer2_subinterfaces_by_id(id)
        print("The response of Layer2SubinterfacesApi->get_layer2_subinterfaces_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling Layer2SubinterfacesApi->get_layer2_subinterfaces_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The UUID of the configuration resource | 

### Return type

[**Layer2Subinterfaces**](Layer2Subinterfaces.md)

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

# **list_layer2_subinterfaces**
> Layer2SubinterfacesListResponse list_layer2_subinterfaces(limit=limit, offset=offset, name=name, folder=folder, snippet=snippet, device=device)

List layer 2 subinterfaces

Retrieve a list of layer 2 subinterfaces. 

### Example

* Bearer (JWT) Authentication (scmToken):

```python
import scm.network_services
from scm.network_services.models.layer2_subinterfaces_list_response import Layer2SubinterfacesListResponse
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
    api_instance = scm.network_services.Layer2SubinterfacesApi(api_client)
    limit = 200 # int | The maximum number of results per page (optional) (default to 200)
    offset = 0 # int | The offset into the list of results returned (optional) (default to 0)
    name = 'name_example' # str | The name of the configuration resource (optional)
    folder = 'folder_example' # str | The folder in which the resource is defined  (optional)
    snippet = 'snippet_example' # str | The snippet in which the resource is defined  (optional)
    device = 'device_example' # str | The device in which the resource is defined  (optional)

    try:
        # List layer 2 subinterfaces
        api_response = api_instance.list_layer2_subinterfaces(limit=limit, offset=offset, name=name, folder=folder, snippet=snippet, device=device)
        print("The response of Layer2SubinterfacesApi->list_layer2_subinterfaces:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling Layer2SubinterfacesApi->list_layer2_subinterfaces: %s\n" % e)
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

[**Layer2SubinterfacesListResponse**](Layer2SubinterfacesListResponse.md)

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

# **update_layer2_subinterfaces_by_id**
> Layer2Subinterfaces update_layer2_subinterfaces_by_id(id, layer2_subinterfaces=layer2_subinterfaces)

Update a layer 2 subinterface

Update an existing layer 2 subinterface. 

### Example

* Bearer (JWT) Authentication (scmToken):

```python
import scm.network_services
from scm.network_services.models.layer2_subinterfaces import Layer2Subinterfaces
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
    api_instance = scm.network_services.Layer2SubinterfacesApi(api_client)
    id = '123e4567-e89b-12d3-a456-426655440000' # str | The UUID of the configuration resource
    layer2_subinterfaces = scm.network_services.Layer2Subinterfaces() # Layer2Subinterfaces | OK (optional)

    try:
        # Update a layer 2 subinterface
        api_response = api_instance.update_layer2_subinterfaces_by_id(id, layer2_subinterfaces=layer2_subinterfaces)
        print("The response of Layer2SubinterfacesApi->update_layer2_subinterfaces_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling Layer2SubinterfacesApi->update_layer2_subinterfaces_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The UUID of the configuration resource | 
 **layer2_subinterfaces** | [**Layer2Subinterfaces**](Layer2Subinterfaces.md)| OK | [optional] 

### Return type

[**Layer2Subinterfaces**](Layer2Subinterfaces.md)

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

