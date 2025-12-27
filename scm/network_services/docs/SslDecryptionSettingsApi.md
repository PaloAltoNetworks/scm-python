# scm_network_services.SslDecryptionSettingsApi

All URIs are relative to *https://api.strata.paloaltonetworks.com/config/network/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_ssl_decryption_settings**](SslDecryptionSettingsApi.md#delete_ssl_decryption_settings) | **DELETE** /ssl-decryption-settings | DELETE Ssl Decryption Settings
[**get_ssl_decryption_settings**](SslDecryptionSettingsApi.md#get_ssl_decryption_settings) | **GET** /ssl-decryption-settings | GET Ssl Decryption Settings
[**post_ssl_decryption_settings**](SslDecryptionSettingsApi.md#post_ssl_decryption_settings) | **POST** /ssl-decryption-settings | POST Ssl Decryption Settings
[**put_ssl_decryption_settings**](SslDecryptionSettingsApi.md#put_ssl_decryption_settings) | **PUT** /ssl-decryption-settings | PUT Ssl Decryption Settings


# **delete_ssl_decryption_settings**
> SslDecryptionSettings delete_ssl_decryption_settings()

DELETE Ssl Decryption Settings

DELETE Ssl Decryption Settings

### Example

* Bearer (JWT) Authentication (scmToken):

```python
import scm_network_services
from scm_network_services.models.ssl_decryption_settings import SslDecryptionSettings
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
    api_instance = scm_network_services.SslDecryptionSettingsApi(api_client)

    try:
        # DELETE Ssl Decryption Settings
        api_response = api_instance.delete_ssl_decryption_settings()
        print("The response of SslDecryptionSettingsApi->delete_ssl_decryption_settings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SslDecryptionSettingsApi->delete_ssl_decryption_settings: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**SslDecryptionSettings**](SslDecryptionSettings.md)

### Authorization

[scmToken](../README.md#scmToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |
**409** |  |  -  |
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_ssl_decryption_settings**
> SslDecryptionSettings get_ssl_decryption_settings(folder=folder, snippet=snippet, device=device, offset=offset, limit=limit)

GET Ssl Decryption Settings

GET Ssl Decryption Settings

### Example

* Bearer (JWT) Authentication (scmToken):

```python
import scm_network_services
from scm_network_services.models.ssl_decryption_settings import SslDecryptionSettings
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
    api_instance = scm_network_services.SslDecryptionSettingsApi(api_client)
    folder = 'folder_example' # str | The folder in which the resource is defined  (optional)
    snippet = 'snippet_example' # str | The snippet in which the resource is defined  (optional)
    device = 'device_example' # str | The device in which the resource is defined  (optional)
    offset = 0 # int | The offset into the list of results returned (optional) (default to 0)
    limit = 200 # int | The maximum number of results per page (optional) (default to 200)

    try:
        # GET Ssl Decryption Settings
        api_response = api_instance.get_ssl_decryption_settings(folder=folder, snippet=snippet, device=device, offset=offset, limit=limit)
        print("The response of SslDecryptionSettingsApi->get_ssl_decryption_settings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SslDecryptionSettingsApi->get_ssl_decryption_settings: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **folder** | **str**| The folder in which the resource is defined  | [optional] 
 **snippet** | **str**| The snippet in which the resource is defined  | [optional] 
 **device** | **str**| The device in which the resource is defined  | [optional] 
 **offset** | **int**| The offset into the list of results returned | [optional] [default to 0]
 **limit** | **int**| The maximum number of results per page | [optional] [default to 200]

### Return type

[**SslDecryptionSettings**](SslDecryptionSettings.md)

### Authorization

[scmToken](../README.md#scmToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** |  |  -  |
**401** |  |  -  |
**403** |  |  -  |
**404** |  |  -  |
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_ssl_decryption_settings**
> SslDecryptionSettings post_ssl_decryption_settings(ssl_decryption_settings)

POST Ssl Decryption Settings

POST Ssl Decryption Settings

### Example

* Bearer (JWT) Authentication (scmToken):

```python
import scm_network_services
from scm_network_services.models.ssl_decryption_settings import SslDecryptionSettings
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
    api_instance = scm_network_services.SslDecryptionSettingsApi(api_client)
    ssl_decryption_settings = scm_network_services.SslDecryptionSettings() # SslDecryptionSettings | 

    try:
        # POST Ssl Decryption Settings
        api_response = api_instance.post_ssl_decryption_settings(ssl_decryption_settings)
        print("The response of SslDecryptionSettingsApi->post_ssl_decryption_settings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SslDecryptionSettingsApi->post_ssl_decryption_settings: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ssl_decryption_settings** | [**SslDecryptionSettings**](SslDecryptionSettings.md)|  | 

### Return type

[**SslDecryptionSettings**](SslDecryptionSettings.md)

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
**409** |  |  -  |
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_ssl_decryption_settings**
> SslDecryptionSettings put_ssl_decryption_settings()

PUT Ssl Decryption Settings

PUT Ssl Decryption Settings

### Example

* Bearer (JWT) Authentication (scmToken):

```python
import scm_network_services
from scm_network_services.models.ssl_decryption_settings import SslDecryptionSettings
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
    api_instance = scm_network_services.SslDecryptionSettingsApi(api_client)

    try:
        # PUT Ssl Decryption Settings
        api_response = api_instance.put_ssl_decryption_settings()
        print("The response of SslDecryptionSettingsApi->put_ssl_decryption_settings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SslDecryptionSettingsApi->put_ssl_decryption_settings: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**SslDecryptionSettings**](SslDecryptionSettings.md)

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
**409** |  |  -  |
**0** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

