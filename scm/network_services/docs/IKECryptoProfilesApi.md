# scm_network_services.IKECryptoProfilesApi

All URIs are relative to *https://api.strata.paloaltonetworks.com/config/network/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_ike_crypto_profiles**](IKECryptoProfilesApi.md#create_ike_crypto_profiles) | **POST** /ike-crypto-profiles | Create an IKE crypto profile
[**delete_ike_crypto_profiles_by_id**](IKECryptoProfilesApi.md#delete_ike_crypto_profiles_by_id) | **DELETE** /ike-crypto-profiles/{id} | Delete an IKE crypto profile
[**get_ike_crypto_profiles_by_id**](IKECryptoProfilesApi.md#get_ike_crypto_profiles_by_id) | **GET** /ike-crypto-profiles/{id} | Get an IKE crypto profile
[**list_ike_crypto_profiles**](IKECryptoProfilesApi.md#list_ike_crypto_profiles) | **GET** /ike-crypto-profiles | List IKE crypto profiles
[**update_ike_crypto_profiles_by_id**](IKECryptoProfilesApi.md#update_ike_crypto_profiles_by_id) | **PUT** /ike-crypto-profiles/{id} | Update an IKE crypto profile


# **create_ike_crypto_profiles**
> IkeCryptoProfiles create_ike_crypto_profiles(ike_crypto_profiles=ike_crypto_profiles)

Create an IKE crypto profile

Create a new IKE crypto profile. 

### Example

* Bearer (JWT) Authentication (scmToken):

```python
import scm_network_services
from scm_network_services.models.ike_crypto_profiles import IkeCryptoProfiles
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
    api_instance = scm_network_services.IKECryptoProfilesApi(api_client)
    ike_crypto_profiles = scm_network_services.IkeCryptoProfiles() # IkeCryptoProfiles | Created (optional)

    try:
        # Create an IKE crypto profile
        api_response = api_instance.create_ike_crypto_profiles(ike_crypto_profiles=ike_crypto_profiles)
        print("The response of IKECryptoProfilesApi->create_ike_crypto_profiles:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IKECryptoProfilesApi->create_ike_crypto_profiles: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ike_crypto_profiles** | [**IkeCryptoProfiles**](IkeCryptoProfiles.md)| Created | [optional] 

### Return type

[**IkeCryptoProfiles**](IkeCryptoProfiles.md)

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

# **delete_ike_crypto_profiles_by_id**
> delete_ike_crypto_profiles_by_id(id)

Delete an IKE crypto profile

Delete an IKE crypto profile. 

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
    api_instance = scm_network_services.IKECryptoProfilesApi(api_client)
    id = '123e4567-e89b-12d3-a456-426655440000' # str | The UUID of the configuration resource

    try:
        # Delete an IKE crypto profile
        api_instance.delete_ike_crypto_profiles_by_id(id)
    except Exception as e:
        print("Exception when calling IKECryptoProfilesApi->delete_ike_crypto_profiles_by_id: %s\n" % e)
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

# **get_ike_crypto_profiles_by_id**
> IkeCryptoProfiles get_ike_crypto_profiles_by_id(id)

Get an IKE crypto profile

Get an existing IKE crypto profile. 

### Example

* Bearer (JWT) Authentication (scmToken):

```python
import scm_network_services
from scm_network_services.models.ike_crypto_profiles import IkeCryptoProfiles
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
    api_instance = scm_network_services.IKECryptoProfilesApi(api_client)
    id = '123e4567-e89b-12d3-a456-426655440000' # str | The UUID of the configuration resource

    try:
        # Get an IKE crypto profile
        api_response = api_instance.get_ike_crypto_profiles_by_id(id)
        print("The response of IKECryptoProfilesApi->get_ike_crypto_profiles_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IKECryptoProfilesApi->get_ike_crypto_profiles_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The UUID of the configuration resource | 

### Return type

[**IkeCryptoProfiles**](IkeCryptoProfiles.md)

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

# **list_ike_crypto_profiles**
> IKECryptoProfilesListResponse list_ike_crypto_profiles(name=name, folder=folder, snippet=snippet, device=device, offset=offset, limit=limit)

List IKE crypto profiles

Retrieve a list of IKE crypto profiles. 

### Example

* Bearer (JWT) Authentication (scmToken):

```python
import scm_network_services
from scm_network_services.models.ike_crypto_profiles_list_response import IKECryptoProfilesListResponse
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
    api_instance = scm_network_services.IKECryptoProfilesApi(api_client)
    name = 'name_example' # str | The name of the configuration resource (optional)
    folder = 'folder_example' # str | The folder in which the resource is defined  (optional)
    snippet = 'snippet_example' # str | The snippet in which the resource is defined  (optional)
    device = 'device_example' # str | The device in which the resource is defined  (optional)
    offset = 0 # int | The offset into the list of results returned (optional) (default to 0)
    limit = 200 # int | The maximum number of results per page (optional) (default to 200)

    try:
        # List IKE crypto profiles
        api_response = api_instance.list_ike_crypto_profiles(name=name, folder=folder, snippet=snippet, device=device, offset=offset, limit=limit)
        print("The response of IKECryptoProfilesApi->list_ike_crypto_profiles:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IKECryptoProfilesApi->list_ike_crypto_profiles: %s\n" % e)
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

[**IKECryptoProfilesListResponse**](IKECryptoProfilesListResponse.md)

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

# **update_ike_crypto_profiles_by_id**
> IkeCryptoProfiles update_ike_crypto_profiles_by_id(id, ike_crypto_profiles=ike_crypto_profiles)

Update an IKE crypto profile

Update an existing IKE crypto profile. 

### Example

* Bearer (JWT) Authentication (scmToken):

```python
import scm_network_services
from scm_network_services.models.ike_crypto_profiles import IkeCryptoProfiles
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
    api_instance = scm_network_services.IKECryptoProfilesApi(api_client)
    id = '123e4567-e89b-12d3-a456-426655440000' # str | The UUID of the configuration resource
    ike_crypto_profiles = scm_network_services.IkeCryptoProfiles() # IkeCryptoProfiles | OK (optional)

    try:
        # Update an IKE crypto profile
        api_response = api_instance.update_ike_crypto_profiles_by_id(id, ike_crypto_profiles=ike_crypto_profiles)
        print("The response of IKECryptoProfilesApi->update_ike_crypto_profiles_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IKECryptoProfilesApi->update_ike_crypto_profiles_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The UUID of the configuration resource | 
 **ike_crypto_profiles** | [**IkeCryptoProfiles**](IkeCryptoProfiles.md)| OK | [optional] 

### Return type

[**IkeCryptoProfiles**](IkeCryptoProfiles.md)

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

