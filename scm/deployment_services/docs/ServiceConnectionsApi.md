# scm.deployment_services.ServiceConnectionsApi

All URIs are relative to *https://api.strata.paloaltonetworks.com/config/deployment/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_service_connections**](ServiceConnectionsApi.md#create_service_connections) | **POST** /service-connections | Create a service connection
[**delete_service_connections_by_id**](ServiceConnectionsApi.md#delete_service_connections_by_id) | **DELETE** /service-connections/{id} | Delete a service connection
[**get_service_connections_by_id**](ServiceConnectionsApi.md#get_service_connections_by_id) | **GET** /service-connections/{id} | Get a service connection
[**list_service_connections**](ServiceConnectionsApi.md#list_service_connections) | **GET** /service-connections | List service connections
[**update_service_connections_by_id**](ServiceConnectionsApi.md#update_service_connections_by_id) | **PUT** /service-connections/{id} | Update a service connection


# **create_service_connections**
> ServiceConnections create_service_connections(service_connections=service_connections)

Create a service connection

Create a new service connection. 

### Example

* Bearer (JWT) Authentication (scmToken):

```python
import scm.deployment_services
from scm.deployment_services.models.service_connections import ServiceConnections
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
    api_instance = scm.deployment_services.ServiceConnectionsApi(api_client)
    service_connections = scm.deployment_services.ServiceConnections() # ServiceConnections | Created (optional)

    try:
        # Create a service connection
        api_response = api_instance.create_service_connections(service_connections=service_connections)
        print("The response of ServiceConnectionsApi->create_service_connections:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServiceConnectionsApi->create_service_connections: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_connections** | [**ServiceConnections**](ServiceConnections.md)| Created | [optional] 

### Return type

[**ServiceConnections**](ServiceConnections.md)

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

# **delete_service_connections_by_id**
> delete_service_connections_by_id(id)

Delete a service connection

Delete a service connection. 

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
    api_instance = scm.deployment_services.ServiceConnectionsApi(api_client)
    id = 'id_example' # str | The UUID of the configuration resource

    try:
        # Delete a service connection
        api_instance.delete_service_connections_by_id(id)
    except Exception as e:
        print("Exception when calling ServiceConnectionsApi->delete_service_connections_by_id: %s\n" % e)
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

# **get_service_connections_by_id**
> ServiceConnections get_service_connections_by_id(id)

Get a service connection

Get an existing service connection. 

### Example

* Bearer (JWT) Authentication (scmToken):

```python
import scm.deployment_services
from scm.deployment_services.models.service_connections import ServiceConnections
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
    api_instance = scm.deployment_services.ServiceConnectionsApi(api_client)
    id = 'id_example' # str | The UUID of the configuration resource

    try:
        # Get a service connection
        api_response = api_instance.get_service_connections_by_id(id)
        print("The response of ServiceConnectionsApi->get_service_connections_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServiceConnectionsApi->get_service_connections_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The UUID of the configuration resource | 

### Return type

[**ServiceConnections**](ServiceConnections.md)

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

# **list_service_connections**
> ServiceConnectionsListResponse list_service_connections(folder, limit=limit, offset=offset, name=name)

List service connections

Retrieve a list of service connections. 

### Example

* Bearer (JWT) Authentication (scmToken):

```python
import scm.deployment_services
from scm.deployment_services.models.service_connections_list_response import ServiceConnectionsListResponse
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
    api_instance = scm.deployment_services.ServiceConnectionsApi(api_client)
    folder = Service Connections # str | The folder in which the resource is defined  (default to Service Connections)
    limit = 200 # int | The maximum number of results per page (optional) (default to 200)
    offset = 0 # int | The offset into the list of results returned (optional) (default to 0)
    name = 'name_example' # str | The name of the configuration resource (optional)

    try:
        # List service connections
        api_response = api_instance.list_service_connections(folder, limit=limit, offset=offset, name=name)
        print("The response of ServiceConnectionsApi->list_service_connections:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServiceConnectionsApi->list_service_connections: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **folder** | **str**| The folder in which the resource is defined  | [default to Service Connections]
 **limit** | **int**| The maximum number of results per page | [optional] [default to 200]
 **offset** | **int**| The offset into the list of results returned | [optional] [default to 0]
 **name** | **str**| The name of the configuration resource | [optional] 

### Return type

[**ServiceConnectionsListResponse**](ServiceConnectionsListResponse.md)

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

# **update_service_connections_by_id**
> ServiceConnections update_service_connections_by_id(id, service_connections=service_connections)

Update a service connection

Update an existing service connection. 

### Example

* Bearer (JWT) Authentication (scmToken):

```python
import scm.deployment_services
from scm.deployment_services.models.service_connections import ServiceConnections
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
    api_instance = scm.deployment_services.ServiceConnectionsApi(api_client)
    id = 'id_example' # str | The UUID of the configuration resource
    service_connections = scm.deployment_services.ServiceConnections() # ServiceConnections | OK (optional)

    try:
        # Update a service connection
        api_response = api_instance.update_service_connections_by_id(id, service_connections=service_connections)
        print("The response of ServiceConnectionsApi->update_service_connections_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServiceConnectionsApi->update_service_connections_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The UUID of the configuration resource | 
 **service_connections** | [**ServiceConnections**](ServiceConnections.md)| OK | [optional] 

### Return type

[**ServiceConnections**](ServiceConnections.md)

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

