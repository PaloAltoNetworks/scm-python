# scm_deployment_services.InternalDNSServersApi

All URIs are relative to *https://api.strata.paloaltonetworks.com/config/deployment/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_internal_dns_servers**](InternalDNSServersApi.md#create_internal_dns_servers) | **POST** /internal-dns-servers | Create a internal DNS server
[**delete_internal_dns_servers_by_id**](InternalDNSServersApi.md#delete_internal_dns_servers_by_id) | **DELETE** /internal-dns-servers/{id} | Delete an internal DNS server
[**get_internal_dns_servers_by_id**](InternalDNSServersApi.md#get_internal_dns_servers_by_id) | **GET** /internal-dns-servers/{id} | Get an internal DNS server
[**list_internal_dns_servers**](InternalDNSServersApi.md#list_internal_dns_servers) | **GET** /internal-dns-servers | List internal DNS servers
[**update_internal_dns_servers_by_id**](InternalDNSServersApi.md#update_internal_dns_servers_by_id) | **PUT** /internal-dns-servers/{id} | Update an internal DNS server


# **create_internal_dns_servers**
> InternalDnsServers create_internal_dns_servers(internal_dns_servers=internal_dns_servers)

Create a internal DNS server

Create a new internal DNS server. 

### Example

* Bearer (JWT) Authentication (scmToken):

```python
import scm_deployment_services
from scm_deployment_services.models.internal_dns_servers import InternalDnsServers
from scm_deployment_services.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.strata.paloaltonetworks.com/config/deployment/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = scm_deployment_services.Configuration(
    host = "https://api.strata.paloaltonetworks.com/config/deployment/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): scmToken
configuration = scm_deployment_services.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with scm_deployment_services.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = scm_deployment_services.InternalDNSServersApi(api_client)
    internal_dns_servers = scm_deployment_services.InternalDnsServers() # InternalDnsServers | Created (optional)

    try:
        # Create a internal DNS server
        api_response = api_instance.create_internal_dns_servers(internal_dns_servers=internal_dns_servers)
        print("The response of InternalDNSServersApi->create_internal_dns_servers:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InternalDNSServersApi->create_internal_dns_servers: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **internal_dns_servers** | [**InternalDnsServers**](InternalDnsServers.md)| Created | [optional] 

### Return type

[**InternalDnsServers**](InternalDnsServers.md)

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

# **delete_internal_dns_servers_by_id**
> delete_internal_dns_servers_by_id(id)

Delete an internal DNS server

Delete an internal DNS server. 

### Example

* Bearer (JWT) Authentication (scmToken):

```python
import scm_deployment_services
from scm_deployment_services.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.strata.paloaltonetworks.com/config/deployment/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = scm_deployment_services.Configuration(
    host = "https://api.strata.paloaltonetworks.com/config/deployment/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): scmToken
configuration = scm_deployment_services.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with scm_deployment_services.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = scm_deployment_services.InternalDNSServersApi(api_client)
    id = 'id_example' # str | The UUID of the configuration resource

    try:
        # Delete an internal DNS server
        api_instance.delete_internal_dns_servers_by_id(id)
    except Exception as e:
        print("Exception when calling InternalDNSServersApi->delete_internal_dns_servers_by_id: %s\n" % e)
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

# **get_internal_dns_servers_by_id**
> InternalDnsServers get_internal_dns_servers_by_id(id)

Get an internal DNS server

Get an existing internal DNS server. 

### Example

* Bearer (JWT) Authentication (scmToken):

```python
import scm_deployment_services
from scm_deployment_services.models.internal_dns_servers import InternalDnsServers
from scm_deployment_services.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.strata.paloaltonetworks.com/config/deployment/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = scm_deployment_services.Configuration(
    host = "https://api.strata.paloaltonetworks.com/config/deployment/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): scmToken
configuration = scm_deployment_services.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with scm_deployment_services.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = scm_deployment_services.InternalDNSServersApi(api_client)
    id = 'id_example' # str | The UUID of the configuration resource

    try:
        # Get an internal DNS server
        api_response = api_instance.get_internal_dns_servers_by_id(id)
        print("The response of InternalDNSServersApi->get_internal_dns_servers_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InternalDNSServersApi->get_internal_dns_servers_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The UUID of the configuration resource | 

### Return type

[**InternalDnsServers**](InternalDnsServers.md)

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

# **list_internal_dns_servers**
> InternalDNSServersListResponse list_internal_dns_servers(limit=limit, offset=offset, name=name)

List internal DNS servers

Retrieve a list of internal DNS servers. 

### Example

* Bearer (JWT) Authentication (scmToken):

```python
import scm_deployment_services
from scm_deployment_services.models.internal_dns_servers_list_response import InternalDNSServersListResponse
from scm_deployment_services.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.strata.paloaltonetworks.com/config/deployment/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = scm_deployment_services.Configuration(
    host = "https://api.strata.paloaltonetworks.com/config/deployment/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): scmToken
configuration = scm_deployment_services.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with scm_deployment_services.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = scm_deployment_services.InternalDNSServersApi(api_client)
    limit = 200 # int | The maximum number of results per page (optional) (default to 200)
    offset = 0 # int | The offset into the list of results returned (optional) (default to 0)
    name = 'name_example' # str | The name of the configuration resource (optional)

    try:
        # List internal DNS servers
        api_response = api_instance.list_internal_dns_servers(limit=limit, offset=offset, name=name)
        print("The response of InternalDNSServersApi->list_internal_dns_servers:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InternalDNSServersApi->list_internal_dns_servers: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| The maximum number of results per page | [optional] [default to 200]
 **offset** | **int**| The offset into the list of results returned | [optional] [default to 0]
 **name** | **str**| The name of the configuration resource | [optional] 

### Return type

[**InternalDNSServersListResponse**](InternalDNSServersListResponse.md)

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

# **update_internal_dns_servers_by_id**
> InternalDnsServers update_internal_dns_servers_by_id(id, internal_dns_servers=internal_dns_servers)

Update an internal DNS server

Update an existing internal dns server. 

### Example

* Bearer (JWT) Authentication (scmToken):

```python
import scm_deployment_services
from scm_deployment_services.models.internal_dns_servers import InternalDnsServers
from scm_deployment_services.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.strata.paloaltonetworks.com/config/deployment/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = scm_deployment_services.Configuration(
    host = "https://api.strata.paloaltonetworks.com/config/deployment/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): scmToken
configuration = scm_deployment_services.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with scm_deployment_services.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = scm_deployment_services.InternalDNSServersApi(api_client)
    id = 'id_example' # str | The UUID of the configuration resource
    internal_dns_servers = scm_deployment_services.InternalDnsServers() # InternalDnsServers | OK (optional)

    try:
        # Update an internal DNS server
        api_response = api_instance.update_internal_dns_servers_by_id(id, internal_dns_servers=internal_dns_servers)
        print("The response of InternalDNSServersApi->update_internal_dns_servers_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InternalDNSServersApi->update_internal_dns_servers_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The UUID of the configuration resource | 
 **internal_dns_servers** | [**InternalDnsServers**](InternalDnsServers.md)| OK | [optional] 

### Return type

[**InternalDnsServers**](InternalDnsServers.md)

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

