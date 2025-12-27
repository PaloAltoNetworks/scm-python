# scm.network_services.IPsecTunnelsApi

All URIs are relative to *https://api.strata.paloaltonetworks.com/config/network/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_i_psec_tunnels**](IPsecTunnelsApi.md#create_i_psec_tunnels) | **POST** /ipsec-tunnels | Create an IPsec tunnel
[**delete_i_psec_tunnels_by_id**](IPsecTunnelsApi.md#delete_i_psec_tunnels_by_id) | **DELETE** /ipsec-tunnels/{id} | Delete an IPsec tunnel
[**get_i_psec_tunnels_by_id**](IPsecTunnelsApi.md#get_i_psec_tunnels_by_id) | **GET** /ipsec-tunnels/{id} | Get an IPsec tunnel
[**list_i_psec_tunnels**](IPsecTunnelsApi.md#list_i_psec_tunnels) | **GET** /ipsec-tunnels | List IPsec tunnels
[**update_i_psec_tunnels_by_id**](IPsecTunnelsApi.md#update_i_psec_tunnels_by_id) | **PUT** /ipsec-tunnels/{id} | Update an IPsec tunnel


# **create_i_psec_tunnels**
> IpsecTunnels create_i_psec_tunnels(ipsec_tunnels=ipsec_tunnels)

Create an IPsec tunnel

Create a new IPsec tunnel. 

### Example

* Bearer (JWT) Authentication (scmToken):

```python
import scm.network_services
from scm.network_services.models.ipsec_tunnels import IpsecTunnels
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
    api_instance = scm.network_services.IPsecTunnelsApi(api_client)
    ipsec_tunnels = scm.network_services.IpsecTunnels() # IpsecTunnels | Created (optional)

    try:
        # Create an IPsec tunnel
        api_response = api_instance.create_i_psec_tunnels(ipsec_tunnels=ipsec_tunnels)
        print("The response of IPsecTunnelsApi->create_i_psec_tunnels:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IPsecTunnelsApi->create_i_psec_tunnels: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ipsec_tunnels** | [**IpsecTunnels**](IpsecTunnels.md)| Created | [optional] 

### Return type

[**IpsecTunnels**](IpsecTunnels.md)

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

# **delete_i_psec_tunnels_by_id**
> delete_i_psec_tunnels_by_id(id)

Delete an IPsec tunnel

Delete an IPsec tunnel. 

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
    api_instance = scm.network_services.IPsecTunnelsApi(api_client)
    id = '123e4567-e89b-12d3-a456-426655440000' # str | The UUID of the configuration resource

    try:
        # Delete an IPsec tunnel
        api_instance.delete_i_psec_tunnels_by_id(id)
    except Exception as e:
        print("Exception when calling IPsecTunnelsApi->delete_i_psec_tunnels_by_id: %s\n" % e)
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

# **get_i_psec_tunnels_by_id**
> IpsecTunnels get_i_psec_tunnels_by_id(id)

Get an IPsec tunnel

Get an existing IPsec tunnel. 

### Example

* Bearer (JWT) Authentication (scmToken):

```python
import scm.network_services
from scm.network_services.models.ipsec_tunnels import IpsecTunnels
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
    api_instance = scm.network_services.IPsecTunnelsApi(api_client)
    id = '123e4567-e89b-12d3-a456-426655440000' # str | The UUID of the configuration resource

    try:
        # Get an IPsec tunnel
        api_response = api_instance.get_i_psec_tunnels_by_id(id)
        print("The response of IPsecTunnelsApi->get_i_psec_tunnels_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IPsecTunnelsApi->get_i_psec_tunnels_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The UUID of the configuration resource | 

### Return type

[**IpsecTunnels**](IpsecTunnels.md)

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

# **list_i_psec_tunnels**
> IPsecTunnelsListResponse list_i_psec_tunnels(name=name, folder=folder, snippet=snippet, device=device, offset=offset, limit=limit)

List IPsec tunnels

Retrieve a list of IPsec tunnels. 

### Example

* Bearer (JWT) Authentication (scmToken):

```python
import scm.network_services
from scm.network_services.models.i_psec_tunnels_list_response import IPsecTunnelsListResponse
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
    api_instance = scm.network_services.IPsecTunnelsApi(api_client)
    name = 'name_example' # str | The name of the configuration resource (optional)
    folder = 'folder_example' # str | The folder in which the resource is defined  (optional)
    snippet = 'snippet_example' # str | The snippet in which the resource is defined  (optional)
    device = 'device_example' # str | The device in which the resource is defined  (optional)
    offset = 0 # int | The offset into the list of results returned (optional) (default to 0)
    limit = 200 # int | The maximum number of results per page (optional) (default to 200)

    try:
        # List IPsec tunnels
        api_response = api_instance.list_i_psec_tunnels(name=name, folder=folder, snippet=snippet, device=device, offset=offset, limit=limit)
        print("The response of IPsecTunnelsApi->list_i_psec_tunnels:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IPsecTunnelsApi->list_i_psec_tunnels: %s\n" % e)
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

[**IPsecTunnelsListResponse**](IPsecTunnelsListResponse.md)

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

# **update_i_psec_tunnels_by_id**
> IpsecTunnels update_i_psec_tunnels_by_id(id, ipsec_tunnels=ipsec_tunnels)

Update an IPsec tunnel

Update an existing IPsec tunnel. 

### Example

* Bearer (JWT) Authentication (scmToken):

```python
import scm.network_services
from scm.network_services.models.ipsec_tunnels import IpsecTunnels
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
    api_instance = scm.network_services.IPsecTunnelsApi(api_client)
    id = '123e4567-e89b-12d3-a456-426655440000' # str | The UUID of the configuration resource
    ipsec_tunnels = scm.network_services.IpsecTunnels() # IpsecTunnels | OK (optional)

    try:
        # Update an IPsec tunnel
        api_response = api_instance.update_i_psec_tunnels_by_id(id, ipsec_tunnels=ipsec_tunnels)
        print("The response of IPsecTunnelsApi->update_i_psec_tunnels_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IPsecTunnelsApi->update_i_psec_tunnels_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The UUID of the configuration resource | 
 **ipsec_tunnels** | [**IpsecTunnels**](IpsecTunnels.md)| OK | [optional] 

### Return type

[**IpsecTunnels**](IpsecTunnels.md)

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

