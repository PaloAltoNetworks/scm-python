# scm_security_services.DecryptionProfilesApi

All URIs are relative to *https://api.strata.paloaltonetworks.com/config/security/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_decryption_profiles**](DecryptionProfilesApi.md#create_decryption_profiles) | **POST** /decryption-profiles | Create a decryption profile
[**delete_decryption_profiles_by_id**](DecryptionProfilesApi.md#delete_decryption_profiles_by_id) | **DELETE** /decryption-profiles/{id} | Delete a decryption profile
[**get_decryption_profiles_by_id**](DecryptionProfilesApi.md#get_decryption_profiles_by_id) | **GET** /decryption-profiles/{id} | Get a decryption profile
[**list_decryption_profiles**](DecryptionProfilesApi.md#list_decryption_profiles) | **GET** /decryption-profiles | List decryption profiles
[**update_decryption_profiles_by_id**](DecryptionProfilesApi.md#update_decryption_profiles_by_id) | **PUT** /decryption-profiles/{id} | Update a decryption profile


# **create_decryption_profiles**
> DecryptionProfiles create_decryption_profiles(decryption_profiles=decryption_profiles)

Create a decryption profile

Create a new decryption profile. 

### Example

* Bearer (JWT) Authentication (scmToken):

```python
import scm_security_services
from scm_security_services.models.decryption_profiles import DecryptionProfiles
from scm_security_services.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.strata.paloaltonetworks.com/config/security/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = scm_security_services.Configuration(
    host = "https://api.strata.paloaltonetworks.com/config/security/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): scmToken
configuration = scm_security_services.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with scm_security_services.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = scm_security_services.DecryptionProfilesApi(api_client)
    decryption_profiles = scm_security_services.DecryptionProfiles() # DecryptionProfiles | Created (optional)

    try:
        # Create a decryption profile
        api_response = api_instance.create_decryption_profiles(decryption_profiles=decryption_profiles)
        print("The response of DecryptionProfilesApi->create_decryption_profiles:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DecryptionProfilesApi->create_decryption_profiles: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **decryption_profiles** | [**DecryptionProfiles**](DecryptionProfiles.md)| Created | [optional] 

### Return type

[**DecryptionProfiles**](DecryptionProfiles.md)

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

# **delete_decryption_profiles_by_id**
> delete_decryption_profiles_by_id(id)

Delete a decryption profile

Delete a decryption profile. 

### Example

* Bearer (JWT) Authentication (scmToken):

```python
import scm_security_services
from scm_security_services.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.strata.paloaltonetworks.com/config/security/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = scm_security_services.Configuration(
    host = "https://api.strata.paloaltonetworks.com/config/security/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): scmToken
configuration = scm_security_services.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with scm_security_services.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = scm_security_services.DecryptionProfilesApi(api_client)
    id = '123e4567-e89b-12d3-a456-426655440000' # str | The UUID of the configuration resource

    try:
        # Delete a decryption profile
        api_instance.delete_decryption_profiles_by_id(id)
    except Exception as e:
        print("Exception when calling DecryptionProfilesApi->delete_decryption_profiles_by_id: %s\n" % e)
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

# **get_decryption_profiles_by_id**
> DecryptionProfiles get_decryption_profiles_by_id(id)

Get a decryption profile

Get an existing decryption profile. 

### Example

* Bearer (JWT) Authentication (scmToken):

```python
import scm_security_services
from scm_security_services.models.decryption_profiles import DecryptionProfiles
from scm_security_services.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.strata.paloaltonetworks.com/config/security/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = scm_security_services.Configuration(
    host = "https://api.strata.paloaltonetworks.com/config/security/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): scmToken
configuration = scm_security_services.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with scm_security_services.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = scm_security_services.DecryptionProfilesApi(api_client)
    id = '123e4567-e89b-12d3-a456-426655440000' # str | The UUID of the configuration resource

    try:
        # Get a decryption profile
        api_response = api_instance.get_decryption_profiles_by_id(id)
        print("The response of DecryptionProfilesApi->get_decryption_profiles_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DecryptionProfilesApi->get_decryption_profiles_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The UUID of the configuration resource | 

### Return type

[**DecryptionProfiles**](DecryptionProfiles.md)

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

# **list_decryption_profiles**
> DecryptionProfilesListResponse list_decryption_profiles(name=name, folder=folder, snippet=snippet, device=device, offset=offset, limit=limit)

List decryption profiles

Retrieve a list of decryption profiles. 

### Example

* Bearer (JWT) Authentication (scmToken):

```python
import scm_security_services
from scm_security_services.models.decryption_profiles_list_response import DecryptionProfilesListResponse
from scm_security_services.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.strata.paloaltonetworks.com/config/security/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = scm_security_services.Configuration(
    host = "https://api.strata.paloaltonetworks.com/config/security/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): scmToken
configuration = scm_security_services.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with scm_security_services.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = scm_security_services.DecryptionProfilesApi(api_client)
    name = 'name_example' # str | The name of the configuration resource (optional)
    folder = 'folder_example' # str | The folder in which the resource is defined  (optional)
    snippet = 'snippet_example' # str | The snippet in which the resource is defined  (optional)
    device = 'device_example' # str | The device in which the resource is defined  (optional)
    offset = 0 # int | The offset into the list of results returned (optional) (default to 0)
    limit = 200 # int | The maximum number of results per page (optional) (default to 200)

    try:
        # List decryption profiles
        api_response = api_instance.list_decryption_profiles(name=name, folder=folder, snippet=snippet, device=device, offset=offset, limit=limit)
        print("The response of DecryptionProfilesApi->list_decryption_profiles:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DecryptionProfilesApi->list_decryption_profiles: %s\n" % e)
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

[**DecryptionProfilesListResponse**](DecryptionProfilesListResponse.md)

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

# **update_decryption_profiles_by_id**
> DecryptionProfiles update_decryption_profiles_by_id(id, decryption_profiles=decryption_profiles)

Update a decryption profile

Update an existing decryption profile. 

### Example

* Bearer (JWT) Authentication (scmToken):

```python
import scm_security_services
from scm_security_services.models.decryption_profiles import DecryptionProfiles
from scm_security_services.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.strata.paloaltonetworks.com/config/security/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = scm_security_services.Configuration(
    host = "https://api.strata.paloaltonetworks.com/config/security/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): scmToken
configuration = scm_security_services.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with scm_security_services.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = scm_security_services.DecryptionProfilesApi(api_client)
    id = '123e4567-e89b-12d3-a456-426655440000' # str | The UUID of the configuration resource
    decryption_profiles = scm_security_services.DecryptionProfiles() # DecryptionProfiles | OK (optional)

    try:
        # Update a decryption profile
        api_response = api_instance.update_decryption_profiles_by_id(id, decryption_profiles=decryption_profiles)
        print("The response of DecryptionProfilesApi->update_decryption_profiles_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DecryptionProfilesApi->update_decryption_profiles_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The UUID of the configuration resource | 
 **decryption_profiles** | [**DecryptionProfiles**](DecryptionProfiles.md)| OK | [optional] 

### Return type

[**DecryptionProfiles**](DecryptionProfiles.md)

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

