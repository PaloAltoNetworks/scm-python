# scm.security_services.DataFilteringApi

All URIs are relative to *https://api.strata.paloaltonetworks.com/config/security/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_data_filtering_profiles**](DataFilteringApi.md#create_data_filtering_profiles) | **POST** /data-filtering-profiles | Create Data Filtering Profile
[**delete_data_filtering_profiles_by_id**](DataFilteringApi.md#delete_data_filtering_profiles_by_id) | **DELETE** /data-filtering-profiles/{id} | Delete Data Filtering Profile by ID
[**get_data_filtering_profiles_by_id**](DataFilteringApi.md#get_data_filtering_profiles_by_id) | **GET** /data-filtering-profiles/{id} | Get Data Filtering Profile by ID
[**list_data_filtering_profiles**](DataFilteringApi.md#list_data_filtering_profiles) | **GET** /data-filtering-profiles | List Data Filtering Profiles
[**update_data_filtering_profiles_by_id**](DataFilteringApi.md#update_data_filtering_profiles_by_id) | **PUT** /data-filtering-profiles/{id} | Update Data Filtering Profile by ID


# **create_data_filtering_profiles**
> DataFilteringProfiles create_data_filtering_profiles(data_filtering_profiles)

Create Data Filtering Profile

Create Data Filtering Profile

### Example

* Bearer (JWT) Authentication (scmToken):

```python
import scm.security_services
from scm.security_services.models.data_filtering_profiles import DataFilteringProfiles
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
    api_instance = scm.security_services.DataFilteringApi(api_client)
    data_filtering_profiles = scm.security_services.DataFilteringProfiles() # DataFilteringProfiles | 

    try:
        # Create Data Filtering Profile
        api_response = api_instance.create_data_filtering_profiles(data_filtering_profiles)
        print("The response of DataFilteringApi->create_data_filtering_profiles:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DataFilteringApi->create_data_filtering_profiles: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data_filtering_profiles** | [**DataFilteringProfiles**](DataFilteringProfiles.md)|  | 

### Return type

[**DataFilteringProfiles**](DataFilteringProfiles.md)

### Authorization

[scmToken](../README.md#scmToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**409** | Conflict |  -  |
**0** | General Errors |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_data_filtering_profiles_by_id**
> delete_data_filtering_profiles_by_id(id)

Delete Data Filtering Profile by ID

Delete Data Filtering Profile by ID

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
    api_instance = scm.security_services.DataFilteringApi(api_client)
    id = 'id_example' # str | 

    try:
        # Delete Data Filtering Profile by ID
        api_instance.delete_data_filtering_profiles_by_id(id)
    except Exception as e:
        print("Exception when calling DataFilteringApi->delete_data_filtering_profiles_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

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

# **get_data_filtering_profiles_by_id**
> DataFilteringProfiles get_data_filtering_profiles_by_id(id)

Get Data Filtering Profile by ID

Get Data Filtering Profile by ID

### Example

* Bearer (JWT) Authentication (scmToken):

```python
import scm.security_services
from scm.security_services.models.data_filtering_profiles import DataFilteringProfiles
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
    api_instance = scm.security_services.DataFilteringApi(api_client)
    id = 'id_example' # str | 

    try:
        # Get Data Filtering Profile by ID
        api_response = api_instance.get_data_filtering_profiles_by_id(id)
        print("The response of DataFilteringApi->get_data_filtering_profiles_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DataFilteringApi->get_data_filtering_profiles_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**DataFilteringProfiles**](DataFilteringProfiles.md)

### Authorization

[scmToken](../README.md#scmToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**0** | General Errors |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_data_filtering_profiles**
> DataFilteringProfilesListResponse list_data_filtering_profiles(name=name, folder=folder, snippet=snippet, device=device, offset=offset, limit=limit)

List Data Filtering Profiles

List Data Filtering Profiles

### Example

* Bearer (JWT) Authentication (scmToken):

```python
import scm.security_services
from scm.security_services.models.data_filtering_profiles_list_response import DataFilteringProfilesListResponse
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
    api_instance = scm.security_services.DataFilteringApi(api_client)
    name = 'name_example' # str | The name of the configuration resource (optional)
    folder = 'folder_example' # str | The folder in which the resource is defined  (optional)
    snippet = 'snippet_example' # str | The snippet in which the resource is defined  (optional)
    device = 'device_example' # str | The device in which the resource is defined  (optional)
    offset = 0 # int | The offset into the list of results returned (optional) (default to 0)
    limit = 200 # int | The maximum number of results per page (optional) (default to 200)

    try:
        # List Data Filtering Profiles
        api_response = api_instance.list_data_filtering_profiles(name=name, folder=folder, snippet=snippet, device=device, offset=offset, limit=limit)
        print("The response of DataFilteringApi->list_data_filtering_profiles:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DataFilteringApi->list_data_filtering_profiles: %s\n" % e)
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

[**DataFilteringProfilesListResponse**](DataFilteringProfilesListResponse.md)

### Authorization

[scmToken](../README.md#scmToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**0** | General Errors |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_data_filtering_profiles_by_id**
> DataFilteringProfiles update_data_filtering_profiles_by_id(id, data_filtering_profiles)

Update Data Filtering Profile by ID

Update Data Filtering Profile by ID

### Example

* Bearer (JWT) Authentication (scmToken):

```python
import scm.security_services
from scm.security_services.models.data_filtering_profiles import DataFilteringProfiles
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
    api_instance = scm.security_services.DataFilteringApi(api_client)
    id = 'id_example' # str | 
    data_filtering_profiles = scm.security_services.DataFilteringProfiles() # DataFilteringProfiles | 

    try:
        # Update Data Filtering Profile by ID
        api_response = api_instance.update_data_filtering_profiles_by_id(id, data_filtering_profiles)
        print("The response of DataFilteringApi->update_data_filtering_profiles_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DataFilteringApi->update_data_filtering_profiles_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **data_filtering_profiles** | [**DataFilteringProfiles**](DataFilteringProfiles.md)|  | 

### Return type

[**DataFilteringProfiles**](DataFilteringProfiles.md)

### Authorization

[scmToken](../README.md#scmToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**409** | Conflict |  -  |
**0** | General Errors |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

