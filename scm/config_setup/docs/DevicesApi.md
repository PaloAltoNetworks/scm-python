# scm.config_setup.DevicesApi

All URIs are relative to *https://api.strata.paloaltonetworks.com/config/setup/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_device_by_id**](DevicesApi.md#get_device_by_id) | **GET** /devices/{id} | Get a device
[**list_devices**](DevicesApi.md#list_devices) | **GET** /devices | List devices
[**update_device_by_id**](DevicesApi.md#update_device_by_id) | **PUT** /devices/{id} | Update a device


# **get_device_by_id**
> Devices get_device_by_id(id)

Get a device

Retrieve an existing device. 

### Example

* Bearer (JWT) Authentication (scmToken):

```python
import scm.config_setup
from scm.config_setup.models.devices import Devices
from scm.config_setup.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.strata.paloaltonetworks.com/config/setup/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = scm.config_setup.Configuration(
    host = "https://api.strata.paloaltonetworks.com/config/setup/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): scmToken
configuration = scm.config_setup.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with scm.config_setup.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = scm.config_setup.DevicesApi(api_client)
    id = 'id_example' # str | The UUID of the resource

    try:
        # Get a device
        api_response = api_instance.get_device_by_id(id)
        print("The response of DevicesApi->get_device_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DevicesApi->get_device_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The UUID of the resource | 

### Return type

[**Devices**](Devices.md)

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

# **list_devices**
> DevicesListResponse list_devices(pagination=pagination, limit=limit, offset=offset, name=name)

List devices

Retrieve a list of devices. 

### Example

* Bearer (JWT) Authentication (scmToken):

```python
import scm.config_setup
from scm.config_setup.models.devices_list_response import DevicesListResponse
from scm.config_setup.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.strata.paloaltonetworks.com/config/setup/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = scm.config_setup.Configuration(
    host = "https://api.strata.paloaltonetworks.com/config/setup/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): scmToken
configuration = scm.config_setup.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with scm.config_setup.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = scm.config_setup.DevicesApi(api_client)
    pagination = True # bool | The parameter to mention if the response should be paginated. By default, its set to false (optional)
    limit = 56 # int | The maximum number of resources to return (optional)
    offset = 56 # int | The offset into the list of resources returned (optional)
    name = 'name_example' # str | The name of the resource (optional)

    try:
        # List devices
        api_response = api_instance.list_devices(pagination=pagination, limit=limit, offset=offset, name=name)
        print("The response of DevicesApi->list_devices:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DevicesApi->list_devices: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pagination** | **bool**| The parameter to mention if the response should be paginated. By default, its set to false | [optional] 
 **limit** | **int**| The maximum number of resources to return | [optional] 
 **offset** | **int**| The offset into the list of resources returned | [optional] 
 **name** | **str**| The name of the resource | [optional] 

### Return type

[**DevicesListResponse**](DevicesListResponse.md)

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

# **update_device_by_id**
> Devices update_device_by_id(id, devices_put=devices_put)

Update a device

Update an existing device. 

### Example

* Bearer (JWT) Authentication (scmToken):

```python
import scm.config_setup
from scm.config_setup.models.devices import Devices
from scm.config_setup.models.devices_put import DevicesPut
from scm.config_setup.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.strata.paloaltonetworks.com/config/setup/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = scm.config_setup.Configuration(
    host = "https://api.strata.paloaltonetworks.com/config/setup/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): scmToken
configuration = scm.config_setup.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with scm.config_setup.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = scm.config_setup.DevicesApi(api_client)
    id = 'id_example' # str | The UUID of the resource
    devices_put = scm.config_setup.DevicesPut() # DevicesPut | The `device` resource definition. (optional)

    try:
        # Update a device
        api_response = api_instance.update_device_by_id(id, devices_put=devices_put)
        print("The response of DevicesApi->update_device_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DevicesApi->update_device_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The UUID of the resource | 
 **devices_put** | [**DevicesPut**](DevicesPut.md)| The &#x60;device&#x60; resource definition. | [optional] 

### Return type

[**Devices**](Devices.md)

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

