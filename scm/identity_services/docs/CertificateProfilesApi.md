# scm_identity_services.CertificateProfilesApi

All URIs are relative to *https://api.strata.paloaltonetworks.com/config/identity/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_certificate_profiles**](CertificateProfilesApi.md#create_certificate_profiles) | **POST** /certificate-profiles | Create a certificate profile
[**delete_certificate_profiles_by_id**](CertificateProfilesApi.md#delete_certificate_profiles_by_id) | **DELETE** /certificate-profiles/{id} | Delete a certificate profile
[**get_certificate_profiles_by_id**](CertificateProfilesApi.md#get_certificate_profiles_by_id) | **GET** /certificate-profiles/{id} | Get a certificate profile
[**list_certificate_profiles**](CertificateProfilesApi.md#list_certificate_profiles) | **GET** /certificate-profiles | List certificate profiles
[**update_certificate_profiles_by_id**](CertificateProfilesApi.md#update_certificate_profiles_by_id) | **PUT** /certificate-profiles/{id} | Update a certificate profile


# **create_certificate_profiles**
> CertificateProfiles create_certificate_profiles(certificate_profiles=certificate_profiles)

Create a certificate profile

Create a certificate profile. 

### Example

* Bearer (JWT) Authentication (scmToken):

```python
import scm_identity_services
from scm_identity_services.models.certificate_profiles import CertificateProfiles
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
    api_instance = scm_identity_services.CertificateProfilesApi(api_client)
    certificate_profiles = scm_identity_services.CertificateProfiles() # CertificateProfiles | Created (optional)

    try:
        # Create a certificate profile
        api_response = api_instance.create_certificate_profiles(certificate_profiles=certificate_profiles)
        print("The response of CertificateProfilesApi->create_certificate_profiles:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CertificateProfilesApi->create_certificate_profiles: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **certificate_profiles** | [**CertificateProfiles**](CertificateProfiles.md)| Created | [optional] 

### Return type

[**CertificateProfiles**](CertificateProfiles.md)

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

# **delete_certificate_profiles_by_id**
> delete_certificate_profiles_by_id(id)

Delete a certificate profile

Delete a certificate profile. 

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
    api_instance = scm_identity_services.CertificateProfilesApi(api_client)
    id = '123e4567-e89b-12d3-a456-426655440000' # str | The UUID of the configuration resource

    try:
        # Delete a certificate profile
        api_instance.delete_certificate_profiles_by_id(id)
    except Exception as e:
        print("Exception when calling CertificateProfilesApi->delete_certificate_profiles_by_id: %s\n" % e)
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

# **get_certificate_profiles_by_id**
> CertificateProfiles get_certificate_profiles_by_id(id)

Get a certificate profile

Get an existing certificate profile. 

### Example

* Bearer (JWT) Authentication (scmToken):

```python
import scm_identity_services
from scm_identity_services.models.certificate_profiles import CertificateProfiles
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
    api_instance = scm_identity_services.CertificateProfilesApi(api_client)
    id = '123e4567-e89b-12d3-a456-426655440000' # str | The UUID of the configuration resource

    try:
        # Get a certificate profile
        api_response = api_instance.get_certificate_profiles_by_id(id)
        print("The response of CertificateProfilesApi->get_certificate_profiles_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CertificateProfilesApi->get_certificate_profiles_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The UUID of the configuration resource | 

### Return type

[**CertificateProfiles**](CertificateProfiles.md)

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

# **list_certificate_profiles**
> CertificateProfilesListResponse list_certificate_profiles(name=name, folder=folder, snippet=snippet, device=device, limit=limit, offset=offset)

List certificate profiles

Retrieve a list of certificate profiles. 

### Example

* Bearer (JWT) Authentication (scmToken):

```python
import scm_identity_services
from scm_identity_services.models.certificate_profiles_list_response import CertificateProfilesListResponse
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
    api_instance = scm_identity_services.CertificateProfilesApi(api_client)
    name = 'name_example' # str | The name of the configuration resource (optional)
    folder = 'folder_example' # str | The folder in which the resource is defined  (optional)
    snippet = 'snippet_example' # str | The snippet in which the resource is defined  (optional)
    device = 'device_example' # str | The device in which the resource is defined  (optional)
    limit = 200 # int | The maximum number of results per page (optional) (default to 200)
    offset = 0 # int | The offset into the list of results returned (optional) (default to 0)

    try:
        # List certificate profiles
        api_response = api_instance.list_certificate_profiles(name=name, folder=folder, snippet=snippet, device=device, limit=limit, offset=offset)
        print("The response of CertificateProfilesApi->list_certificate_profiles:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CertificateProfilesApi->list_certificate_profiles: %s\n" % e)
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

[**CertificateProfilesListResponse**](CertificateProfilesListResponse.md)

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

# **update_certificate_profiles_by_id**
> CertificateProfiles update_certificate_profiles_by_id(id, certificate_profiles=certificate_profiles)

Update a certificate profile

Update an existing certificate profile. 

### Example

* Bearer (JWT) Authentication (scmToken):

```python
import scm_identity_services
from scm_identity_services.models.certificate_profiles import CertificateProfiles
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
    api_instance = scm_identity_services.CertificateProfilesApi(api_client)
    id = '123e4567-e89b-12d3-a456-426655440000' # str | The UUID of the configuration resource
    certificate_profiles = scm_identity_services.CertificateProfiles() # CertificateProfiles | OK (optional)

    try:
        # Update a certificate profile
        api_response = api_instance.update_certificate_profiles_by_id(id, certificate_profiles=certificate_profiles)
        print("The response of CertificateProfilesApi->update_certificate_profiles_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CertificateProfilesApi->update_certificate_profiles_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The UUID of the configuration resource | 
 **certificate_profiles** | [**CertificateProfiles**](CertificateProfiles.md)| OK | [optional] 

### Return type

[**CertificateProfiles**](CertificateProfiles.md)

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

