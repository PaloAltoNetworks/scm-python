# scm.ztna_connector_all.ConnectorApi

All URIs are relative to *https://api.sase.paloaltonetworks.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_connectors**](ConnectorApi.md#create_connectors) | **POST** /sse/connector/v2.0/api/connectors | Create Connector
[**create_connectors_pcaps_by_id**](ConnectorApi.md#create_connectors_pcaps_by_id) | **POST** /sse/connector/v2.0/api/connectors/{oid}/pcaps | Start Connector Packet Capture
[**create_connectors_scheduled_upgrade_by_id**](ConnectorApi.md#create_connectors_scheduled_upgrade_by_id) | **POST** /sse/connector/v2.0/api/connectors/{oid}/scheduled-upgrade | Create Connector Scheduled Upgrade
[**create_connectors_tech_support_files_by_id**](ConnectorApi.md#create_connectors_tech_support_files_by_id) | **POST** /sse/connector/v2.0/api/connectors/{oid}/tech-support-files | Start Connector Tech Support Generation
[**delete_connectors_by_id**](ConnectorApi.md#delete_connectors_by_id) | **DELETE** /sse/connector/v2.0/api/connectors/{oid} | Delete Connector
[**delete_connectors_scheduled_upgrade_by_id**](ConnectorApi.md#delete_connectors_scheduled_upgrade_by_id) | **DELETE** /sse/connector/v2.0/api/connectors/{oid}/scheduled-upgrade | Delete Connector Scheduled Upgrade
[**download_connectors_pcaps_by_id**](ConnectorApi.md#download_connectors_pcaps_by_id) | **GET** /sse/connector/v2.0/api/connectors/{oid}/pcaps/{id}:download | Download Connector Packet Capture File
[**download_connectors_tech_support_files_by_id**](ConnectorApi.md#download_connectors_tech_support_files_by_id) | **GET** /sse/connector/v2.0/api/connectors/{oid}/tech-support-files/{id}:download | Download Connector Tech Support File
[**get_connectors_by_id**](ConnectorApi.md#get_connectors_by_id) | **GET** /sse/connector/v2.0/api/connectors/{oid} | Get Connector
[**get_connectors_quiesce_by_id**](ConnectorApi.md#get_connectors_quiesce_by_id) | **GET** /sse/connector/v2.0/api/connectors/{oid}/quiesce | Get Connector Quiesce State
[**get_connectors_scheduled_upgrade_by_id**](ConnectorApi.md#get_connectors_scheduled_upgrade_by_id) | **GET** /sse/connector/v2.0/api/connectors/{oid}/scheduled-upgrade | Get Connector Scheduled Upgrade
[**get_connectors_scheduled_upgrade_status_by_id**](ConnectorApi.md#get_connectors_scheduled_upgrade_status_by_id) | **GET** /sse/connector/v2.0/api/connectors/{oid}/scheduled-upgrade-status | Get Connector Scheduled Upgrade Status
[**list_connector_filters**](ConnectorApi.md#list_connector_filters) | **GET** /sse/connector/v2.0/api/connectors/filters | List Connector Filters
[**list_connector_images**](ConnectorApi.md#list_connector_images) | **GET** /sse/connector/v2.0/api/connector-images | List Connector Image Versions
[**list_connectors**](ConnectorApi.md#list_connectors) | **GET** /sse/connector/v2.0/api/connectors | List Connectors
[**list_connectors_pcaps_by_id**](ConnectorApi.md#list_connectors_pcaps_by_id) | **GET** /sse/connector/v2.0/api/connectors/{oid}/pcaps | List Connector Packet Capture Files
[**list_connectors_tech_support_files_by_id**](ConnectorApi.md#list_connectors_tech_support_files_by_id) | **GET** /sse/connector/v2.0/api/connectors/{oid}/tech-support-files | List Connector Tech Support Files
[**stop_connectors_pcaps_by_id**](ConnectorApi.md#stop_connectors_pcaps_by_id) | **POST** /sse/connector/v2.0/api/connectors/{oid}/pcaps/{id}:stop | Stop Connector Packet Capture
[**stop_connectors_tech_support_files_by_id**](ConnectorApi.md#stop_connectors_tech_support_files_by_id) | **POST** /sse/connector/v2.0/api/connectors/{oid}/tech-support-files/{id}:stop | Stop Connector Tech Support Generation
[**update_connectors_by_id**](ConnectorApi.md#update_connectors_by_id) | **PUT** /sse/connector/v2.0/api/connectors/{oid} | Update Connector
[**update_connectors_quiesce_by_id**](ConnectorApi.md#update_connectors_quiesce_by_id) | **PUT** /sse/connector/v2.0/api/connectors/{oid}/quiesce | Update Connector Quiesce State
[**update_connectors_scheduled_upgrade_by_id**](ConnectorApi.md#update_connectors_scheduled_upgrade_by_id) | **PUT** /sse/connector/v2.0/api/connectors/{oid}/scheduled-upgrade | Update Connector Scheduled Upgrade


# **create_connectors**
> create_connectors(connectors, x_panw_region=x_panw_region)

Create Connector

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import scm.ztna_connector_all
from scm.ztna_connector_all.models.connectors import Connectors
from scm.ztna_connector_all.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.sase.paloaltonetworks.com
# See configuration.py for a list of all supported configuration parameters.
configuration = scm.ztna_connector_all.Configuration(
    host = "https://api.sase.paloaltonetworks.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = scm.ztna_connector_all.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with scm.ztna_connector_all.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = scm.ztna_connector_all.ConnectorApi(api_client)
    connectors = scm.ztna_connector_all.Connectors() # Connectors | 
    x_panw_region = 'x_panw_region_example' # str | The region of the tenant (optional)

    try:
        # Create Connector
        api_instance.create_connectors(connectors, x_panw_region=x_panw_region)
    except Exception as e:
        print("Exception when calling ConnectorApi->create_connectors: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **connectors** | [**Connectors**](Connectors.md)|  | 
 **x_panw_region** | **str**| The region of the tenant | [optional] 

### Return type

void (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | [201 Created](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/201)  |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**409** | Conflict |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_connectors_pcaps_by_id**
> PacketCapture create_connectors_pcaps_by_id(oid, packet_capture_create)

Start Connector Packet Capture

This API will start a packet capture operation on the ZTNA connector. The Interface information must be provided in the API.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import scm.ztna_connector_all
from scm.ztna_connector_all.models.packet_capture import PacketCapture
from scm.ztna_connector_all.models.packet_capture_create import PacketCaptureCreate
from scm.ztna_connector_all.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.sase.paloaltonetworks.com
# See configuration.py for a list of all supported configuration parameters.
configuration = scm.ztna_connector_all.Configuration(
    host = "https://api.sase.paloaltonetworks.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = scm.ztna_connector_all.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with scm.ztna_connector_all.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = scm.ztna_connector_all.ConnectorApi(api_client)
    oid = 'oid_example' # str | Object ID
    packet_capture_create = scm.ztna_connector_all.PacketCaptureCreate() # PacketCaptureCreate | 

    try:
        # Start Connector Packet Capture
        api_response = api_instance.create_connectors_pcaps_by_id(oid, packet_capture_create)
        print("The response of ConnectorApi->create_connectors_pcaps_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConnectorApi->create_connectors_pcaps_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **oid** | **str**| Object ID | 
 **packet_capture_create** | [**PacketCaptureCreate**](PacketCaptureCreate.md)|  | 

### Return type

[**PacketCapture**](PacketCapture.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_connectors_scheduled_upgrade_by_id**
> create_connectors_scheduled_upgrade_by_id(oid, connector_scheduled_upgrade)

Create Connector Scheduled Upgrade

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import scm.ztna_connector_all
from scm.ztna_connector_all.models.connector_scheduled_upgrade import ConnectorScheduledUpgrade
from scm.ztna_connector_all.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.sase.paloaltonetworks.com
# See configuration.py for a list of all supported configuration parameters.
configuration = scm.ztna_connector_all.Configuration(
    host = "https://api.sase.paloaltonetworks.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = scm.ztna_connector_all.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with scm.ztna_connector_all.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = scm.ztna_connector_all.ConnectorApi(api_client)
    oid = 'oid_example' # str | Object ID
    connector_scheduled_upgrade = scm.ztna_connector_all.ConnectorScheduledUpgrade() # ConnectorScheduledUpgrade | 

    try:
        # Create Connector Scheduled Upgrade
        api_instance.create_connectors_scheduled_upgrade_by_id(oid, connector_scheduled_upgrade)
    except Exception as e:
        print("Exception when calling ConnectorApi->create_connectors_scheduled_upgrade_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **oid** | **str**| Object ID | 
 **connector_scheduled_upgrade** | [**ConnectorScheduledUpgrade**](ConnectorScheduledUpgrade.md)|  | 

### Return type

void (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | [201 Created](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/201)  |  -  |
**400** | Bad Request |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_connectors_tech_support_files_by_id**
> create_connectors_tech_support_files_by_id(oid)

Start Connector Tech Support Generation

This API will start a tech support operation on the ZTNA connector. In the current implementation it uses the \"dump tech-support\" command to generate the data.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import scm.ztna_connector_all
from scm.ztna_connector_all.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.sase.paloaltonetworks.com
# See configuration.py for a list of all supported configuration parameters.
configuration = scm.ztna_connector_all.Configuration(
    host = "https://api.sase.paloaltonetworks.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = scm.ztna_connector_all.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with scm.ztna_connector_all.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = scm.ztna_connector_all.ConnectorApi(api_client)
    oid = 'oid_example' # str | Object ID

    try:
        # Start Connector Tech Support Generation
        api_instance.create_connectors_tech_support_files_by_id(oid)
    except Exception as e:
        print("Exception when calling ConnectorApi->create_connectors_tech_support_files_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **oid** | **str**| Object ID | 

### Return type

void (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_connectors_by_id**
> delete_connectors_by_id(oid, x_panw_region=x_panw_region)

Delete Connector

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import scm.ztna_connector_all
from scm.ztna_connector_all.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.sase.paloaltonetworks.com
# See configuration.py for a list of all supported configuration parameters.
configuration = scm.ztna_connector_all.Configuration(
    host = "https://api.sase.paloaltonetworks.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = scm.ztna_connector_all.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with scm.ztna_connector_all.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = scm.ztna_connector_all.ConnectorApi(api_client)
    oid = 'oid_example' # str | Object ID
    x_panw_region = 'x_panw_region_example' # str | The region of the tenant (optional)

    try:
        # Delete Connector
        api_instance.delete_connectors_by_id(oid, x_panw_region=x_panw_region)
    except Exception as e:
        print("Exception when calling ConnectorApi->delete_connectors_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **oid** | **str**| Object ID | 
 **x_panw_region** | **str**| The region of the tenant | [optional] 

### Return type

void (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | [202 Accepted](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/202)  |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**409** | Conflict |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_connectors_scheduled_upgrade_by_id**
> delete_connectors_scheduled_upgrade_by_id(oid)

Delete Connector Scheduled Upgrade

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import scm.ztna_connector_all
from scm.ztna_connector_all.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.sase.paloaltonetworks.com
# See configuration.py for a list of all supported configuration parameters.
configuration = scm.ztna_connector_all.Configuration(
    host = "https://api.sase.paloaltonetworks.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = scm.ztna_connector_all.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with scm.ztna_connector_all.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = scm.ztna_connector_all.ConnectorApi(api_client)
    oid = 'oid_example' # str | Object ID

    try:
        # Delete Connector Scheduled Upgrade
        api_instance.delete_connectors_scheduled_upgrade_by_id(oid)
    except Exception as e:
        print("Exception when calling ConnectorApi->delete_connectors_scheduled_upgrade_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **oid** | **str**| Object ID | 

### Return type

void (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | [202 Accepted](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/202)  |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **download_connectors_pcaps_by_id**
> download_connectors_pcaps_by_id(oid, id)

Download Connector Packet Capture File

This API downloads the captured packet file from the ZTNA connector.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import scm.ztna_connector_all
from scm.ztna_connector_all.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.sase.paloaltonetworks.com
# See configuration.py for a list of all supported configuration parameters.
configuration = scm.ztna_connector_all.Configuration(
    host = "https://api.sase.paloaltonetworks.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = scm.ztna_connector_all.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with scm.ztna_connector_all.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = scm.ztna_connector_all.ConnectorApi(api_client)
    oid = 'oid_example' # str | Object ID
    id = 'id_example' # str | request id

    try:
        # Download Connector Packet Capture File
        api_instance.download_connectors_pcaps_by_id(oid, id)
    except Exception as e:
        print("Exception when calling ConnectorApi->download_connectors_pcaps_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **oid** | **str**| Object ID | 
 **id** | **str**| request id | 

### Return type

void (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **download_connectors_tech_support_files_by_id**
> download_connectors_tech_support_files_by_id(oid, id)

Download Connector Tech Support File

This API downloads a tech support file from the ZTNA connector.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import scm.ztna_connector_all
from scm.ztna_connector_all.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.sase.paloaltonetworks.com
# See configuration.py for a list of all supported configuration parameters.
configuration = scm.ztna_connector_all.Configuration(
    host = "https://api.sase.paloaltonetworks.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = scm.ztna_connector_all.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with scm.ztna_connector_all.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = scm.ztna_connector_all.ConnectorApi(api_client)
    oid = 'oid_example' # str | Object ID
    id = 'id_example' # str | request id

    try:
        # Download Connector Tech Support File
        api_instance.download_connectors_tech_support_files_by_id(oid, id)
    except Exception as e:
        print("Exception when calling ConnectorApi->download_connectors_tech_support_files_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **oid** | **str**| Object ID | 
 **id** | **str**| request id | 

### Return type

void (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_connectors_by_id**
> Connectors get_connectors_by_id(oid, x_panw_region=x_panw_region)

Get Connector

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import scm.ztna_connector_all
from scm.ztna_connector_all.models.connectors import Connectors
from scm.ztna_connector_all.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.sase.paloaltonetworks.com
# See configuration.py for a list of all supported configuration parameters.
configuration = scm.ztna_connector_all.Configuration(
    host = "https://api.sase.paloaltonetworks.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = scm.ztna_connector_all.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with scm.ztna_connector_all.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = scm.ztna_connector_all.ConnectorApi(api_client)
    oid = 'oid_example' # str | Object ID
    x_panw_region = 'x_panw_region_example' # str | The region of the tenant (optional)

    try:
        # Get Connector
        api_response = api_instance.get_connectors_by_id(oid, x_panw_region=x_panw_region)
        print("The response of ConnectorApi->get_connectors_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConnectorApi->get_connectors_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **oid** | **str**| Object ID | 
 **x_panw_region** | **str**| The region of the tenant | [optional] 

### Return type

[**Connectors**](Connectors.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_connectors_quiesce_by_id**
> ConnectorQuiesce get_connectors_quiesce_by_id(oid, x_panw_region=x_panw_region)

Get Connector Quiesce State

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import scm.ztna_connector_all
from scm.ztna_connector_all.models.connector_quiesce import ConnectorQuiesce
from scm.ztna_connector_all.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.sase.paloaltonetworks.com
# See configuration.py for a list of all supported configuration parameters.
configuration = scm.ztna_connector_all.Configuration(
    host = "https://api.sase.paloaltonetworks.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = scm.ztna_connector_all.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with scm.ztna_connector_all.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = scm.ztna_connector_all.ConnectorApi(api_client)
    oid = 'oid_example' # str | Object ID
    x_panw_region = 'x_panw_region_example' # str | The region of the tenant (optional)

    try:
        # Get Connector Quiesce State
        api_response = api_instance.get_connectors_quiesce_by_id(oid, x_panw_region=x_panw_region)
        print("The response of ConnectorApi->get_connectors_quiesce_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConnectorApi->get_connectors_quiesce_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **oid** | **str**| Object ID | 
 **x_panw_region** | **str**| The region of the tenant | [optional] 

### Return type

[**ConnectorQuiesce**](ConnectorQuiesce.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |
**424** | Failed Dependency |  -  |
**5XX** | Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_connectors_scheduled_upgrade_by_id**
> ConnectorScheduledUpgrade get_connectors_scheduled_upgrade_by_id(oid)

Get Connector Scheduled Upgrade

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import scm.ztna_connector_all
from scm.ztna_connector_all.models.connector_scheduled_upgrade import ConnectorScheduledUpgrade
from scm.ztna_connector_all.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.sase.paloaltonetworks.com
# See configuration.py for a list of all supported configuration parameters.
configuration = scm.ztna_connector_all.Configuration(
    host = "https://api.sase.paloaltonetworks.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = scm.ztna_connector_all.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with scm.ztna_connector_all.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = scm.ztna_connector_all.ConnectorApi(api_client)
    oid = 'oid_example' # str | Object ID

    try:
        # Get Connector Scheduled Upgrade
        api_response = api_instance.get_connectors_scheduled_upgrade_by_id(oid)
        print("The response of ConnectorApi->get_connectors_scheduled_upgrade_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConnectorApi->get_connectors_scheduled_upgrade_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **oid** | **str**| Object ID | 

### Return type

[**ConnectorScheduledUpgrade**](ConnectorScheduledUpgrade.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_connectors_scheduled_upgrade_status_by_id**
> ConnectorUpgradeStatus get_connectors_scheduled_upgrade_status_by_id(oid, x_panw_region=x_panw_region)

Get Connector Scheduled Upgrade Status

Retrieves the detailed scheduled upgrade status for a specific connector

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import scm.ztna_connector_all
from scm.ztna_connector_all.models.connector_upgrade_status import ConnectorUpgradeStatus
from scm.ztna_connector_all.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.sase.paloaltonetworks.com
# See configuration.py for a list of all supported configuration parameters.
configuration = scm.ztna_connector_all.Configuration(
    host = "https://api.sase.paloaltonetworks.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = scm.ztna_connector_all.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with scm.ztna_connector_all.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = scm.ztna_connector_all.ConnectorApi(api_client)
    oid = 'oid_example' # str | Object ID
    x_panw_region = 'x_panw_region_example' # str | The region of the tenant (optional)

    try:
        # Get Connector Scheduled Upgrade Status
        api_response = api_instance.get_connectors_scheduled_upgrade_status_by_id(oid, x_panw_region=x_panw_region)
        print("The response of ConnectorApi->get_connectors_scheduled_upgrade_status_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConnectorApi->get_connectors_scheduled_upgrade_status_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **oid** | **str**| Object ID | 
 **x_panw_region** | **str**| The region of the tenant | [optional] 

### Return type

[**ConnectorUpgradeStatus**](ConnectorUpgradeStatus.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |
**5XX** | Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_connector_filters**
> List[str] list_connector_filters(x_panw_region=x_panw_region, var_field=var_field, search=search)

List Connector Filters

Get filter values for connector fields. 

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import scm.ztna_connector_all
from scm.ztna_connector_all.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.sase.paloaltonetworks.com
# See configuration.py for a list of all supported configuration parameters.
configuration = scm.ztna_connector_all.Configuration(
    host = "https://api.sase.paloaltonetworks.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = scm.ztna_connector_all.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with scm.ztna_connector_all.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = scm.ztna_connector_all.ConnectorApi(api_client)
    x_panw_region = 'x_panw_region_example' # str | The region of the tenant (optional)
    var_field = 'connector_group' # str | String that represents a static filter field. Call any of the /filters endpoints without specifying a field to get a list of all available fields. (optional)
    search = 'connector1' # str | String to filter list results by. Is searched over multiple fields in each object. Multiple searches can be specified. (optional)

    try:
        # List Connector Filters
        api_response = api_instance.list_connector_filters(x_panw_region=x_panw_region, var_field=var_field, search=search)
        print("The response of ConnectorApi->list_connector_filters:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConnectorApi->list_connector_filters: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_panw_region** | **str**| The region of the tenant | [optional] 
 **var_field** | **str**| String that represents a static filter field. Call any of the /filters endpoints without specifying a field to get a list of all available fields. | [optional] 
 **search** | **str**| String to filter list results by. Is searched over multiple fields in each object. Multiple searches can be specified. | [optional] 

### Return type

**List[str]**

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_connector_images**
> ConnectorImagesListResponse list_connector_images(offset=offset, limit=limit)

List Connector Image Versions

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import scm.ztna_connector_all
from scm.ztna_connector_all.models.connector_images_list_response import ConnectorImagesListResponse
from scm.ztna_connector_all.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.sase.paloaltonetworks.com
# See configuration.py for a list of all supported configuration parameters.
configuration = scm.ztna_connector_all.Configuration(
    host = "https://api.sase.paloaltonetworks.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = scm.ztna_connector_all.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with scm.ztna_connector_all.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = scm.ztna_connector_all.ConnectorApi(api_client)
    offset = 56 # int | A 0-based offset into the collection. It is the index of the starting entry of the page  (optional)
    limit = 56 # int | The max count in result entry (count per page) (optional)

    try:
        # List Connector Image Versions
        api_response = api_instance.list_connector_images(offset=offset, limit=limit)
        print("The response of ConnectorApi->list_connector_images:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConnectorApi->list_connector_images: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **offset** | **int**| A 0-based offset into the collection. It is the index of the starting entry of the page  | [optional] 
 **limit** | **int**| The max count in result entry (count per page) | [optional] 

### Return type

[**ConnectorImagesListResponse**](ConnectorImagesListResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_connectors**
> ConnectorsListResponse list_connectors(x_panw_region=x_panw_region, offset=offset, limit=limit, sort=sort, search=search, filters=filters)

List Connectors

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import scm.ztna_connector_all
from scm.ztna_connector_all.models.connectors_list_response import ConnectorsListResponse
from scm.ztna_connector_all.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.sase.paloaltonetworks.com
# See configuration.py for a list of all supported configuration parameters.
configuration = scm.ztna_connector_all.Configuration(
    host = "https://api.sase.paloaltonetworks.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = scm.ztna_connector_all.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with scm.ztna_connector_all.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = scm.ztna_connector_all.ConnectorApi(api_client)
    x_panw_region = 'x_panw_region_example' # str | The region of the tenant (optional)
    offset = 56 # int | A 0-based offset into the collection. It is the index of the starting entry of the page  (optional)
    limit = 56 # int | The max count in result entry (count per page) (optional)
    sort = 'A[asc],B[desc],C' # str | List of fields from item response to sort by. (optional)
    search = 'connector1' # str | String to filter list results by. Is searched over multiple fields in each object. Multiple searches can be specified. (optional)
    filters = '{\"field\":\"name\",\"search\":\"abc\"}' # str | String to filter list results by searching one specified field of an object. Multiple filters can be specified. (optional)

    try:
        # List Connectors
        api_response = api_instance.list_connectors(x_panw_region=x_panw_region, offset=offset, limit=limit, sort=sort, search=search, filters=filters)
        print("The response of ConnectorApi->list_connectors:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConnectorApi->list_connectors: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_panw_region** | **str**| The region of the tenant | [optional] 
 **offset** | **int**| A 0-based offset into the collection. It is the index of the starting entry of the page  | [optional] 
 **limit** | **int**| The max count in result entry (count per page) | [optional] 
 **sort** | **str**| List of fields from item response to sort by. | [optional] 
 **search** | **str**| String to filter list results by. Is searched over multiple fields in each object. Multiple searches can be specified. | [optional] 
 **filters** | **str**| String to filter list results by searching one specified field of an object. Multiple filters can be specified. | [optional] 

### Return type

[**ConnectorsListResponse**](ConnectorsListResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_connectors_pcaps_by_id**
> DiagnosticFileList list_connectors_pcaps_by_id(oid)

List Connector Packet Capture Files

This API is used to get the list of captured packet files on the ZTNA connector. The result is an array of file information objects. Each file information object has id, state, date, name and size of the file.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import scm.ztna_connector_all
from scm.ztna_connector_all.models.diagnostic_file_list import DiagnosticFileList
from scm.ztna_connector_all.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.sase.paloaltonetworks.com
# See configuration.py for a list of all supported configuration parameters.
configuration = scm.ztna_connector_all.Configuration(
    host = "https://api.sase.paloaltonetworks.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = scm.ztna_connector_all.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with scm.ztna_connector_all.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = scm.ztna_connector_all.ConnectorApi(api_client)
    oid = 'oid_example' # str | Object ID

    try:
        # List Connector Packet Capture Files
        api_response = api_instance.list_connectors_pcaps_by_id(oid)
        print("The response of ConnectorApi->list_connectors_pcaps_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConnectorApi->list_connectors_pcaps_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **oid** | **str**| Object ID | 

### Return type

[**DiagnosticFileList**](DiagnosticFileList.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_connectors_tech_support_files_by_id**
> DiagnosticFileList list_connectors_tech_support_files_by_id(oid)

List Connector Tech Support Files

This API is used to get the list the available \"dump tech-support\" data files on the ZTNA connector. The result is an array of file information objects. Each file information object has id, state, date, name and size of the file.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import scm.ztna_connector_all
from scm.ztna_connector_all.models.diagnostic_file_list import DiagnosticFileList
from scm.ztna_connector_all.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.sase.paloaltonetworks.com
# See configuration.py for a list of all supported configuration parameters.
configuration = scm.ztna_connector_all.Configuration(
    host = "https://api.sase.paloaltonetworks.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = scm.ztna_connector_all.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with scm.ztna_connector_all.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = scm.ztna_connector_all.ConnectorApi(api_client)
    oid = 'oid_example' # str | Object ID

    try:
        # List Connector Tech Support Files
        api_response = api_instance.list_connectors_tech_support_files_by_id(oid)
        print("The response of ConnectorApi->list_connectors_tech_support_files_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConnectorApi->list_connectors_tech_support_files_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **oid** | **str**| Object ID | 

### Return type

[**DiagnosticFileList**](DiagnosticFileList.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stop_connectors_pcaps_by_id**
> PacketCapture stop_connectors_pcaps_by_id(oid, id)

Stop Connector Packet Capture

This API will stop an in-progress packet capture operation on the ZTNA connector.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import scm.ztna_connector_all
from scm.ztna_connector_all.models.packet_capture import PacketCapture
from scm.ztna_connector_all.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.sase.paloaltonetworks.com
# See configuration.py for a list of all supported configuration parameters.
configuration = scm.ztna_connector_all.Configuration(
    host = "https://api.sase.paloaltonetworks.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = scm.ztna_connector_all.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with scm.ztna_connector_all.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = scm.ztna_connector_all.ConnectorApi(api_client)
    oid = 'oid_example' # str | Object ID
    id = 'id_example' # str | request id

    try:
        # Stop Connector Packet Capture
        api_response = api_instance.stop_connectors_pcaps_by_id(oid, id)
        print("The response of ConnectorApi->stop_connectors_pcaps_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConnectorApi->stop_connectors_pcaps_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **oid** | **str**| Object ID | 
 **id** | **str**| request id | 

### Return type

[**PacketCapture**](PacketCapture.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stop_connectors_tech_support_files_by_id**
> stop_connectors_tech_support_files_by_id(oid, id)

Stop Connector Tech Support Generation

This API will stop an in-progress tech support operation on the ZTNA connector.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import scm.ztna_connector_all
from scm.ztna_connector_all.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.sase.paloaltonetworks.com
# See configuration.py for a list of all supported configuration parameters.
configuration = scm.ztna_connector_all.Configuration(
    host = "https://api.sase.paloaltonetworks.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = scm.ztna_connector_all.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with scm.ztna_connector_all.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = scm.ztna_connector_all.ConnectorApi(api_client)
    oid = 'oid_example' # str | Object ID
    id = 'id_example' # str | request id

    try:
        # Stop Connector Tech Support Generation
        api_instance.stop_connectors_tech_support_files_by_id(oid, id)
    except Exception as e:
        print("Exception when calling ConnectorApi->stop_connectors_tech_support_files_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **oid** | **str**| Object ID | 
 **id** | **str**| request id | 

### Return type

void (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_connectors_by_id**
> update_connectors_by_id(oid, connectors, x_panw_region=x_panw_region)

Update Connector

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import scm.ztna_connector_all
from scm.ztna_connector_all.models.connectors import Connectors
from scm.ztna_connector_all.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.sase.paloaltonetworks.com
# See configuration.py for a list of all supported configuration parameters.
configuration = scm.ztna_connector_all.Configuration(
    host = "https://api.sase.paloaltonetworks.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = scm.ztna_connector_all.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with scm.ztna_connector_all.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = scm.ztna_connector_all.ConnectorApi(api_client)
    oid = 'oid_example' # str | Object ID
    connectors = scm.ztna_connector_all.Connectors() # Connectors | 
    x_panw_region = 'x_panw_region_example' # str | The region of the tenant (optional)

    try:
        # Update Connector
        api_instance.update_connectors_by_id(oid, connectors, x_panw_region=x_panw_region)
    except Exception as e:
        print("Exception when calling ConnectorApi->update_connectors_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **oid** | **str**| Object ID | 
 **connectors** | [**Connectors**](Connectors.md)|  | 
 **x_panw_region** | **str**| The region of the tenant | [optional] 

### Return type

void (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | [200 OK](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/200)  |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**409** | Conflict |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_connectors_quiesce_by_id**
> update_connectors_quiesce_by_id(oid, connector_quiesce, x_panw_region=x_panw_region)

Update Connector Quiesce State

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import scm.ztna_connector_all
from scm.ztna_connector_all.models.connector_quiesce import ConnectorQuiesce
from scm.ztna_connector_all.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.sase.paloaltonetworks.com
# See configuration.py for a list of all supported configuration parameters.
configuration = scm.ztna_connector_all.Configuration(
    host = "https://api.sase.paloaltonetworks.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = scm.ztna_connector_all.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with scm.ztna_connector_all.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = scm.ztna_connector_all.ConnectorApi(api_client)
    oid = 'oid_example' # str | Object ID
    connector_quiesce = scm.ztna_connector_all.ConnectorQuiesce() # ConnectorQuiesce | 
    x_panw_region = 'x_panw_region_example' # str | The region of the tenant (optional)

    try:
        # Update Connector Quiesce State
        api_instance.update_connectors_quiesce_by_id(oid, connector_quiesce, x_panw_region=x_panw_region)
    except Exception as e:
        print("Exception when calling ConnectorApi->update_connectors_quiesce_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **oid** | **str**| Object ID | 
 **connector_quiesce** | [**ConnectorQuiesce**](ConnectorQuiesce.md)|  | 
 **x_panw_region** | **str**| The region of the tenant | [optional] 

### Return type

void (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | [204 No Content](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/204)  |  -  |
**400** | Bad Request |  -  |
**404** | Not Found |  -  |
**424** | Failed Dependency |  -  |
**5XX** | Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_connectors_scheduled_upgrade_by_id**
> update_connectors_scheduled_upgrade_by_id(oid, connector_scheduled_upgrade)

Update Connector Scheduled Upgrade

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import scm.ztna_connector_all
from scm.ztna_connector_all.models.connector_scheduled_upgrade import ConnectorScheduledUpgrade
from scm.ztna_connector_all.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.sase.paloaltonetworks.com
# See configuration.py for a list of all supported configuration parameters.
configuration = scm.ztna_connector_all.Configuration(
    host = "https://api.sase.paloaltonetworks.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = scm.ztna_connector_all.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with scm.ztna_connector_all.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = scm.ztna_connector_all.ConnectorApi(api_client)
    oid = 'oid_example' # str | Object ID
    connector_scheduled_upgrade = scm.ztna_connector_all.ConnectorScheduledUpgrade() # ConnectorScheduledUpgrade | 

    try:
        # Update Connector Scheduled Upgrade
        api_instance.update_connectors_scheduled_upgrade_by_id(oid, connector_scheduled_upgrade)
    except Exception as e:
        print("Exception when calling ConnectorApi->update_connectors_scheduled_upgrade_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **oid** | **str**| Object ID | 
 **connector_scheduled_upgrade** | [**ConnectorScheduledUpgrade**](ConnectorScheduledUpgrade.md)|  | 

### Return type

void (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | [204 No Content](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/204)  |  -  |
**400** | Bad Request |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

