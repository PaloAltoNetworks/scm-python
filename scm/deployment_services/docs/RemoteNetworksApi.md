# scm.deployment_services.RemoteNetworksApi

All URIs are relative to *https://api.strata.paloaltonetworks.com/config/deployment/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_remote_networks**](RemoteNetworksApi.md#create_remote_networks) | **POST** /remote-networks | Create a remote network
[**delete_remote_networks_by_id**](RemoteNetworksApi.md#delete_remote_networks_by_id) | **DELETE** /remote-networks/{id} | Delete a remote network
[**get_remote_networks_by_id**](RemoteNetworksApi.md#get_remote_networks_by_id) | **GET** /remote-networks/{id} | Get a remote network
[**list_remote_networks**](RemoteNetworksApi.md#list_remote_networks) | **GET** /remote-networks | List remote networks
[**update_remote_networks_by_id**](RemoteNetworksApi.md#update_remote_networks_by_id) | **PUT** /remote-networks/{id} | Update a remote network


# **create_remote_networks**
> RemoteNetworks create_remote_networks(remote_networks=remote_networks)

Create a remote network

Create a new remote network. 

### Example

* Bearer (JWT) Authentication (scmToken):

```python
import scm.deployment_services
from scm.deployment_services.models.remote_networks import RemoteNetworks
from scm.deployment_services.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.strata.paloaltonetworks.com/config/deployment/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = scm.deployment_services.Configuration(
    host = "https://api.strata.paloaltonetworks.com/config/deployment/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): scmToken
configuration = scm.deployment_services.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with scm.deployment_services.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = scm.deployment_services.RemoteNetworksApi(api_client)
    remote_networks = scm.deployment_services.RemoteNetworks() # RemoteNetworks | Created (optional)

    try:
        # Create a remote network
        api_response = api_instance.create_remote_networks(remote_networks=remote_networks)
        print("The response of RemoteNetworksApi->create_remote_networks:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RemoteNetworksApi->create_remote_networks: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **remote_networks** | [**RemoteNetworks**](RemoteNetworks.md)| Created | [optional] 

### Return type

[**RemoteNetworks**](RemoteNetworks.md)

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

# **delete_remote_networks_by_id**
> delete_remote_networks_by_id(id)

Delete a remote network

Delete a remote network. 

### Example

* Bearer (JWT) Authentication (scmToken):

```python
import scm.deployment_services
from scm.deployment_services.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.strata.paloaltonetworks.com/config/deployment/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = scm.deployment_services.Configuration(
    host = "https://api.strata.paloaltonetworks.com/config/deployment/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): scmToken
configuration = scm.deployment_services.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with scm.deployment_services.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = scm.deployment_services.RemoteNetworksApi(api_client)
    id = 'id_example' # str | The UUID of the configuration resource

    try:
        # Delete a remote network
        api_instance.delete_remote_networks_by_id(id)
    except Exception as e:
        print("Exception when calling RemoteNetworksApi->delete_remote_networks_by_id: %s\n" % e)
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

# **get_remote_networks_by_id**
> RemoteNetworks get_remote_networks_by_id(id)

Get a remote network

Get an existing remote network. 

### Example

* Bearer (JWT) Authentication (scmToken):

```python
import scm.deployment_services
from scm.deployment_services.models.remote_networks import RemoteNetworks
from scm.deployment_services.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.strata.paloaltonetworks.com/config/deployment/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = scm.deployment_services.Configuration(
    host = "https://api.strata.paloaltonetworks.com/config/deployment/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): scmToken
configuration = scm.deployment_services.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with scm.deployment_services.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = scm.deployment_services.RemoteNetworksApi(api_client)
    id = 'id_example' # str | The UUID of the configuration resource

    try:
        # Get a remote network
        api_response = api_instance.get_remote_networks_by_id(id)
        print("The response of RemoteNetworksApi->get_remote_networks_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RemoteNetworksApi->get_remote_networks_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The UUID of the configuration resource | 

### Return type

[**RemoteNetworks**](RemoteNetworks.md)

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

# **list_remote_networks**
> RemoteNetworksListResponse list_remote_networks(folder, limit=limit, offset=offset, name=name)

List remote networks

Retrieve a list of remote networks. 

### Example

* Bearer (JWT) Authentication (scmToken):

```python
import scm.deployment_services
from scm.deployment_services.models.remote_networks_list_response import RemoteNetworksListResponse
from scm.deployment_services.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.strata.paloaltonetworks.com/config/deployment/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = scm.deployment_services.Configuration(
    host = "https://api.strata.paloaltonetworks.com/config/deployment/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): scmToken
configuration = scm.deployment_services.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with scm.deployment_services.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = scm.deployment_services.RemoteNetworksApi(api_client)
    folder = Remote Networks # str | The folder in which the resource is defined  (default to Remote Networks)
    limit = 200 # int | The maximum number of results per page (optional) (default to 200)
    offset = 0 # int | The offset into the list of results returned (optional) (default to 0)
    name = 'name_example' # str | The name of the configuration resource (optional)

    try:
        # List remote networks
        api_response = api_instance.list_remote_networks(folder, limit=limit, offset=offset, name=name)
        print("The response of RemoteNetworksApi->list_remote_networks:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RemoteNetworksApi->list_remote_networks: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **folder** | **str**| The folder in which the resource is defined  | [default to Remote Networks]
 **limit** | **int**| The maximum number of results per page | [optional] [default to 200]
 **offset** | **int**| The offset into the list of results returned | [optional] [default to 0]
 **name** | **str**| The name of the configuration resource | [optional] 

### Return type

[**RemoteNetworksListResponse**](RemoteNetworksListResponse.md)

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

# **update_remote_networks_by_id**
> RemoteNetworks update_remote_networks_by_id(id, remote_networks=remote_networks)

Update a remote network

Update an existing remote network. 

### Example

* Bearer (JWT) Authentication (scmToken):

```python
import scm.deployment_services
from scm.deployment_services.models.remote_networks import RemoteNetworks
from scm.deployment_services.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.strata.paloaltonetworks.com/config/deployment/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = scm.deployment_services.Configuration(
    host = "https://api.strata.paloaltonetworks.com/config/deployment/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): scmToken
configuration = scm.deployment_services.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with scm.deployment_services.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = scm.deployment_services.RemoteNetworksApi(api_client)
    id = 'id_example' # str | The UUID of the configuration resource
    remote_networks = scm.deployment_services.RemoteNetworks() # RemoteNetworks | OK (optional)

    try:
        # Update a remote network
        api_response = api_instance.update_remote_networks_by_id(id, remote_networks=remote_networks)
        print("The response of RemoteNetworksApi->update_remote_networks_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RemoteNetworksApi->update_remote_networks_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The UUID of the configuration resource | 
 **remote_networks** | [**RemoteNetworks**](RemoteNetworks.md)| OK | [optional] 

### Return type

[**RemoteNetworks**](RemoteNetworks.md)

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

