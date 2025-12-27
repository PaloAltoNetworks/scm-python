# scm_network_services.OSPFAuthenticationProfilesApi

All URIs are relative to *https://api.strata.paloaltonetworks.com/config/network/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_ospf_authentication_profiles**](OSPFAuthenticationProfilesApi.md#create_ospf_authentication_profiles) | **POST** /ospf-auth-profiles | Create an OSPF authentication profile
[**delete_ospf_authentication_profiles_by_id**](OSPFAuthenticationProfilesApi.md#delete_ospf_authentication_profiles_by_id) | **DELETE** /ospf-auth-profiles/{id} | Delete an OSPF authentication profile
[**get_ospf_authentication_profiles_by_id**](OSPFAuthenticationProfilesApi.md#get_ospf_authentication_profiles_by_id) | **GET** /ospf-auth-profiles/{id} | Get an OSPF authentication profile
[**list_ospf_authentication_profiles**](OSPFAuthenticationProfilesApi.md#list_ospf_authentication_profiles) | **GET** /ospf-auth-profiles | List OSPF authentication profiles
[**update_ospf_authentication_profiles_by_id**](OSPFAuthenticationProfilesApi.md#update_ospf_authentication_profiles_by_id) | **PUT** /ospf-auth-profiles/{id} | Update an OSPF authentication profile


# **create_ospf_authentication_profiles**
> OspfAuthProfiles create_ospf_authentication_profiles(ospf_auth_profiles=ospf_auth_profiles)

Create an OSPF authentication profile

Create a new OSPF authentication profile. 

### Example

* Bearer (JWT) Authentication (scmToken):

```python
import scm_network_services
from scm_network_services.models.ospf_auth_profiles import OspfAuthProfiles
from scm_network_services.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.strata.paloaltonetworks.com/config/network/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = scm_network_services.Configuration(
    host = "https://api.strata.paloaltonetworks.com/config/network/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): scmToken
configuration = scm_network_services.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with scm_network_services.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = scm_network_services.OSPFAuthenticationProfilesApi(api_client)
    ospf_auth_profiles = scm_network_services.OspfAuthProfiles() # OspfAuthProfiles | Created (optional)

    try:
        # Create an OSPF authentication profile
        api_response = api_instance.create_ospf_authentication_profiles(ospf_auth_profiles=ospf_auth_profiles)
        print("The response of OSPFAuthenticationProfilesApi->create_ospf_authentication_profiles:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OSPFAuthenticationProfilesApi->create_ospf_authentication_profiles: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ospf_auth_profiles** | [**OspfAuthProfiles**](OspfAuthProfiles.md)| Created | [optional] 

### Return type

[**OspfAuthProfiles**](OspfAuthProfiles.md)

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

# **delete_ospf_authentication_profiles_by_id**
> delete_ospf_authentication_profiles_by_id(id)

Delete an OSPF authentication profile

Delete an OSPF authentication profile. 

### Example

* Bearer (JWT) Authentication (scmToken):

```python
import scm_network_services
from scm_network_services.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.strata.paloaltonetworks.com/config/network/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = scm_network_services.Configuration(
    host = "https://api.strata.paloaltonetworks.com/config/network/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): scmToken
configuration = scm_network_services.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with scm_network_services.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = scm_network_services.OSPFAuthenticationProfilesApi(api_client)
    id = '123e4567-e89b-12d3-a456-426655440000' # str | The UUID of the configuration resource

    try:
        # Delete an OSPF authentication profile
        api_instance.delete_ospf_authentication_profiles_by_id(id)
    except Exception as e:
        print("Exception when calling OSPFAuthenticationProfilesApi->delete_ospf_authentication_profiles_by_id: %s\n" % e)
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

# **get_ospf_authentication_profiles_by_id**
> OspfAuthProfiles get_ospf_authentication_profiles_by_id(id)

Get an OSPF authentication profile

Get an existing OSPF authentication profile. 

### Example

* Bearer (JWT) Authentication (scmToken):

```python
import scm_network_services
from scm_network_services.models.ospf_auth_profiles import OspfAuthProfiles
from scm_network_services.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.strata.paloaltonetworks.com/config/network/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = scm_network_services.Configuration(
    host = "https://api.strata.paloaltonetworks.com/config/network/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): scmToken
configuration = scm_network_services.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with scm_network_services.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = scm_network_services.OSPFAuthenticationProfilesApi(api_client)
    id = '123e4567-e89b-12d3-a456-426655440000' # str | The UUID of the configuration resource

    try:
        # Get an OSPF authentication profile
        api_response = api_instance.get_ospf_authentication_profiles_by_id(id)
        print("The response of OSPFAuthenticationProfilesApi->get_ospf_authentication_profiles_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OSPFAuthenticationProfilesApi->get_ospf_authentication_profiles_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The UUID of the configuration resource | 

### Return type

[**OspfAuthProfiles**](OspfAuthProfiles.md)

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

# **list_ospf_authentication_profiles**
> OSPFAuthenticationProfilesListResponse list_ospf_authentication_profiles(limit=limit, offset=offset, name=name, folder=folder, snippet=snippet, device=device)

List OSPF authentication profiles

Retrieve a list of OSPF authentication profiles. 

### Example

* Bearer (JWT) Authentication (scmToken):

```python
import scm_network_services
from scm_network_services.models.ospf_authentication_profiles_list_response import OSPFAuthenticationProfilesListResponse
from scm_network_services.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.strata.paloaltonetworks.com/config/network/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = scm_network_services.Configuration(
    host = "https://api.strata.paloaltonetworks.com/config/network/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): scmToken
configuration = scm_network_services.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with scm_network_services.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = scm_network_services.OSPFAuthenticationProfilesApi(api_client)
    limit = 200 # int | The maximum number of results per page (optional) (default to 200)
    offset = 0 # int | The offset into the list of results returned (optional) (default to 0)
    name = 'name_example' # str | The name of the configuration resource (optional)
    folder = 'folder_example' # str | The folder in which the resource is defined  (optional)
    snippet = 'snippet_example' # str | The snippet in which the resource is defined  (optional)
    device = 'device_example' # str | The device in which the resource is defined  (optional)

    try:
        # List OSPF authentication profiles
        api_response = api_instance.list_ospf_authentication_profiles(limit=limit, offset=offset, name=name, folder=folder, snippet=snippet, device=device)
        print("The response of OSPFAuthenticationProfilesApi->list_ospf_authentication_profiles:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OSPFAuthenticationProfilesApi->list_ospf_authentication_profiles: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| The maximum number of results per page | [optional] [default to 200]
 **offset** | **int**| The offset into the list of results returned | [optional] [default to 0]
 **name** | **str**| The name of the configuration resource | [optional] 
 **folder** | **str**| The folder in which the resource is defined  | [optional] 
 **snippet** | **str**| The snippet in which the resource is defined  | [optional] 
 **device** | **str**| The device in which the resource is defined  | [optional] 

### Return type

[**OSPFAuthenticationProfilesListResponse**](OSPFAuthenticationProfilesListResponse.md)

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

# **update_ospf_authentication_profiles_by_id**
> OspfAuthProfiles update_ospf_authentication_profiles_by_id(id, ospf_auth_profiles=ospf_auth_profiles)

Update an OSPF authentication profile

Update an existing OSPF authentication profile. 

### Example

* Bearer (JWT) Authentication (scmToken):

```python
import scm_network_services
from scm_network_services.models.ospf_auth_profiles import OspfAuthProfiles
from scm_network_services.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.strata.paloaltonetworks.com/config/network/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = scm_network_services.Configuration(
    host = "https://api.strata.paloaltonetworks.com/config/network/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): scmToken
configuration = scm_network_services.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with scm_network_services.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = scm_network_services.OSPFAuthenticationProfilesApi(api_client)
    id = '123e4567-e89b-12d3-a456-426655440000' # str | The UUID of the configuration resource
    ospf_auth_profiles = scm_network_services.OspfAuthProfiles() # OspfAuthProfiles | OK (optional)

    try:
        # Update an OSPF authentication profile
        api_response = api_instance.update_ospf_authentication_profiles_by_id(id, ospf_auth_profiles=ospf_auth_profiles)
        print("The response of OSPFAuthenticationProfilesApi->update_ospf_authentication_profiles_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OSPFAuthenticationProfilesApi->update_ospf_authentication_profiles_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The UUID of the configuration resource | 
 **ospf_auth_profiles** | [**OspfAuthProfiles**](OspfAuthProfiles.md)| OK | [optional] 

### Return type

[**OspfAuthProfiles**](OspfAuthProfiles.md)

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

