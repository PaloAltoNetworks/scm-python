# scm_device_settings.VPNSettingsApi

All URIs are relative to *https://api.strata.paloaltonetworks.com/config/device/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_vpn_settings**](VPNSettingsApi.md#create_vpn_settings) | **POST** /vpn-settings | Create VPN settings
[**delete_vpn_settings_by_id**](VPNSettingsApi.md#delete_vpn_settings_by_id) | **DELETE** /vpn-settings/{id} | Delete VPN settings
[**get_vpn_settings_by_id**](VPNSettingsApi.md#get_vpn_settings_by_id) | **GET** /vpn-settings/{id} | Get existing VPN settings
[**list_vpn_settings**](VPNSettingsApi.md#list_vpn_settings) | **GET** /vpn-settings | List VPN settings
[**update_vpn_settings_by_id**](VPNSettingsApi.md#update_vpn_settings_by_id) | **PUT** /vpn-settings/{id} | Update VPN settings


# **create_vpn_settings**
> VpnSettings create_vpn_settings(vpn_settings=vpn_settings)

Create VPN settings

Create new VPN settings. 

### Example

* Bearer (JWT) Authentication (scmToken):

```python
import scm_device_settings
from scm_device_settings.models.vpn_settings import VpnSettings
from scm_device_settings.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.strata.paloaltonetworks.com/config/device/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = scm_device_settings.Configuration(
    host = "https://api.strata.paloaltonetworks.com/config/device/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): scmToken
configuration = scm_device_settings.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with scm_device_settings.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = scm_device_settings.VPNSettingsApi(api_client)
    vpn_settings = scm_device_settings.VpnSettings() # VpnSettings |  (optional)

    try:
        # Create VPN settings
        api_response = api_instance.create_vpn_settings(vpn_settings=vpn_settings)
        print("The response of VPNSettingsApi->create_vpn_settings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VPNSettingsApi->create_vpn_settings: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vpn_settings** | [**VpnSettings**](VpnSettings.md)|  | [optional] 

### Return type

[**VpnSettings**](VpnSettings.md)

### Authorization

[scmToken](../README.md#scmToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**409** | Conflict |  -  |
**0** | General Errors |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_vpn_settings_by_id**
> delete_vpn_settings_by_id(id)

Delete VPN settings

Delete the VPN settings. 

### Example

* Bearer (JWT) Authentication (scmToken):

```python
import scm_device_settings
from scm_device_settings.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.strata.paloaltonetworks.com/config/device/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = scm_device_settings.Configuration(
    host = "https://api.strata.paloaltonetworks.com/config/device/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): scmToken
configuration = scm_device_settings.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with scm_device_settings.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = scm_device_settings.VPNSettingsApi(api_client)
    id = '123e4567-e89b-12d3-a456-426655440000' # str | The UUID of the configuration resource

    try:
        # Delete VPN settings
        api_instance.delete_vpn_settings_by_id(id)
    except Exception as e:
        print("Exception when calling VPNSettingsApi->delete_vpn_settings_by_id: %s\n" % e)
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

# **get_vpn_settings_by_id**
> VpnSettings get_vpn_settings_by_id(id)

Get existing VPN settings

Retrieve existing VPN settings. 

### Example

* Bearer (JWT) Authentication (scmToken):

```python
import scm_device_settings
from scm_device_settings.models.vpn_settings import VpnSettings
from scm_device_settings.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.strata.paloaltonetworks.com/config/device/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = scm_device_settings.Configuration(
    host = "https://api.strata.paloaltonetworks.com/config/device/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): scmToken
configuration = scm_device_settings.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with scm_device_settings.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = scm_device_settings.VPNSettingsApi(api_client)
    id = '123e4567-e89b-12d3-a456-426655440000' # str | The UUID of the configuration resource

    try:
        # Get existing VPN settings
        api_response = api_instance.get_vpn_settings_by_id(id)
        print("The response of VPNSettingsApi->get_vpn_settings_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VPNSettingsApi->get_vpn_settings_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The UUID of the configuration resource | 

### Return type

[**VpnSettings**](VpnSettings.md)

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

# **list_vpn_settings**
> List[VpnSettings] list_vpn_settings(folder=folder, snippet=snippet, device=device)

List VPN settings

Retrieve a list of VPN settings. 

### Example

* Bearer (JWT) Authentication (scmToken):

```python
import scm_device_settings
from scm_device_settings.models.vpn_settings import VpnSettings
from scm_device_settings.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.strata.paloaltonetworks.com/config/device/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = scm_device_settings.Configuration(
    host = "https://api.strata.paloaltonetworks.com/config/device/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): scmToken
configuration = scm_device_settings.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with scm_device_settings.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = scm_device_settings.VPNSettingsApi(api_client)
    folder = 'folder_example' # str | The folder in which the resource is defined  (optional)
    snippet = 'snippet_example' # str | The snippet in which the resource is defined  (optional)
    device = 'device_example' # str | The device in which the resource is defined  (optional)

    try:
        # List VPN settings
        api_response = api_instance.list_vpn_settings(folder=folder, snippet=snippet, device=device)
        print("The response of VPNSettingsApi->list_vpn_settings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VPNSettingsApi->list_vpn_settings: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **folder** | **str**| The folder in which the resource is defined  | [optional] 
 **snippet** | **str**| The snippet in which the resource is defined  | [optional] 
 **device** | **str**| The device in which the resource is defined  | [optional] 

### Return type

[**List[VpnSettings]**](VpnSettings.md)

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

# **update_vpn_settings_by_id**
> VpnSettings update_vpn_settings_by_id(id, vpn_settings=vpn_settings)

Update VPN settings

Update the VPN settings. 

### Example

* Bearer (JWT) Authentication (scmToken):

```python
import scm_device_settings
from scm_device_settings.models.vpn_settings import VpnSettings
from scm_device_settings.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.strata.paloaltonetworks.com/config/device/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = scm_device_settings.Configuration(
    host = "https://api.strata.paloaltonetworks.com/config/device/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): scmToken
configuration = scm_device_settings.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with scm_device_settings.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = scm_device_settings.VPNSettingsApi(api_client)
    id = '123e4567-e89b-12d3-a456-426655440000' # str | The UUID of the configuration resource
    vpn_settings = scm_device_settings.VpnSettings() # VpnSettings | OK (optional)

    try:
        # Update VPN settings
        api_response = api_instance.update_vpn_settings_by_id(id, vpn_settings=vpn_settings)
        print("The response of VPNSettingsApi->update_vpn_settings_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VPNSettingsApi->update_vpn_settings_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The UUID of the configuration resource | 
 **vpn_settings** | [**VpnSettings**](VpnSettings.md)| OK | [optional] 

### Return type

[**VpnSettings**](VpnSettings.md)

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

