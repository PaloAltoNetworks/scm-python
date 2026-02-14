# scm.objects.QuarantinedDevicesApi

All URIs are relative to *https://api.strata.paloaltonetworks.com/config/objects/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_quarantined_devices**](QuarantinedDevicesApi.md#create_quarantined_devices) | **POST** /quarantined-devices | Create a quarantined device
[**delete_quarantined_devices**](QuarantinedDevicesApi.md#delete_quarantined_devices) | **DELETE** /quarantined-devices | Delete a quarantined device
[**list_quarantined_devices**](QuarantinedDevicesApi.md#list_quarantined_devices) | **GET** /quarantined-devices | List quarantined devices


# **create_quarantined_devices**
> QuarantinedDevices create_quarantined_devices(quarantined_devices=quarantined_devices)

Create a quarantined device

Create a new quarantined device. 

### Example

* Bearer (JWT) Authentication (scmToken):

```python
import scm.objects
from scm.objects.models.quarantined_devices import QuarantinedDevices
from scm.objects.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.strata.paloaltonetworks.com/config/objects/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = scm.objects.Configuration(
    host = "https://api.strata.paloaltonetworks.com/config/objects/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): scmToken
configuration = scm.objects.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with scm.objects.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = scm.objects.QuarantinedDevicesApi(api_client)
    quarantined_devices = scm.objects.QuarantinedDevices() # QuarantinedDevices | Created (optional)

    try:
        # Create a quarantined device
        api_response = api_instance.create_quarantined_devices(quarantined_devices=quarantined_devices)
        print("The response of QuarantinedDevicesApi->create_quarantined_devices:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QuarantinedDevicesApi->create_quarantined_devices: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **quarantined_devices** | [**QuarantinedDevices**](QuarantinedDevices.md)| Created | [optional] 

### Return type

[**QuarantinedDevices**](QuarantinedDevices.md)

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

# **delete_quarantined_devices**
> delete_quarantined_devices(host_id)

Delete a quarantined device

Delete a quarantined device. 

### Example

* Bearer (JWT) Authentication (scmToken):

```python
import scm.objects
from scm.objects.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.strata.paloaltonetworks.com/config/objects/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = scm.objects.Configuration(
    host = "https://api.strata.paloaltonetworks.com/config/objects/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): scmToken
configuration = scm.objects.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with scm.objects.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = scm.objects.QuarantinedDevicesApi(api_client)
    host_id = 'host_id_example' # str | Device host ID 

    try:
        # Delete a quarantined device
        api_instance.delete_quarantined_devices(host_id)
    except Exception as e:
        print("Exception when calling QuarantinedDevicesApi->delete_quarantined_devices: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **host_id** | **str**| Device host ID  | 

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

# **list_quarantined_devices**
> List[QuarantinedDevices] list_quarantined_devices(host_id=host_id, serial_number=serial_number)

List quarantined devices

Retrieve a list of quarantined devices 

### Example

* Bearer (JWT) Authentication (scmToken):

```python
import scm.objects
from scm.objects.models.quarantined_devices import QuarantinedDevices
from scm.objects.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.strata.paloaltonetworks.com/config/objects/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = scm.objects.Configuration(
    host = "https://api.strata.paloaltonetworks.com/config/objects/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): scmToken
configuration = scm.objects.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with scm.objects.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = scm.objects.QuarantinedDevicesApi(api_client)
    host_id = 'host_id_example' # str | Device host ID  (optional)
    serial_number = 'serial_number_example' # str | Device serial number  (optional)

    try:
        # List quarantined devices
        api_response = api_instance.list_quarantined_devices(host_id=host_id, serial_number=serial_number)
        print("The response of QuarantinedDevicesApi->list_quarantined_devices:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QuarantinedDevicesApi->list_quarantined_devices: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **host_id** | **str**| Device host ID  | [optional] 
 **serial_number** | **str**| Device serial number  | [optional] 

### Return type

[**List[QuarantinedDevices]**](QuarantinedDevices.md)

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

