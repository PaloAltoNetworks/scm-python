# scm_security_services.WildFireAntiVirusProfilesApi

All URIs are relative to *https://api.strata.paloaltonetworks.com/config/security/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_wild_fire_anti_virus_profiles**](WildFireAntiVirusProfilesApi.md#create_wild_fire_anti_virus_profiles) | **POST** /wildfire-anti-virus-profiles | Create a WildFire and anti-virus profile
[**delete_wild_fire_anti_virus_profiles_by_id**](WildFireAntiVirusProfilesApi.md#delete_wild_fire_anti_virus_profiles_by_id) | **DELETE** /wildfire-anti-virus-profiles/{id} | Delete a WildFire and anti-virus profile
[**get_wild_fire_anti_virus_profiles_by_id**](WildFireAntiVirusProfilesApi.md#get_wild_fire_anti_virus_profiles_by_id) | **GET** /wildfire-anti-virus-profiles/{id} | Get a WildFire and anti-virus profile
[**list_wild_fire_anti_virus_profiles**](WildFireAntiVirusProfilesApi.md#list_wild_fire_anti_virus_profiles) | **GET** /wildfire-anti-virus-profiles | List Wildfire and anti-virus profiles
[**update_wild_fire_anti_virus_profiles_by_id**](WildFireAntiVirusProfilesApi.md#update_wild_fire_anti_virus_profiles_by_id) | **PUT** /wildfire-anti-virus-profiles/{id} | Update a wildfire and antivirus profile


# **create_wild_fire_anti_virus_profiles**
> WildfireAntiVirusProfiles create_wild_fire_anti_virus_profiles(wildfire_anti_virus_profiles=wildfire_anti_virus_profiles)

Create a WildFire and anti-virus profile

Create a new WildFire and anti-virus profile. 

### Example

* Bearer (JWT) Authentication (scmToken):

```python
import scm_security_services
from scm_security_services.models.wildfire_anti_virus_profiles import WildfireAntiVirusProfiles
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
    api_instance = scm_security_services.WildFireAntiVirusProfilesApi(api_client)
    wildfire_anti_virus_profiles = scm_security_services.WildfireAntiVirusProfiles() # WildfireAntiVirusProfiles | Created (optional)

    try:
        # Create a WildFire and anti-virus profile
        api_response = api_instance.create_wild_fire_anti_virus_profiles(wildfire_anti_virus_profiles=wildfire_anti_virus_profiles)
        print("The response of WildFireAntiVirusProfilesApi->create_wild_fire_anti_virus_profiles:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WildFireAntiVirusProfilesApi->create_wild_fire_anti_virus_profiles: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wildfire_anti_virus_profiles** | [**WildfireAntiVirusProfiles**](WildfireAntiVirusProfiles.md)| Created | [optional] 

### Return type

[**WildfireAntiVirusProfiles**](WildfireAntiVirusProfiles.md)

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

# **delete_wild_fire_anti_virus_profiles_by_id**
> delete_wild_fire_anti_virus_profiles_by_id(id)

Delete a WildFire and anti-virus profile

Delete a WildFire and anti-virus profile. 

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
    api_instance = scm_security_services.WildFireAntiVirusProfilesApi(api_client)
    id = '123e4567-e89b-12d3-a456-426655440000' # str | The UUID of the configuration resource

    try:
        # Delete a WildFire and anti-virus profile
        api_instance.delete_wild_fire_anti_virus_profiles_by_id(id)
    except Exception as e:
        print("Exception when calling WildFireAntiVirusProfilesApi->delete_wild_fire_anti_virus_profiles_by_id: %s\n" % e)
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

# **get_wild_fire_anti_virus_profiles_by_id**
> WildfireAntiVirusProfiles get_wild_fire_anti_virus_profiles_by_id(id)

Get a WildFire and anti-virus profile

Get an existing WildFire and anti-virus profile. 

### Example

* Bearer (JWT) Authentication (scmToken):

```python
import scm_security_services
from scm_security_services.models.wildfire_anti_virus_profiles import WildfireAntiVirusProfiles
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
    api_instance = scm_security_services.WildFireAntiVirusProfilesApi(api_client)
    id = '123e4567-e89b-12d3-a456-426655440000' # str | The UUID of the configuration resource

    try:
        # Get a WildFire and anti-virus profile
        api_response = api_instance.get_wild_fire_anti_virus_profiles_by_id(id)
        print("The response of WildFireAntiVirusProfilesApi->get_wild_fire_anti_virus_profiles_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WildFireAntiVirusProfilesApi->get_wild_fire_anti_virus_profiles_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The UUID of the configuration resource | 

### Return type

[**WildfireAntiVirusProfiles**](WildfireAntiVirusProfiles.md)

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

# **list_wild_fire_anti_virus_profiles**
> WildFireAntiVirusProfilesListResponse list_wild_fire_anti_virus_profiles(name=name, folder=folder, snippet=snippet, device=device, offset=offset, limit=limit)

List Wildfire and anti-virus profiles

Retrieve a list of WildFire and anti-virus profiles. 

### Example

* Bearer (JWT) Authentication (scmToken):

```python
import scm_security_services
from scm_security_services.models.wild_fire_anti_virus_profiles_list_response import WildFireAntiVirusProfilesListResponse
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
    api_instance = scm_security_services.WildFireAntiVirusProfilesApi(api_client)
    name = 'name_example' # str | The name of the configuration resource (optional)
    folder = 'folder_example' # str | The folder in which the resource is defined  (optional)
    snippet = 'snippet_example' # str | The snippet in which the resource is defined  (optional)
    device = 'device_example' # str | The device in which the resource is defined  (optional)
    offset = 0 # int | The offset into the list of results returned (optional) (default to 0)
    limit = 200 # int | The maximum number of results per page (optional) (default to 200)

    try:
        # List Wildfire and anti-virus profiles
        api_response = api_instance.list_wild_fire_anti_virus_profiles(name=name, folder=folder, snippet=snippet, device=device, offset=offset, limit=limit)
        print("The response of WildFireAntiVirusProfilesApi->list_wild_fire_anti_virus_profiles:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WildFireAntiVirusProfilesApi->list_wild_fire_anti_virus_profiles: %s\n" % e)
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

[**WildFireAntiVirusProfilesListResponse**](WildFireAntiVirusProfilesListResponse.md)

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

# **update_wild_fire_anti_virus_profiles_by_id**
> WildfireAntiVirusProfiles update_wild_fire_anti_virus_profiles_by_id(id, wildfire_anti_virus_profiles=wildfire_anti_virus_profiles)

Update a wildfire and antivirus profile

Update an existing WildFire and anti-virus profile. 

### Example

* Bearer (JWT) Authentication (scmToken):

```python
import scm_security_services
from scm_security_services.models.wildfire_anti_virus_profiles import WildfireAntiVirusProfiles
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
    api_instance = scm_security_services.WildFireAntiVirusProfilesApi(api_client)
    id = '123e4567-e89b-12d3-a456-426655440000' # str | The UUID of the configuration resource
    wildfire_anti_virus_profiles = scm_security_services.WildfireAntiVirusProfiles() # WildfireAntiVirusProfiles | OK (optional)

    try:
        # Update a wildfire and antivirus profile
        api_response = api_instance.update_wild_fire_anti_virus_profiles_by_id(id, wildfire_anti_virus_profiles=wildfire_anti_virus_profiles)
        print("The response of WildFireAntiVirusProfilesApi->update_wild_fire_anti_virus_profiles_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WildFireAntiVirusProfilesApi->update_wild_fire_anti_virus_profiles_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The UUID of the configuration resource | 
 **wildfire_anti_virus_profiles** | [**WildfireAntiVirusProfiles**](WildfireAntiVirusProfiles.md)| OK | [optional] 

### Return type

[**WildfireAntiVirusProfiles**](WildfireAntiVirusProfiles.md)

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

