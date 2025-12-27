# scm_identity_services.TLSServiceProfilesApi

All URIs are relative to *https://api.strata.paloaltonetworks.com/config/identity/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_tls_service_profiles**](TLSServiceProfilesApi.md#create_tls_service_profiles) | **POST** /tls-service-profiles | Create a TLS service profile
[**delete_tls_service_profiles_by_id**](TLSServiceProfilesApi.md#delete_tls_service_profiles_by_id) | **DELETE** /tls-service-profiles/{id} | Delete a TLS service profile
[**get_tls_service_profiles_by_id**](TLSServiceProfilesApi.md#get_tls_service_profiles_by_id) | **GET** /tls-service-profiles/{id} | Get a TLS service profile
[**list_tls_service_profiles**](TLSServiceProfilesApi.md#list_tls_service_profiles) | **GET** /tls-service-profiles | List TLS service profiles
[**update_tls_service_profiles_by_id**](TLSServiceProfilesApi.md#update_tls_service_profiles_by_id) | **PUT** /tls-service-profiles/{id} | Update a TLS service profile


# **create_tls_service_profiles**
> TlsServiceProfiles create_tls_service_profiles(tls_service_profiles=tls_service_profiles)

Create a TLS service profile

Create a new TLS service profile. 

### Example

* Bearer (JWT) Authentication (scmToken):

```python
import scm_identity_services
from scm_identity_services.models.tls_service_profiles import TlsServiceProfiles
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
    api_instance = scm_identity_services.TLSServiceProfilesApi(api_client)
    tls_service_profiles = scm_identity_services.TlsServiceProfiles() # TlsServiceProfiles | Created (optional)

    try:
        # Create a TLS service profile
        api_response = api_instance.create_tls_service_profiles(tls_service_profiles=tls_service_profiles)
        print("The response of TLSServiceProfilesApi->create_tls_service_profiles:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TLSServiceProfilesApi->create_tls_service_profiles: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tls_service_profiles** | [**TlsServiceProfiles**](TlsServiceProfiles.md)| Created | [optional] 

### Return type

[**TlsServiceProfiles**](TlsServiceProfiles.md)

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

# **delete_tls_service_profiles_by_id**
> delete_tls_service_profiles_by_id(id)

Delete a TLS service profile

Delete a TLS service profile. 

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
    api_instance = scm_identity_services.TLSServiceProfilesApi(api_client)
    id = '123e4567-e89b-12d3-a456-426655440000' # str | The UUID of the configuration resource

    try:
        # Delete a TLS service profile
        api_instance.delete_tls_service_profiles_by_id(id)
    except Exception as e:
        print("Exception when calling TLSServiceProfilesApi->delete_tls_service_profiles_by_id: %s\n" % e)
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

# **get_tls_service_profiles_by_id**
> TlsServiceProfiles get_tls_service_profiles_by_id(id)

Get a TLS service profile

Get an existing TLS service profile. 

### Example

* Bearer (JWT) Authentication (scmToken):

```python
import scm_identity_services
from scm_identity_services.models.tls_service_profiles import TlsServiceProfiles
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
    api_instance = scm_identity_services.TLSServiceProfilesApi(api_client)
    id = '123e4567-e89b-12d3-a456-426655440000' # str | The UUID of the configuration resource

    try:
        # Get a TLS service profile
        api_response = api_instance.get_tls_service_profiles_by_id(id)
        print("The response of TLSServiceProfilesApi->get_tls_service_profiles_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TLSServiceProfilesApi->get_tls_service_profiles_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The UUID of the configuration resource | 

### Return type

[**TlsServiceProfiles**](TlsServiceProfiles.md)

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

# **list_tls_service_profiles**
> TLSServiceProfilesListResponse list_tls_service_profiles(name=name, folder=folder, snippet=snippet, device=device, limit=limit, offset=offset)

List TLS service profiles

Retrieve a list of TLS service profiles. 

### Example

* Bearer (JWT) Authentication (scmToken):

```python
import scm_identity_services
from scm_identity_services.models.tls_service_profiles_list_response import TLSServiceProfilesListResponse
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
    api_instance = scm_identity_services.TLSServiceProfilesApi(api_client)
    name = 'name_example' # str | The name of the configuration resource (optional)
    folder = 'folder_example' # str | The folder in which the resource is defined  (optional)
    snippet = 'snippet_example' # str | The snippet in which the resource is defined  (optional)
    device = 'device_example' # str | The device in which the resource is defined  (optional)
    limit = 200 # int | The maximum number of results per page (optional) (default to 200)
    offset = 0 # int | The offset into the list of results returned (optional) (default to 0)

    try:
        # List TLS service profiles
        api_response = api_instance.list_tls_service_profiles(name=name, folder=folder, snippet=snippet, device=device, limit=limit, offset=offset)
        print("The response of TLSServiceProfilesApi->list_tls_service_profiles:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TLSServiceProfilesApi->list_tls_service_profiles: %s\n" % e)
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

[**TLSServiceProfilesListResponse**](TLSServiceProfilesListResponse.md)

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

# **update_tls_service_profiles_by_id**
> TlsServiceProfiles update_tls_service_profiles_by_id(id, tls_service_profiles=tls_service_profiles)

Update a TLS service profile

Update an existing TLS service profile. 

### Example

* Bearer (JWT) Authentication (scmToken):

```python
import scm_identity_services
from scm_identity_services.models.tls_service_profiles import TlsServiceProfiles
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
    api_instance = scm_identity_services.TLSServiceProfilesApi(api_client)
    id = '123e4567-e89b-12d3-a456-426655440000' # str | The UUID of the configuration resource
    tls_service_profiles = scm_identity_services.TlsServiceProfiles() # TlsServiceProfiles | OK (optional)

    try:
        # Update a TLS service profile
        api_response = api_instance.update_tls_service_profiles_by_id(id, tls_service_profiles=tls_service_profiles)
        print("The response of TLSServiceProfilesApi->update_tls_service_profiles_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TLSServiceProfilesApi->update_tls_service_profiles_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The UUID of the configuration resource | 
 **tls_service_profiles** | [**TlsServiceProfiles**](TlsServiceProfiles.md)| OK | [optional] 

### Return type

[**TlsServiceProfiles**](TlsServiceProfiles.md)

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

