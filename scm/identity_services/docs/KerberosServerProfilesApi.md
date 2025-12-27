# scm_identity_services.KerberosServerProfilesApi

All URIs are relative to *https://api.strata.paloaltonetworks.com/config/identity/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_kerberos_server_profiles**](KerberosServerProfilesApi.md#create_kerberos_server_profiles) | **POST** /kerberos-server-profiles | Create a Kerberos server profile
[**delete_kerberos_server_profiles_by_id**](KerberosServerProfilesApi.md#delete_kerberos_server_profiles_by_id) | **DELETE** /kerberos-server-profiles/{id} | Delete a Kerberos server profile
[**get_kerberos_server_profiles_by_id**](KerberosServerProfilesApi.md#get_kerberos_server_profiles_by_id) | **GET** /kerberos-server-profiles/{id} | Get a Kerberos server profile
[**list_kerberos_server_profiles**](KerberosServerProfilesApi.md#list_kerberos_server_profiles) | **GET** /kerberos-server-profiles | List Kerberos server profiles
[**update_kerberos_server_profiles_by_id**](KerberosServerProfilesApi.md#update_kerberos_server_profiles_by_id) | **PUT** /kerberos-server-profiles/{id} | Update a Kerberos server profile


# **create_kerberos_server_profiles**
> KerberosServerProfiles create_kerberos_server_profiles(kerberos_server_profiles=kerberos_server_profiles)

Create a Kerberos server profile

Create a new Kerberos server profile. 

### Example

* Bearer (JWT) Authentication (scmToken):

```python
import scm_identity_services
from scm_identity_services.models.kerberos_server_profiles import KerberosServerProfiles
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
    api_instance = scm_identity_services.KerberosServerProfilesApi(api_client)
    kerberos_server_profiles = scm_identity_services.KerberosServerProfiles() # KerberosServerProfiles | Created (optional)

    try:
        # Create a Kerberos server profile
        api_response = api_instance.create_kerberos_server_profiles(kerberos_server_profiles=kerberos_server_profiles)
        print("The response of KerberosServerProfilesApi->create_kerberos_server_profiles:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KerberosServerProfilesApi->create_kerberos_server_profiles: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **kerberos_server_profiles** | [**KerberosServerProfiles**](KerberosServerProfiles.md)| Created | [optional] 

### Return type

[**KerberosServerProfiles**](KerberosServerProfiles.md)

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

# **delete_kerberos_server_profiles_by_id**
> delete_kerberos_server_profiles_by_id(id)

Delete a Kerberos server profile

Delete a Kerberos server profile. 

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
    api_instance = scm_identity_services.KerberosServerProfilesApi(api_client)
    id = '123e4567-e89b-12d3-a456-426655440000' # str | The UUID of the configuration resource

    try:
        # Delete a Kerberos server profile
        api_instance.delete_kerberos_server_profiles_by_id(id)
    except Exception as e:
        print("Exception when calling KerberosServerProfilesApi->delete_kerberos_server_profiles_by_id: %s\n" % e)
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

# **get_kerberos_server_profiles_by_id**
> KerberosServerProfiles get_kerberos_server_profiles_by_id(id)

Get a Kerberos server profile

Get an existing Kerberos server profile. 

### Example

* Bearer (JWT) Authentication (scmToken):

```python
import scm_identity_services
from scm_identity_services.models.kerberos_server_profiles import KerberosServerProfiles
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
    api_instance = scm_identity_services.KerberosServerProfilesApi(api_client)
    id = '123e4567-e89b-12d3-a456-426655440000' # str | The UUID of the configuration resource

    try:
        # Get a Kerberos server profile
        api_response = api_instance.get_kerberos_server_profiles_by_id(id)
        print("The response of KerberosServerProfilesApi->get_kerberos_server_profiles_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KerberosServerProfilesApi->get_kerberos_server_profiles_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The UUID of the configuration resource | 

### Return type

[**KerberosServerProfiles**](KerberosServerProfiles.md)

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

# **list_kerberos_server_profiles**
> KerberosServerProfilesListResponse list_kerberos_server_profiles(name=name, folder=folder, snippet=snippet, device=device, limit=limit, offset=offset)

List Kerberos server profiles

Retrieve a list of Kerberos server profiles. 

### Example

* Bearer (JWT) Authentication (scmToken):

```python
import scm_identity_services
from scm_identity_services.models.kerberos_server_profiles_list_response import KerberosServerProfilesListResponse
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
    api_instance = scm_identity_services.KerberosServerProfilesApi(api_client)
    name = 'name_example' # str | The name of the configuration resource (optional)
    folder = 'folder_example' # str | The folder in which the resource is defined  (optional)
    snippet = 'snippet_example' # str | The snippet in which the resource is defined  (optional)
    device = 'device_example' # str | The device in which the resource is defined  (optional)
    limit = 200 # int | The maximum number of results per page (optional) (default to 200)
    offset = 0 # int | The offset into the list of results returned (optional) (default to 0)

    try:
        # List Kerberos server profiles
        api_response = api_instance.list_kerberos_server_profiles(name=name, folder=folder, snippet=snippet, device=device, limit=limit, offset=offset)
        print("The response of KerberosServerProfilesApi->list_kerberos_server_profiles:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KerberosServerProfilesApi->list_kerberos_server_profiles: %s\n" % e)
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

[**KerberosServerProfilesListResponse**](KerberosServerProfilesListResponse.md)

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

# **update_kerberos_server_profiles_by_id**
> KerberosServerProfiles update_kerberos_server_profiles_by_id(id, kerberos_server_profiles=kerberos_server_profiles)

Update a Kerberos server profile

Update an existing Kerberos server profile. 

### Example

* Bearer (JWT) Authentication (scmToken):

```python
import scm_identity_services
from scm_identity_services.models.kerberos_server_profiles import KerberosServerProfiles
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
    api_instance = scm_identity_services.KerberosServerProfilesApi(api_client)
    id = '123e4567-e89b-12d3-a456-426655440000' # str | The UUID of the configuration resource
    kerberos_server_profiles = scm_identity_services.KerberosServerProfiles() # KerberosServerProfiles | OK (optional)

    try:
        # Update a Kerberos server profile
        api_response = api_instance.update_kerberos_server_profiles_by_id(id, kerberos_server_profiles=kerberos_server_profiles)
        print("The response of KerberosServerProfilesApi->update_kerberos_server_profiles_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KerberosServerProfilesApi->update_kerberos_server_profiles_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The UUID of the configuration resource | 
 **kerberos_server_profiles** | [**KerberosServerProfiles**](KerberosServerProfiles.md)| OK | [optional] 

### Return type

[**KerberosServerProfiles**](KerberosServerProfiles.md)

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

