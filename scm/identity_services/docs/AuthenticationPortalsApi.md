# scm_identity_services.AuthenticationPortalsApi

All URIs are relative to *https://api.strata.paloaltonetworks.com/config/identity/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_authentication_portals**](AuthenticationPortalsApi.md#create_authentication_portals) | **POST** /authentication-portals | Create an authentication portal
[**delete_authentication_portals_by_id**](AuthenticationPortalsApi.md#delete_authentication_portals_by_id) | **DELETE** /authentication-portals/{id} | Delete an authentication portal
[**get_authentication_portals_by_id**](AuthenticationPortalsApi.md#get_authentication_portals_by_id) | **GET** /authentication-portals/{id} | Get an authentication portal
[**list_authentication_portals**](AuthenticationPortalsApi.md#list_authentication_portals) | **GET** /authentication-portals | List authentication portals
[**update_authentication_portals_by_id**](AuthenticationPortalsApi.md#update_authentication_portals_by_id) | **PUT** /authentication-portals/{id} | Update an authentication portal


# **create_authentication_portals**
> AuthenticationPortals create_authentication_portals(authentication_portals=authentication_portals)

Create an authentication portal

Create a new authentication portal. 

### Example

* Bearer (JWT) Authentication (scmToken):

```python
import scm_identity_services
from scm_identity_services.models.authentication_portals import AuthenticationPortals
from scm_identity_services.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.strata.paloaltonetworks.com/config/identity/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = scm_identity_services.Configuration(
    host = "https://api.strata.paloaltonetworks.com/config/identity/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): scmToken
configuration = scm_identity_services.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with scm_identity_services.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = scm_identity_services.AuthenticationPortalsApi(api_client)
    authentication_portals = scm_identity_services.AuthenticationPortals() # AuthenticationPortals | Created (optional)

    try:
        # Create an authentication portal
        api_response = api_instance.create_authentication_portals(authentication_portals=authentication_portals)
        print("The response of AuthenticationPortalsApi->create_authentication_portals:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthenticationPortalsApi->create_authentication_portals: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authentication_portals** | [**AuthenticationPortals**](AuthenticationPortals.md)| Created | [optional] 

### Return type

[**AuthenticationPortals**](AuthenticationPortals.md)

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

# **delete_authentication_portals_by_id**
> delete_authentication_portals_by_id(id)

Delete an authentication portal

Delete an authentication portal. 

### Example

* Bearer (JWT) Authentication (scmToken):

```python
import scm_identity_services
from scm_identity_services.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.strata.paloaltonetworks.com/config/identity/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = scm_identity_services.Configuration(
    host = "https://api.strata.paloaltonetworks.com/config/identity/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): scmToken
configuration = scm_identity_services.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with scm_identity_services.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = scm_identity_services.AuthenticationPortalsApi(api_client)
    id = '123e4567-e89b-12d3-a456-426655440000' # str | The UUID of the configuration resource

    try:
        # Delete an authentication portal
        api_instance.delete_authentication_portals_by_id(id)
    except Exception as e:
        print("Exception when calling AuthenticationPortalsApi->delete_authentication_portals_by_id: %s\n" % e)
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

# **get_authentication_portals_by_id**
> AuthenticationPortals get_authentication_portals_by_id(id)

Get an authentication portal

Get an existing authentication portal. 

### Example

* Bearer (JWT) Authentication (scmToken):

```python
import scm_identity_services
from scm_identity_services.models.authentication_portals import AuthenticationPortals
from scm_identity_services.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.strata.paloaltonetworks.com/config/identity/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = scm_identity_services.Configuration(
    host = "https://api.strata.paloaltonetworks.com/config/identity/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): scmToken
configuration = scm_identity_services.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with scm_identity_services.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = scm_identity_services.AuthenticationPortalsApi(api_client)
    id = '123e4567-e89b-12d3-a456-426655440000' # str | The UUID of the configuration resource

    try:
        # Get an authentication portal
        api_response = api_instance.get_authentication_portals_by_id(id)
        print("The response of AuthenticationPortalsApi->get_authentication_portals_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthenticationPortalsApi->get_authentication_portals_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The UUID of the configuration resource | 

### Return type

[**AuthenticationPortals**](AuthenticationPortals.md)

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

# **list_authentication_portals**
> AuthenticationPortalsListResponse list_authentication_portals(name=name, folder=folder, snippet=snippet, device=device, limit=limit, offset=offset)

List authentication portals

Retreive a list of authentication portals. 

### Example

* Bearer (JWT) Authentication (scmToken):

```python
import scm_identity_services
from scm_identity_services.models.authentication_portals_list_response import AuthenticationPortalsListResponse
from scm_identity_services.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.strata.paloaltonetworks.com/config/identity/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = scm_identity_services.Configuration(
    host = "https://api.strata.paloaltonetworks.com/config/identity/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): scmToken
configuration = scm_identity_services.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with scm_identity_services.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = scm_identity_services.AuthenticationPortalsApi(api_client)
    name = 'name_example' # str | The name of the configuration resource (optional)
    folder = 'folder_example' # str | The folder in which the resource is defined  (optional)
    snippet = 'snippet_example' # str | The snippet in which the resource is defined  (optional)
    device = 'device_example' # str | The device in which the resource is defined  (optional)
    limit = 200 # int | The maximum number of results per page (optional) (default to 200)
    offset = 0 # int | The offset into the list of results returned (optional) (default to 0)

    try:
        # List authentication portals
        api_response = api_instance.list_authentication_portals(name=name, folder=folder, snippet=snippet, device=device, limit=limit, offset=offset)
        print("The response of AuthenticationPortalsApi->list_authentication_portals:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthenticationPortalsApi->list_authentication_portals: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The name of the configuration resource | [optional] 
 **folder** | **str**| The folder in which the resource is defined  | [optional] 
 **snippet** | **str**| The snippet in which the resource is defined  | [optional] 
 **device** | **str**| The device in which the resource is defined  | [optional] 
 **limit** | **int**| The maximum number of results per page | [optional] [default to 200]
 **offset** | **int**| The offset into the list of results returned | [optional] [default to 0]

### Return type

[**AuthenticationPortalsListResponse**](AuthenticationPortalsListResponse.md)

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

# **update_authentication_portals_by_id**
> AuthenticationPortals update_authentication_portals_by_id(id, authentication_portals=authentication_portals)

Update an authentication portal

Update an existing authentication portal. 

### Example

* Bearer (JWT) Authentication (scmToken):

```python
import scm_identity_services
from scm_identity_services.models.authentication_portals import AuthenticationPortals
from scm_identity_services.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.strata.paloaltonetworks.com/config/identity/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = scm_identity_services.Configuration(
    host = "https://api.strata.paloaltonetworks.com/config/identity/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): scmToken
configuration = scm_identity_services.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with scm_identity_services.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = scm_identity_services.AuthenticationPortalsApi(api_client)
    id = '123e4567-e89b-12d3-a456-426655440000' # str | The UUID of the configuration resource
    authentication_portals = scm_identity_services.AuthenticationPortals() # AuthenticationPortals | OK (optional)

    try:
        # Update an authentication portal
        api_response = api_instance.update_authentication_portals_by_id(id, authentication_portals=authentication_portals)
        print("The response of AuthenticationPortalsApi->update_authentication_portals_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthenticationPortalsApi->update_authentication_portals_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The UUID of the configuration resource | 
 **authentication_portals** | [**AuthenticationPortals**](AuthenticationPortals.md)| OK | [optional] 

### Return type

[**AuthenticationPortals**](AuthenticationPortals.md)

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

