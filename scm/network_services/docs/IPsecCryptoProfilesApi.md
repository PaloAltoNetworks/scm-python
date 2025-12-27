# scm_network_services.IPsecCryptoProfilesApi

All URIs are relative to *https://api.strata.paloaltonetworks.com/config/network/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_i_psec_crypto_profiles**](IPsecCryptoProfilesApi.md#create_i_psec_crypto_profiles) | **POST** /ipsec-crypto-profiles | Create an IPsec crypto profile
[**delete_i_psec_crypto_profiles_by_id**](IPsecCryptoProfilesApi.md#delete_i_psec_crypto_profiles_by_id) | **DELETE** /ipsec-crypto-profiles/{id} | Delete an IPsec crypto profile
[**get_i_psec_crypto_profiles_by_id**](IPsecCryptoProfilesApi.md#get_i_psec_crypto_profiles_by_id) | **GET** /ipsec-crypto-profiles/{id} | Get an IPsec crypto profile
[**list_i_psec_crypto_profiles**](IPsecCryptoProfilesApi.md#list_i_psec_crypto_profiles) | **GET** /ipsec-crypto-profiles | List IPsec crypto profiles
[**update_i_psec_crypto_profiles_by_id**](IPsecCryptoProfilesApi.md#update_i_psec_crypto_profiles_by_id) | **PUT** /ipsec-crypto-profiles/{id} | Update an IPsec crypto profile


# **create_i_psec_crypto_profiles**
> IpsecCryptoProfiles create_i_psec_crypto_profiles(ipsec_crypto_profiles=ipsec_crypto_profiles)

Create an IPsec crypto profile

Create a new IPsec crypto profile. 

### Example

* Bearer (JWT) Authentication (scmToken):

```python
import scm_network_services
from scm_network_services.models.ipsec_crypto_profiles import IpsecCryptoProfiles
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
    api_instance = scm_network_services.IPsecCryptoProfilesApi(api_client)
    ipsec_crypto_profiles = scm_network_services.IpsecCryptoProfiles() # IpsecCryptoProfiles | Created (optional)

    try:
        # Create an IPsec crypto profile
        api_response = api_instance.create_i_psec_crypto_profiles(ipsec_crypto_profiles=ipsec_crypto_profiles)
        print("The response of IPsecCryptoProfilesApi->create_i_psec_crypto_profiles:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IPsecCryptoProfilesApi->create_i_psec_crypto_profiles: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ipsec_crypto_profiles** | [**IpsecCryptoProfiles**](IpsecCryptoProfiles.md)| Created | [optional] 

### Return type

[**IpsecCryptoProfiles**](IpsecCryptoProfiles.md)

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

# **delete_i_psec_crypto_profiles_by_id**
> delete_i_psec_crypto_profiles_by_id(id)

Delete an IPsec crypto profile

Delete an IPsec crypto profile. 

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
    api_instance = scm_network_services.IPsecCryptoProfilesApi(api_client)
    id = '123e4567-e89b-12d3-a456-426655440000' # str | The UUID of the configuration resource

    try:
        # Delete an IPsec crypto profile
        api_instance.delete_i_psec_crypto_profiles_by_id(id)
    except Exception as e:
        print("Exception when calling IPsecCryptoProfilesApi->delete_i_psec_crypto_profiles_by_id: %s\n" % e)
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

# **get_i_psec_crypto_profiles_by_id**
> IpsecCryptoProfiles get_i_psec_crypto_profiles_by_id(id)

Get an IPsec crypto profile

Get an existing IPsec crypto profile. 

### Example

* Bearer (JWT) Authentication (scmToken):

```python
import scm_network_services
from scm_network_services.models.ipsec_crypto_profiles import IpsecCryptoProfiles
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
    api_instance = scm_network_services.IPsecCryptoProfilesApi(api_client)
    id = '123e4567-e89b-12d3-a456-426655440000' # str | The UUID of the configuration resource

    try:
        # Get an IPsec crypto profile
        api_response = api_instance.get_i_psec_crypto_profiles_by_id(id)
        print("The response of IPsecCryptoProfilesApi->get_i_psec_crypto_profiles_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IPsecCryptoProfilesApi->get_i_psec_crypto_profiles_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The UUID of the configuration resource | 

### Return type

[**IpsecCryptoProfiles**](IpsecCryptoProfiles.md)

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

# **list_i_psec_crypto_profiles**
> IPsecCryptoProfilesListResponse list_i_psec_crypto_profiles(name=name, folder=folder, snippet=snippet, device=device, offset=offset, limit=limit)

List IPsec crypto profiles

Retrieve a list of IPsec crypto profiles. 

### Example

* Bearer (JWT) Authentication (scmToken):

```python
import scm_network_services
from scm_network_services.models.i_psec_crypto_profiles_list_response import IPsecCryptoProfilesListResponse
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
    api_instance = scm_network_services.IPsecCryptoProfilesApi(api_client)
    name = 'name_example' # str | The name of the configuration resource (optional)
    folder = 'folder_example' # str | The folder in which the resource is defined  (optional)
    snippet = 'snippet_example' # str | The snippet in which the resource is defined  (optional)
    device = 'device_example' # str | The device in which the resource is defined  (optional)
    offset = 0 # int | The offset into the list of results returned (optional) (default to 0)
    limit = 200 # int | The maximum number of results per page (optional) (default to 200)

    try:
        # List IPsec crypto profiles
        api_response = api_instance.list_i_psec_crypto_profiles(name=name, folder=folder, snippet=snippet, device=device, offset=offset, limit=limit)
        print("The response of IPsecCryptoProfilesApi->list_i_psec_crypto_profiles:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IPsecCryptoProfilesApi->list_i_psec_crypto_profiles: %s\n" % e)
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

[**IPsecCryptoProfilesListResponse**](IPsecCryptoProfilesListResponse.md)

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

# **update_i_psec_crypto_profiles_by_id**
> IpsecCryptoProfiles update_i_psec_crypto_profiles_by_id(id, ipsec_crypto_profiles=ipsec_crypto_profiles)

Update an IPsec crypto profile

Update an IPsec crypto profile. 

### Example

* Bearer (JWT) Authentication (scmToken):

```python
import scm_network_services
from scm_network_services.models.ipsec_crypto_profiles import IpsecCryptoProfiles
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
    api_instance = scm_network_services.IPsecCryptoProfilesApi(api_client)
    id = '123e4567-e89b-12d3-a456-426655440000' # str | The UUID of the configuration resource
    ipsec_crypto_profiles = scm_network_services.IpsecCryptoProfiles() # IpsecCryptoProfiles | OK (optional)

    try:
        # Update an IPsec crypto profile
        api_response = api_instance.update_i_psec_crypto_profiles_by_id(id, ipsec_crypto_profiles=ipsec_crypto_profiles)
        print("The response of IPsecCryptoProfilesApi->update_i_psec_crypto_profiles_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IPsecCryptoProfilesApi->update_i_psec_crypto_profiles_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The UUID of the configuration resource | 
 **ipsec_crypto_profiles** | [**IpsecCryptoProfiles**](IpsecCryptoProfiles.md)| OK | [optional] 

### Return type

[**IpsecCryptoProfiles**](IpsecCryptoProfiles.md)

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

