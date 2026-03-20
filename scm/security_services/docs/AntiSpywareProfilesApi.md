# scm.security_services.AntiSpywareProfilesApi

All URIs are relative to *https://api.strata.paloaltonetworks.com/config/security/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_anti_spyware_profiles**](AntiSpywareProfilesApi.md#create_anti_spyware_profiles) | **POST** /anti-spyware-profiles | Create an anti-spyware profile
[**delete_anti_spyware_profiles_by_id**](AntiSpywareProfilesApi.md#delete_anti_spyware_profiles_by_id) | **DELETE** /anti-spyware-profiles/{id} | Delete an anti-spyware profile
[**get_anti_spyware_profiles_by_id**](AntiSpywareProfilesApi.md#get_anti_spyware_profiles_by_id) | **GET** /anti-spyware-profiles/{id} | Get an anti-spyware profile
[**list_anti_spyware_profiles**](AntiSpywareProfilesApi.md#list_anti_spyware_profiles) | **GET** /anti-spyware-profiles | List anti-spyware profiles
[**update_anti_spyware_profiles_by_id**](AntiSpywareProfilesApi.md#update_anti_spyware_profiles_by_id) | **PUT** /anti-spyware-profiles/{id} | Update an anti-spyware profile


# **create_anti_spyware_profiles**
> AntiSpywareProfiles create_anti_spyware_profiles(anti_spyware_profiles=anti_spyware_profiles)

Create an anti-spyware profile

Create a new anti-spyware profile. 

### Example

* Bearer (JWT) Authentication (scmToken):

```python
import scm.security_services
from scm.security_services.models.anti_spyware_profiles import AntiSpywareProfiles
from scm.security_services.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.strata.paloaltonetworks.com/config/security/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = scm.security_services.Configuration(
    host = "https://api.strata.paloaltonetworks.com/config/security/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): scmToken
configuration = scm.security_services.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with scm.security_services.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = scm.security_services.AntiSpywareProfilesApi(api_client)
    anti_spyware_profiles = scm.security_services.AntiSpywareProfiles() # AntiSpywareProfiles | Created (optional)

    try:
        # Create an anti-spyware profile
        api_response = api_instance.create_anti_spyware_profiles(anti_spyware_profiles=anti_spyware_profiles)
        print("The response of AntiSpywareProfilesApi->create_anti_spyware_profiles:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AntiSpywareProfilesApi->create_anti_spyware_profiles: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **anti_spyware_profiles** | [**AntiSpywareProfiles**](AntiSpywareProfiles.md)| Created | [optional] 

### Return type

[**AntiSpywareProfiles**](AntiSpywareProfiles.md)

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

# **delete_anti_spyware_profiles_by_id**
> delete_anti_spyware_profiles_by_id(id)

Delete an anti-spyware profile

Delete an anti-spyware profile. 

### Example

* Bearer (JWT) Authentication (scmToken):

```python
import scm.security_services
from scm.security_services.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.strata.paloaltonetworks.com/config/security/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = scm.security_services.Configuration(
    host = "https://api.strata.paloaltonetworks.com/config/security/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): scmToken
configuration = scm.security_services.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with scm.security_services.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = scm.security_services.AntiSpywareProfilesApi(api_client)
    id = '123e4567-e89b-12d3-a456-426655440000' # str | The UUID of the configuration resource

    try:
        # Delete an anti-spyware profile
        api_instance.delete_anti_spyware_profiles_by_id(id)
    except Exception as e:
        print("Exception when calling AntiSpywareProfilesApi->delete_anti_spyware_profiles_by_id: %s\n" % e)
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

# **get_anti_spyware_profiles_by_id**
> AntiSpywareProfiles get_anti_spyware_profiles_by_id(id)

Get an anti-spyware profile

Get an existing anti-spyware profile. 

### Example

* Bearer (JWT) Authentication (scmToken):

```python
import scm.security_services
from scm.security_services.models.anti_spyware_profiles import AntiSpywareProfiles
from scm.security_services.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.strata.paloaltonetworks.com/config/security/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = scm.security_services.Configuration(
    host = "https://api.strata.paloaltonetworks.com/config/security/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): scmToken
configuration = scm.security_services.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with scm.security_services.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = scm.security_services.AntiSpywareProfilesApi(api_client)
    id = '123e4567-e89b-12d3-a456-426655440000' # str | The UUID of the configuration resource

    try:
        # Get an anti-spyware profile
        api_response = api_instance.get_anti_spyware_profiles_by_id(id)
        print("The response of AntiSpywareProfilesApi->get_anti_spyware_profiles_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AntiSpywareProfilesApi->get_anti_spyware_profiles_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The UUID of the configuration resource | 

### Return type

[**AntiSpywareProfiles**](AntiSpywareProfiles.md)

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

# **list_anti_spyware_profiles**
> AntiSpywareProfilesListResponse list_anti_spyware_profiles(name=name, folder=folder, snippet=snippet, device=device, offset=offset, limit=limit)

List anti-spyware profiles

Retrieve a list of anti-spyware profiles. 

### Example

* Bearer (JWT) Authentication (scmToken):

```python
import scm.security_services
from scm.security_services.models.anti_spyware_profiles_list_response import AntiSpywareProfilesListResponse
from scm.security_services.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.strata.paloaltonetworks.com/config/security/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = scm.security_services.Configuration(
    host = "https://api.strata.paloaltonetworks.com/config/security/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): scmToken
configuration = scm.security_services.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with scm.security_services.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = scm.security_services.AntiSpywareProfilesApi(api_client)
    name = 'name_example' # str | The name of the configuration resource (optional)
    folder = 'folder_example' # str | The folder in which the resource is defined  (optional)
    snippet = 'snippet_example' # str | The snippet in which the resource is defined  (optional)
    device = 'device_example' # str | The device in which the resource is defined  (optional)
    offset = 0 # int | The offset into the list of results returned (optional) (default to 0)
    limit = 200 # int | The maximum number of results per page (optional) (default to 200)

    try:
        # List anti-spyware profiles
        api_response = api_instance.list_anti_spyware_profiles(name=name, folder=folder, snippet=snippet, device=device, offset=offset, limit=limit)
        print("The response of AntiSpywareProfilesApi->list_anti_spyware_profiles:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AntiSpywareProfilesApi->list_anti_spyware_profiles: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The name of the configuration resource | [optional] 
 **folder** | **str**| The folder in which the resource is defined  | [optional] 
 **snippet** | **str**| The snippet in which the resource is defined  | [optional] 
 **device** | **str**| The device in which the resource is defined  | [optional] 
 **offset** | **int**| The offset into the list of results returned | [optional] [default to 0]
 **limit** | **int**| The maximum number of results per page | [optional] [default to 200]

### Return type

[**AntiSpywareProfilesListResponse**](AntiSpywareProfilesListResponse.md)

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

# **update_anti_spyware_profiles_by_id**
> AntiSpywareProfiles update_anti_spyware_profiles_by_id(id, anti_spyware_profiles=anti_spyware_profiles)

Update an anti-spyware profile

Update an existing anti-spyware profile. 

### Example

* Bearer (JWT) Authentication (scmToken):

```python
import scm.security_services
from scm.security_services.models.anti_spyware_profiles import AntiSpywareProfiles
from scm.security_services.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.strata.paloaltonetworks.com/config/security/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = scm.security_services.Configuration(
    host = "https://api.strata.paloaltonetworks.com/config/security/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): scmToken
configuration = scm.security_services.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with scm.security_services.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = scm.security_services.AntiSpywareProfilesApi(api_client)
    id = '123e4567-e89b-12d3-a456-426655440000' # str | The UUID of the configuration resource
    anti_spyware_profiles = scm.security_services.AntiSpywareProfiles() # AntiSpywareProfiles | OK (optional)

    try:
        # Update an anti-spyware profile
        api_response = api_instance.update_anti_spyware_profiles_by_id(id, anti_spyware_profiles=anti_spyware_profiles)
        print("The response of AntiSpywareProfilesApi->update_anti_spyware_profiles_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AntiSpywareProfilesApi->update_anti_spyware_profiles_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The UUID of the configuration resource | 
 **anti_spyware_profiles** | [**AntiSpywareProfiles**](AntiSpywareProfiles.md)| OK | [optional] 

### Return type

[**AntiSpywareProfiles**](AntiSpywareProfiles.md)

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

