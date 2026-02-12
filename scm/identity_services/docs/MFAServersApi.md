# scm.identity_services.MFAServersApi

All URIs are relative to *https://api.strata.paloaltonetworks.com/config/identity/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_mfa_servers**](MFAServersApi.md#create_mfa_servers) | **POST** /mfa-servers | Create an MFA server
[**delete_mfa_servers_by_id**](MFAServersApi.md#delete_mfa_servers_by_id) | **DELETE** /mfa-servers/{id} | Delete an MFA server
[**get_mfa_servers_by_id**](MFAServersApi.md#get_mfa_servers_by_id) | **GET** /mfa-servers/{id} | Get an MFA server
[**list_mfa_servers**](MFAServersApi.md#list_mfa_servers) | **GET** /mfa-servers | List MFA servers
[**update_mfa_servers_by_id**](MFAServersApi.md#update_mfa_servers_by_id) | **PUT** /mfa-servers/{id} | Update an MFA server


# **create_mfa_servers**
> MfaServers create_mfa_servers(mfa_servers=mfa_servers)

Create an MFA server

Create a new MFA server. 

### Example

* Bearer (JWT) Authentication (scmToken):

```python
import scm.identity_services
from scm.identity_services.models.mfa_servers import MfaServers
from scm.identity_services.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.strata.paloaltonetworks.com/config/identity/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = scm.identity_services.Configuration(
    host = "https://api.strata.paloaltonetworks.com/config/identity/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): scmToken
configuration = scm.identity_services.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with scm.identity_services.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = scm.identity_services.MFAServersApi(api_client)
    mfa_servers = scm.identity_services.MfaServers() # MfaServers | Created (optional)

    try:
        # Create an MFA server
        api_response = api_instance.create_mfa_servers(mfa_servers=mfa_servers)
        print("The response of MFAServersApi->create_mfa_servers:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MFAServersApi->create_mfa_servers: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mfa_servers** | [**MfaServers**](MfaServers.md)| Created | [optional] 

### Return type

[**MfaServers**](MfaServers.md)

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
**409** | Conflict |  -  |
**0** | General Errors |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_mfa_servers_by_id**
> delete_mfa_servers_by_id(id)

Delete an MFA server

Delete an MFA server. 

### Example

* Bearer (JWT) Authentication (scmToken):

```python
import scm.identity_services
from scm.identity_services.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.strata.paloaltonetworks.com/config/identity/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = scm.identity_services.Configuration(
    host = "https://api.strata.paloaltonetworks.com/config/identity/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): scmToken
configuration = scm.identity_services.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with scm.identity_services.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = scm.identity_services.MFAServersApi(api_client)
    id = '123e4567-e89b-12d3-a456-426655440000' # str | The UUID of the configuration resource

    try:
        # Delete an MFA server
        api_instance.delete_mfa_servers_by_id(id)
    except Exception as e:
        print("Exception when calling MFAServersApi->delete_mfa_servers_by_id: %s\n" % e)
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

# **get_mfa_servers_by_id**
> MfaServers get_mfa_servers_by_id(id)

Get an MFA server

Get an existing MFA server. 

### Example

* Bearer (JWT) Authentication (scmToken):

```python
import scm.identity_services
from scm.identity_services.models.mfa_servers import MfaServers
from scm.identity_services.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.strata.paloaltonetworks.com/config/identity/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = scm.identity_services.Configuration(
    host = "https://api.strata.paloaltonetworks.com/config/identity/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): scmToken
configuration = scm.identity_services.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with scm.identity_services.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = scm.identity_services.MFAServersApi(api_client)
    id = '123e4567-e89b-12d3-a456-426655440000' # str | The UUID of the configuration resource

    try:
        # Get an MFA server
        api_response = api_instance.get_mfa_servers_by_id(id)
        print("The response of MFAServersApi->get_mfa_servers_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MFAServersApi->get_mfa_servers_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The UUID of the configuration resource | 

### Return type

[**MfaServers**](MfaServers.md)

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

# **list_mfa_servers**
> List[MfaServers] list_mfa_servers(position, name=name, folder=folder, snippet=snippet, device=device, limit=limit, offset=offset)

List MFA servers

Retrieve a list of MFA servers. 

### Example

* Bearer (JWT) Authentication (scmToken):

```python
import scm.identity_services
from scm.identity_services.models.mfa_servers import MfaServers
from scm.identity_services.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.strata.paloaltonetworks.com/config/identity/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = scm.identity_services.Configuration(
    host = "https://api.strata.paloaltonetworks.com/config/identity/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): scmToken
configuration = scm.identity_services.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with scm.identity_services.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = scm.identity_services.MFAServersApi(api_client)
    position = pre # str | The relative position of the rule  (default to pre)
    name = 'name_example' # str | The name of the configuration resource (optional)
    folder = 'folder_example' # str | The folder in which the resource is defined  (optional)
    snippet = 'snippet_example' # str | The snippet in which the resource is defined  (optional)
    device = 'device_example' # str | The device in which the resource is defined  (optional)
    limit = 200 # int | The maximum number of results per page (optional) (default to 200)
    offset = 0 # int | The offset into the list of results returned (optional) (default to 0)

    try:
        # List MFA servers
        api_response = api_instance.list_mfa_servers(position, name=name, folder=folder, snippet=snippet, device=device, limit=limit, offset=offset)
        print("The response of MFAServersApi->list_mfa_servers:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MFAServersApi->list_mfa_servers: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **position** | **str**| The relative position of the rule  | [default to pre]
 **name** | **str**| The name of the configuration resource | [optional] 
 **folder** | **str**| The folder in which the resource is defined  | [optional] 
 **snippet** | **str**| The snippet in which the resource is defined  | [optional] 
 **device** | **str**| The device in which the resource is defined  | [optional] 
 **limit** | **int**| The maximum number of results per page | [optional] [default to 200]
 **offset** | **int**| The offset into the list of results returned | [optional] [default to 0]

### Return type

[**List[MfaServers]**](MfaServers.md)

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

# **update_mfa_servers_by_id**
> MfaServers update_mfa_servers_by_id(id, mfa_servers=mfa_servers)

Update an MFA server

Update an existing MFA server. 

### Example

* Bearer (JWT) Authentication (scmToken):

```python
import scm.identity_services
from scm.identity_services.models.mfa_servers import MfaServers
from scm.identity_services.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.strata.paloaltonetworks.com/config/identity/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = scm.identity_services.Configuration(
    host = "https://api.strata.paloaltonetworks.com/config/identity/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): scmToken
configuration = scm.identity_services.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with scm.identity_services.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = scm.identity_services.MFAServersApi(api_client)
    id = '123e4567-e89b-12d3-a456-426655440000' # str | The UUID of the configuration resource
    mfa_servers = scm.identity_services.MfaServers() # MfaServers | OK (optional)

    try:
        # Update an MFA server
        api_response = api_instance.update_mfa_servers_by_id(id, mfa_servers=mfa_servers)
        print("The response of MFAServersApi->update_mfa_servers_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MFAServersApi->update_mfa_servers_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The UUID of the configuration resource | 
 **mfa_servers** | [**MfaServers**](MfaServers.md)| OK | [optional] 

### Return type

[**MfaServers**](MfaServers.md)

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

