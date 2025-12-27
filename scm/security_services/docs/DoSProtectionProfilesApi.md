# scm.security_services.DoSProtectionProfilesApi

All URIs are relative to *https://api.strata.paloaltonetworks.com/config/security/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_do_s_protection_profiles**](DoSProtectionProfilesApi.md#create_do_s_protection_profiles) | **POST** /dos-protection-profiles | Create a DoS protection profile
[**delete_do_s_protection_profiles_by_id**](DoSProtectionProfilesApi.md#delete_do_s_protection_profiles_by_id) | **DELETE** /dos-protection-profiles/{id} | Delete a DoS protection profile
[**get_do_s_protection_profiles_by_id**](DoSProtectionProfilesApi.md#get_do_s_protection_profiles_by_id) | **GET** /dos-protection-profiles/{id} | Get a DoS protection profile
[**list_do_s_protection_profiles**](DoSProtectionProfilesApi.md#list_do_s_protection_profiles) | **GET** /dos-protection-profiles | List DoS protection profiles
[**update_do_s_protection_profiles_by_id**](DoSProtectionProfilesApi.md#update_do_s_protection_profiles_by_id) | **PUT** /dos-protection-profiles/{id} | Update a DoS protection profile


# **create_do_s_protection_profiles**
> DosProtectionProfiles create_do_s_protection_profiles(dos_protection_profiles=dos_protection_profiles)

Create a DoS protection profile

Create a new DoS protection profile. 

### Example

* Bearer (JWT) Authentication (scmToken):

```python
import scm.security_services
from scm.security_services.models.dos_protection_profiles import DosProtectionProfiles
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
    api_instance = scm.security_services.DoSProtectionProfilesApi(api_client)
    dos_protection_profiles = scm.security_services.DosProtectionProfiles() # DosProtectionProfiles | Created (optional)

    try:
        # Create a DoS protection profile
        api_response = api_instance.create_do_s_protection_profiles(dos_protection_profiles=dos_protection_profiles)
        print("The response of DoSProtectionProfilesApi->create_do_s_protection_profiles:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DoSProtectionProfilesApi->create_do_s_protection_profiles: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dos_protection_profiles** | [**DosProtectionProfiles**](DosProtectionProfiles.md)| Created | [optional] 

### Return type

[**DosProtectionProfiles**](DosProtectionProfiles.md)

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

# **delete_do_s_protection_profiles_by_id**
> delete_do_s_protection_profiles_by_id(id)

Delete a DoS protection profile

Delete a DoS protection profile. 

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
    api_instance = scm.security_services.DoSProtectionProfilesApi(api_client)
    id = '123e4567-e89b-12d3-a456-426655440000' # str | The UUID of the configuration resource

    try:
        # Delete a DoS protection profile
        api_instance.delete_do_s_protection_profiles_by_id(id)
    except Exception as e:
        print("Exception when calling DoSProtectionProfilesApi->delete_do_s_protection_profiles_by_id: %s\n" % e)
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

# **get_do_s_protection_profiles_by_id**
> DosProtectionProfiles get_do_s_protection_profiles_by_id(id)

Get a DoS protection profile

Get an existing DoS protection profile. 

### Example

* Bearer (JWT) Authentication (scmToken):

```python
import scm.security_services
from scm.security_services.models.dos_protection_profiles import DosProtectionProfiles
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
    api_instance = scm.security_services.DoSProtectionProfilesApi(api_client)
    id = '123e4567-e89b-12d3-a456-426655440000' # str | The UUID of the configuration resource

    try:
        # Get a DoS protection profile
        api_response = api_instance.get_do_s_protection_profiles_by_id(id)
        print("The response of DoSProtectionProfilesApi->get_do_s_protection_profiles_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DoSProtectionProfilesApi->get_do_s_protection_profiles_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The UUID of the configuration resource | 

### Return type

[**DosProtectionProfiles**](DosProtectionProfiles.md)

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

# **list_do_s_protection_profiles**
> DoSProtectionProfilesListResponse list_do_s_protection_profiles(limit=limit, offset=offset, name=name, folder=folder, snippet=snippet, device=device)

List DoS protection profiles

Retrieve a list of DoS protection profiles. 

### Example

* Bearer (JWT) Authentication (scmToken):

```python
import scm.security_services
from scm.security_services.models.do_s_protection_profiles_list_response import DoSProtectionProfilesListResponse
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
    api_instance = scm.security_services.DoSProtectionProfilesApi(api_client)
    limit = 200 # int | The maximum number of results per page (optional) (default to 200)
    offset = 0 # int | The offset into the list of results returned (optional) (default to 0)
    name = 'name_example' # str | The name of the configuration resource (optional)
    folder = 'folder_example' # str | The folder in which the resource is defined  (optional)
    snippet = 'snippet_example' # str | The snippet in which the resource is defined  (optional)
    device = 'device_example' # str | The device in which the resource is defined  (optional)

    try:
        # List DoS protection profiles
        api_response = api_instance.list_do_s_protection_profiles(limit=limit, offset=offset, name=name, folder=folder, snippet=snippet, device=device)
        print("The response of DoSProtectionProfilesApi->list_do_s_protection_profiles:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DoSProtectionProfilesApi->list_do_s_protection_profiles: %s\n" % e)
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

[**DoSProtectionProfilesListResponse**](DoSProtectionProfilesListResponse.md)

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

# **update_do_s_protection_profiles_by_id**
> DosProtectionProfiles update_do_s_protection_profiles_by_id(id, dos_protection_profiles=dos_protection_profiles)

Update a DoS protection profile

Update an existing DoS protection profile. 

### Example

* Bearer (JWT) Authentication (scmToken):

```python
import scm.security_services
from scm.security_services.models.dos_protection_profiles import DosProtectionProfiles
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
    api_instance = scm.security_services.DoSProtectionProfilesApi(api_client)
    id = '123e4567-e89b-12d3-a456-426655440000' # str | The UUID of the configuration resource
    dos_protection_profiles = scm.security_services.DosProtectionProfiles() # DosProtectionProfiles | OK (optional)

    try:
        # Update a DoS protection profile
        api_response = api_instance.update_do_s_protection_profiles_by_id(id, dos_protection_profiles=dos_protection_profiles)
        print("The response of DoSProtectionProfilesApi->update_do_s_protection_profiles_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DoSProtectionProfilesApi->update_do_s_protection_profiles_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The UUID of the configuration resource | 
 **dos_protection_profiles** | [**DosProtectionProfiles**](DosProtectionProfiles.md)| OK | [optional] 

### Return type

[**DosProtectionProfiles**](DosProtectionProfiles.md)

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

