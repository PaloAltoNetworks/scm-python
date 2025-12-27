# scm.security_services.DNSSecurityProfilesApi

All URIs are relative to *https://api.strata.paloaltonetworks.com/config/security/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_dns_security_profiles**](DNSSecurityProfilesApi.md#create_dns_security_profiles) | **POST** /dns-security-profiles | Create a DNS security profile
[**delete_dns_security_profiles_by_id**](DNSSecurityProfilesApi.md#delete_dns_security_profiles_by_id) | **DELETE** /dns-security-profiles/{id} | Delete a DNS security profile
[**get_dns_security_profiles_by_id**](DNSSecurityProfilesApi.md#get_dns_security_profiles_by_id) | **GET** /dns-security-profiles/{id} | Get a DNS security profile
[**list_dns_security_profiles**](DNSSecurityProfilesApi.md#list_dns_security_profiles) | **GET** /dns-security-profiles | List DNS security profiles
[**update_dns_security_profiles_by_id**](DNSSecurityProfilesApi.md#update_dns_security_profiles_by_id) | **PUT** /dns-security-profiles/{id} | Update a DNS security profile


# **create_dns_security_profiles**
> DnsSecurityProfiles create_dns_security_profiles(dns_security_profiles=dns_security_profiles)

Create a DNS security profile

Create a new DNS security profile. 

### Example

* Bearer (JWT) Authentication (scmToken):

```python
import scm.security_services
from scm.security_services.models.dns_security_profiles import DnsSecurityProfiles
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
    api_instance = scm.security_services.DNSSecurityProfilesApi(api_client)
    dns_security_profiles = scm.security_services.DnsSecurityProfiles() # DnsSecurityProfiles | Created (optional)

    try:
        # Create a DNS security profile
        api_response = api_instance.create_dns_security_profiles(dns_security_profiles=dns_security_profiles)
        print("The response of DNSSecurityProfilesApi->create_dns_security_profiles:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DNSSecurityProfilesApi->create_dns_security_profiles: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dns_security_profiles** | [**DnsSecurityProfiles**](DnsSecurityProfiles.md)| Created | [optional] 

### Return type

[**DnsSecurityProfiles**](DnsSecurityProfiles.md)

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

# **delete_dns_security_profiles_by_id**
> delete_dns_security_profiles_by_id(id)

Delete a DNS security profile

Delete a DNS security profile. 

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
    api_instance = scm.security_services.DNSSecurityProfilesApi(api_client)
    id = '123e4567-e89b-12d3-a456-426655440000' # str | The UUID of the configuration resource

    try:
        # Delete a DNS security profile
        api_instance.delete_dns_security_profiles_by_id(id)
    except Exception as e:
        print("Exception when calling DNSSecurityProfilesApi->delete_dns_security_profiles_by_id: %s\n" % e)
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

# **get_dns_security_profiles_by_id**
> DnsSecurityProfiles get_dns_security_profiles_by_id(id)

Get a DNS security profile

Get an existing DNS security profile. 

### Example

* Bearer (JWT) Authentication (scmToken):

```python
import scm.security_services
from scm.security_services.models.dns_security_profiles import DnsSecurityProfiles
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
    api_instance = scm.security_services.DNSSecurityProfilesApi(api_client)
    id = '123e4567-e89b-12d3-a456-426655440000' # str | The UUID of the configuration resource

    try:
        # Get a DNS security profile
        api_response = api_instance.get_dns_security_profiles_by_id(id)
        print("The response of DNSSecurityProfilesApi->get_dns_security_profiles_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DNSSecurityProfilesApi->get_dns_security_profiles_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The UUID of the configuration resource | 

### Return type

[**DnsSecurityProfiles**](DnsSecurityProfiles.md)

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

# **list_dns_security_profiles**
> DNSSecurityProfilesListResponse list_dns_security_profiles(name=name, folder=folder, snippet=snippet, device=device, offset=offset, limit=limit)

List DNS security profiles

Retrieve a list of DNS security profiles. 

### Example

* Bearer (JWT) Authentication (scmToken):

```python
import scm.security_services
from scm.security_services.models.dns_security_profiles_list_response import DNSSecurityProfilesListResponse
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
    api_instance = scm.security_services.DNSSecurityProfilesApi(api_client)
    name = 'name_example' # str | The name of the configuration resource (optional)
    folder = 'folder_example' # str | The folder in which the resource is defined  (optional)
    snippet = 'snippet_example' # str | The snippet in which the resource is defined  (optional)
    device = 'device_example' # str | The device in which the resource is defined  (optional)
    offset = 0 # int | The offset into the list of results returned (optional) (default to 0)
    limit = 200 # int | The maximum number of results per page (optional) (default to 200)

    try:
        # List DNS security profiles
        api_response = api_instance.list_dns_security_profiles(name=name, folder=folder, snippet=snippet, device=device, offset=offset, limit=limit)
        print("The response of DNSSecurityProfilesApi->list_dns_security_profiles:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DNSSecurityProfilesApi->list_dns_security_profiles: %s\n" % e)
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

[**DNSSecurityProfilesListResponse**](DNSSecurityProfilesListResponse.md)

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

# **update_dns_security_profiles_by_id**
> DnsSecurityProfiles update_dns_security_profiles_by_id(id, dns_security_profiles=dns_security_profiles)

Update a DNS security profile

Update an existing DNS security profile. 

### Example

* Bearer (JWT) Authentication (scmToken):

```python
import scm.security_services
from scm.security_services.models.dns_security_profiles import DnsSecurityProfiles
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
    api_instance = scm.security_services.DNSSecurityProfilesApi(api_client)
    id = '123e4567-e89b-12d3-a456-426655440000' # str | The UUID of the configuration resource
    dns_security_profiles = scm.security_services.DnsSecurityProfiles() # DnsSecurityProfiles | OK (optional)

    try:
        # Update a DNS security profile
        api_response = api_instance.update_dns_security_profiles_by_id(id, dns_security_profiles=dns_security_profiles)
        print("The response of DNSSecurityProfilesApi->update_dns_security_profiles_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DNSSecurityProfilesApi->update_dns_security_profiles_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The UUID of the configuration resource | 
 **dns_security_profiles** | [**DnsSecurityProfiles**](DnsSecurityProfiles.md)| OK | [optional] 

### Return type

[**DnsSecurityProfiles**](DnsSecurityProfiles.md)

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

