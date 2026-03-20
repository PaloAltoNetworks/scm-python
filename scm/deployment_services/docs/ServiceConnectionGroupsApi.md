# scm.deployment_services.ServiceConnectionGroupsApi

All URIs are relative to *https://api.strata.paloaltonetworks.com/config/deployment/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_service_connection_groups**](ServiceConnectionGroupsApi.md#create_service_connection_groups) | **POST** /service-connection-groups | Create a service connection group
[**delete_service_connection_groups_by_id**](ServiceConnectionGroupsApi.md#delete_service_connection_groups_by_id) | **DELETE** /service-connection-groups/{id} | Delete a service connection group
[**get_service_connection_groups_by_id**](ServiceConnectionGroupsApi.md#get_service_connection_groups_by_id) | **GET** /service-connection-groups/{id} | Get a service connection group
[**list_service_connection_groups**](ServiceConnectionGroupsApi.md#list_service_connection_groups) | **GET** /service-connection-groups | List service connection groups
[**update_service_connection_groups_by_id**](ServiceConnectionGroupsApi.md#update_service_connection_groups_by_id) | **PUT** /service-connection-groups/{id} | Update a service connection group


# **create_service_connection_groups**
> ServiceConnectionGroups create_service_connection_groups(service_connection_groups=service_connection_groups)

Create a service connection group

Create a new service connection group. 

### Example

* Bearer (JWT) Authentication (scmToken):

```python
import scm.deployment_services
from scm.deployment_services.models.service_connection_groups import ServiceConnectionGroups
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
    api_instance = scm.deployment_services.ServiceConnectionGroupsApi(api_client)
    service_connection_groups = scm.deployment_services.ServiceConnectionGroups() # ServiceConnectionGroups | Created (optional)

    try:
        # Create a service connection group
        api_response = api_instance.create_service_connection_groups(service_connection_groups=service_connection_groups)
        print("The response of ServiceConnectionGroupsApi->create_service_connection_groups:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServiceConnectionGroupsApi->create_service_connection_groups: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_connection_groups** | [**ServiceConnectionGroups**](ServiceConnectionGroups.md)| Created | [optional] 

### Return type

[**ServiceConnectionGroups**](ServiceConnectionGroups.md)

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

# **delete_service_connection_groups_by_id**
> delete_service_connection_groups_by_id(id)

Delete a service connection group

Delete a service connection group. 

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
    api_instance = scm.deployment_services.ServiceConnectionGroupsApi(api_client)
    id = 'id_example' # str | The UUID of the configuration resource

    try:
        # Delete a service connection group
        api_instance.delete_service_connection_groups_by_id(id)
    except Exception as e:
        print("Exception when calling ServiceConnectionGroupsApi->delete_service_connection_groups_by_id: %s\n" % e)
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

# **get_service_connection_groups_by_id**
> ServiceConnectionGroups get_service_connection_groups_by_id(id)

Get a service connection group

Get an existing service connection group. 

### Example

* Bearer (JWT) Authentication (scmToken):

```python
import scm.deployment_services
from scm.deployment_services.models.service_connection_groups import ServiceConnectionGroups
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
    api_instance = scm.deployment_services.ServiceConnectionGroupsApi(api_client)
    id = 'id_example' # str | The UUID of the configuration resource

    try:
        # Get a service connection group
        api_response = api_instance.get_service_connection_groups_by_id(id)
        print("The response of ServiceConnectionGroupsApi->get_service_connection_groups_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServiceConnectionGroupsApi->get_service_connection_groups_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The UUID of the configuration resource | 

### Return type

[**ServiceConnectionGroups**](ServiceConnectionGroups.md)

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

# **list_service_connection_groups**
> ServiceConnectionGroupsListResponse list_service_connection_groups(folder, limit=limit, offset=offset, name=name)

List service connection groups

Retrieve a list of service connection groups. 

### Example

* Bearer (JWT) Authentication (scmToken):

```python
import scm.deployment_services
from scm.deployment_services.models.service_connection_groups_list_response import ServiceConnectionGroupsListResponse
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
    api_instance = scm.deployment_services.ServiceConnectionGroupsApi(api_client)
    folder = Service Connections # str | The folder in which the resource is defined  (default to Service Connections)
    limit = 200 # int | The maximum number of results per page (optional) (default to 200)
    offset = 0 # int | The offset into the list of results returned (optional) (default to 0)
    name = 'name_example' # str | The name of the configuration resource (optional)

    try:
        # List service connection groups
        api_response = api_instance.list_service_connection_groups(folder, limit=limit, offset=offset, name=name)
        print("The response of ServiceConnectionGroupsApi->list_service_connection_groups:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServiceConnectionGroupsApi->list_service_connection_groups: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **folder** | **str**| The folder in which the resource is defined  | [default to Service Connections]
 **limit** | **int**| The maximum number of results per page | [optional] [default to 200]
 **offset** | **int**| The offset into the list of results returned | [optional] [default to 0]
 **name** | **str**| The name of the configuration resource | [optional] 

### Return type

[**ServiceConnectionGroupsListResponse**](ServiceConnectionGroupsListResponse.md)

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

# **update_service_connection_groups_by_id**
> ServiceConnectionGroups update_service_connection_groups_by_id(id, service_connection_groups=service_connection_groups)

Update a service connection group

Update an existing service connection group. 

### Example

* Bearer (JWT) Authentication (scmToken):

```python
import scm.deployment_services
from scm.deployment_services.models.service_connection_groups import ServiceConnectionGroups
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
    api_instance = scm.deployment_services.ServiceConnectionGroupsApi(api_client)
    id = 'id_example' # str | The UUID of the configuration resource
    service_connection_groups = scm.deployment_services.ServiceConnectionGroups() # ServiceConnectionGroups | OK (optional)

    try:
        # Update a service connection group
        api_response = api_instance.update_service_connection_groups_by_id(id, service_connection_groups=service_connection_groups)
        print("The response of ServiceConnectionGroupsApi->update_service_connection_groups_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServiceConnectionGroupsApi->update_service_connection_groups_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The UUID of the configuration resource | 
 **service_connection_groups** | [**ServiceConnectionGroups**](ServiceConnectionGroups.md)| OK | [optional] 

### Return type

[**ServiceConnectionGroups**](ServiceConnectionGroups.md)

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

