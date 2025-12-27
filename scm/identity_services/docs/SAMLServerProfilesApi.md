# scm.identity_services.SAMLServerProfilesApi

All URIs are relative to *https://api.strata.paloaltonetworks.com/config/identity/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_saml_server_profiles**](SAMLServerProfilesApi.md#create_saml_server_profiles) | **POST** /saml-server-profiles | Create a SAML server profile
[**delete_saml_server_profiles_by_id**](SAMLServerProfilesApi.md#delete_saml_server_profiles_by_id) | **DELETE** /saml-server-profiles/{id} | Delete a SAML server profile
[**get_saml_server_profiles_by_id**](SAMLServerProfilesApi.md#get_saml_server_profiles_by_id) | **GET** /saml-server-profiles/{id} | Get a SAML server profile
[**list_saml_server_profiles**](SAMLServerProfilesApi.md#list_saml_server_profiles) | **GET** /saml-server-profiles | List SAML server profiles
[**update_saml_server_profiles_by_id**](SAMLServerProfilesApi.md#update_saml_server_profiles_by_id) | **PUT** /saml-server-profiles/{id} | Update a SAML server profile


# **create_saml_server_profiles**
> SamlServerProfiles create_saml_server_profiles(saml_server_profiles=saml_server_profiles)

Create a SAML server profile

Create a new SAML server profile. 

### Example

* Bearer (JWT) Authentication (scmToken):

```python
import scm.identity_services
from scm.identity_services.models.saml_server_profiles import SamlServerProfiles
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
    api_instance = scm.identity_services.SAMLServerProfilesApi(api_client)
    saml_server_profiles = scm.identity_services.SamlServerProfiles() # SamlServerProfiles | Created (optional)

    try:
        # Create a SAML server profile
        api_response = api_instance.create_saml_server_profiles(saml_server_profiles=saml_server_profiles)
        print("The response of SAMLServerProfilesApi->create_saml_server_profiles:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SAMLServerProfilesApi->create_saml_server_profiles: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **saml_server_profiles** | [**SamlServerProfiles**](SamlServerProfiles.md)| Created | [optional] 

### Return type

[**SamlServerProfiles**](SamlServerProfiles.md)

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

# **delete_saml_server_profiles_by_id**
> delete_saml_server_profiles_by_id(id)

Delete a SAML server profile

Delete a SAML server profile. 

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
    api_instance = scm.identity_services.SAMLServerProfilesApi(api_client)
    id = '123e4567-e89b-12d3-a456-426655440000' # str | The UUID of the configuration resource

    try:
        # Delete a SAML server profile
        api_instance.delete_saml_server_profiles_by_id(id)
    except Exception as e:
        print("Exception when calling SAMLServerProfilesApi->delete_saml_server_profiles_by_id: %s\n" % e)
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

# **get_saml_server_profiles_by_id**
> SamlServerProfiles get_saml_server_profiles_by_id(id)

Get a SAML server profile

Get an existing SAML server profile. 

### Example

* Bearer (JWT) Authentication (scmToken):

```python
import scm.identity_services
from scm.identity_services.models.saml_server_profiles import SamlServerProfiles
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
    api_instance = scm.identity_services.SAMLServerProfilesApi(api_client)
    id = '123e4567-e89b-12d3-a456-426655440000' # str | The UUID of the configuration resource

    try:
        # Get a SAML server profile
        api_response = api_instance.get_saml_server_profiles_by_id(id)
        print("The response of SAMLServerProfilesApi->get_saml_server_profiles_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SAMLServerProfilesApi->get_saml_server_profiles_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The UUID of the configuration resource | 

### Return type

[**SamlServerProfiles**](SamlServerProfiles.md)

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

# **list_saml_server_profiles**
> SAMLServerProfilesListResponse list_saml_server_profiles(name=name, folder=folder, snippet=snippet, device=device, limit=limit, offset=offset)

List SAML server profiles

Retrieve a list of SAML server profiles. 

### Example

* Bearer (JWT) Authentication (scmToken):

```python
import scm.identity_services
from scm.identity_services.models.saml_server_profiles_list_response import SAMLServerProfilesListResponse
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
    api_instance = scm.identity_services.SAMLServerProfilesApi(api_client)
    name = 'name_example' # str | The name of the configuration resource (optional)
    folder = 'folder_example' # str | The folder in which the resource is defined  (optional)
    snippet = 'snippet_example' # str | The snippet in which the resource is defined  (optional)
    device = 'device_example' # str | The device in which the resource is defined  (optional)
    limit = 200 # int | The maximum number of results per page (optional) (default to 200)
    offset = 0 # int | The offset into the list of results returned (optional) (default to 0)

    try:
        # List SAML server profiles
        api_response = api_instance.list_saml_server_profiles(name=name, folder=folder, snippet=snippet, device=device, limit=limit, offset=offset)
        print("The response of SAMLServerProfilesApi->list_saml_server_profiles:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SAMLServerProfilesApi->list_saml_server_profiles: %s\n" % e)
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

[**SAMLServerProfilesListResponse**](SAMLServerProfilesListResponse.md)

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

# **update_saml_server_profiles_by_id**
> SamlServerProfiles update_saml_server_profiles_by_id(id, saml_server_profiles=saml_server_profiles)

Update a SAML server profile

Update an existing SAML server profile. 

### Example

* Bearer (JWT) Authentication (scmToken):

```python
import scm.identity_services
from scm.identity_services.models.saml_server_profiles import SamlServerProfiles
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
    api_instance = scm.identity_services.SAMLServerProfilesApi(api_client)
    id = '123e4567-e89b-12d3-a456-426655440000' # str | The UUID of the configuration resource
    saml_server_profiles = scm.identity_services.SamlServerProfiles() # SamlServerProfiles | OK (optional)

    try:
        # Update a SAML server profile
        api_response = api_instance.update_saml_server_profiles_by_id(id, saml_server_profiles=saml_server_profiles)
        print("The response of SAMLServerProfilesApi->update_saml_server_profiles_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SAMLServerProfilesApi->update_saml_server_profiles_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The UUID of the configuration resource | 
 **saml_server_profiles** | [**SamlServerProfiles**](SamlServerProfiles.md)| OK | [optional] 

### Return type

[**SamlServerProfiles**](SamlServerProfiles.md)

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

