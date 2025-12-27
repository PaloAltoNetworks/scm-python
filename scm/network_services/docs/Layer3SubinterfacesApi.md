# scm.network_services.Layer3SubinterfacesApi

All URIs are relative to *https://api.strata.paloaltonetworks.com/config/network/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_layer3_subinterfaces**](Layer3SubinterfacesApi.md#create_layer3_subinterfaces) | **POST** /layer3-subinterfaces | Create a layer 3 subinterface
[**delete_layer3_subinterfaces_by_id**](Layer3SubinterfacesApi.md#delete_layer3_subinterfaces_by_id) | **DELETE** /layer3-subinterfaces/{id} | Delete a layer 3 subinterface
[**get_layer3_subinterfaces_by_id**](Layer3SubinterfacesApi.md#get_layer3_subinterfaces_by_id) | **GET** /layer3-subinterfaces/{id} | Get a layer 3 subinterface
[**list_layer3_subinterfaces**](Layer3SubinterfacesApi.md#list_layer3_subinterfaces) | **GET** /layer3-subinterfaces | List layer 3 subinterfaces
[**update_layer3_subinterfaces_by_id**](Layer3SubinterfacesApi.md#update_layer3_subinterfaces_by_id) | **PUT** /layer3-subinterfaces/{id} | Update a layer 3 subinterface


# **create_layer3_subinterfaces**
> Layer3Subinterfaces create_layer3_subinterfaces(layer3_subinterfaces=layer3_subinterfaces)

Create a layer 3 subinterface

Create a new layer 3 subinterface. 

### Example

* Bearer (JWT) Authentication (scmToken):

```python
import scm.network_services
from scm.network_services.models.layer3_subinterfaces import Layer3Subinterfaces
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
    api_instance = scm.network_services.Layer3SubinterfacesApi(api_client)
    layer3_subinterfaces = scm.network_services.Layer3Subinterfaces() # Layer3Subinterfaces | Created (optional)

    try:
        # Create a layer 3 subinterface
        api_response = api_instance.create_layer3_subinterfaces(layer3_subinterfaces=layer3_subinterfaces)
        print("The response of Layer3SubinterfacesApi->create_layer3_subinterfaces:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling Layer3SubinterfacesApi->create_layer3_subinterfaces: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **layer3_subinterfaces** | [**Layer3Subinterfaces**](Layer3Subinterfaces.md)| Created | [optional] 

### Return type

[**Layer3Subinterfaces**](Layer3Subinterfaces.md)

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

# **delete_layer3_subinterfaces_by_id**
> delete_layer3_subinterfaces_by_id(id)

Delete a layer 3 subinterface

Delete a layer 3 subinterface. 

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
    api_instance = scm.network_services.Layer3SubinterfacesApi(api_client)
    id = '123e4567-e89b-12d3-a456-426655440000' # str | The UUID of the configuration resource

    try:
        # Delete a layer 3 subinterface
        api_instance.delete_layer3_subinterfaces_by_id(id)
    except Exception as e:
        print("Exception when calling Layer3SubinterfacesApi->delete_layer3_subinterfaces_by_id: %s\n" % e)
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

# **get_layer3_subinterfaces_by_id**
> Layer3Subinterfaces get_layer3_subinterfaces_by_id(id)

Get a layer 3 subinterface

Get an existing layer 3 subinterface. 

### Example

* Bearer (JWT) Authentication (scmToken):

```python
import scm.network_services
from scm.network_services.models.layer3_subinterfaces import Layer3Subinterfaces
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
    api_instance = scm.network_services.Layer3SubinterfacesApi(api_client)
    id = '123e4567-e89b-12d3-a456-426655440000' # str | The UUID of the configuration resource

    try:
        # Get a layer 3 subinterface
        api_response = api_instance.get_layer3_subinterfaces_by_id(id)
        print("The response of Layer3SubinterfacesApi->get_layer3_subinterfaces_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling Layer3SubinterfacesApi->get_layer3_subinterfaces_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The UUID of the configuration resource | 

### Return type

[**Layer3Subinterfaces**](Layer3Subinterfaces.md)

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

# **list_layer3_subinterfaces**
> Layer3SubinterfacesListResponse list_layer3_subinterfaces(limit=limit, offset=offset, name=name, folder=folder, snippet=snippet, device=device)

List layer 3 subinterfaces

Retrieve a list of layer 3 subinterfaces. 

### Example

* Bearer (JWT) Authentication (scmToken):

```python
import scm.network_services
from scm.network_services.models.layer3_subinterfaces_list_response import Layer3SubinterfacesListResponse
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
    api_instance = scm.network_services.Layer3SubinterfacesApi(api_client)
    limit = 200 # int | The maximum number of results per page (optional) (default to 200)
    offset = 0 # int | The offset into the list of results returned (optional) (default to 0)
    name = 'name_example' # str | The name of the configuration resource (optional)
    folder = 'folder_example' # str | The folder in which the resource is defined  (optional)
    snippet = 'snippet_example' # str | The snippet in which the resource is defined  (optional)
    device = 'device_example' # str | The device in which the resource is defined  (optional)

    try:
        # List layer 3 subinterfaces
        api_response = api_instance.list_layer3_subinterfaces(limit=limit, offset=offset, name=name, folder=folder, snippet=snippet, device=device)
        print("The response of Layer3SubinterfacesApi->list_layer3_subinterfaces:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling Layer3SubinterfacesApi->list_layer3_subinterfaces: %s\n" % e)
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

[**Layer3SubinterfacesListResponse**](Layer3SubinterfacesListResponse.md)

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

# **update_layer3_subinterfaces_by_id**
> Layer3Subinterfaces update_layer3_subinterfaces_by_id(id, layer3_subinterfaces=layer3_subinterfaces)

Update a layer 3 subinterface

Update an existing layer 3 subinterface. 

### Example

* Bearer (JWT) Authentication (scmToken):

```python
import scm.network_services
from scm.network_services.models.layer3_subinterfaces import Layer3Subinterfaces
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
    api_instance = scm.network_services.Layer3SubinterfacesApi(api_client)
    id = '123e4567-e89b-12d3-a456-426655440000' # str | The UUID of the configuration resource
    layer3_subinterfaces = scm.network_services.Layer3Subinterfaces() # Layer3Subinterfaces | OK (optional)

    try:
        # Update a layer 3 subinterface
        api_response = api_instance.update_layer3_subinterfaces_by_id(id, layer3_subinterfaces=layer3_subinterfaces)
        print("The response of Layer3SubinterfacesApi->update_layer3_subinterfaces_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling Layer3SubinterfacesApi->update_layer3_subinterfaces_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The UUID of the configuration resource | 
 **layer3_subinterfaces** | [**Layer3Subinterfaces**](Layer3Subinterfaces.md)| OK | [optional] 

### Return type

[**Layer3Subinterfaces**](Layer3Subinterfaces.md)

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

