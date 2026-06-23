# scm.ztna_connector_all.ConnectorGroupApi

All URIs are relative to *https://api.sase.paloaltonetworks.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_connector_group**](ConnectorGroupApi.md#create_connector_group) | **POST** /sse/connector/v2.0/api/connector-groups | Create Connector Group
[**create_connector_group_scheduled_upgrade**](ConnectorGroupApi.md#create_connector_group_scheduled_upgrade) | **POST** /sse/connector/v2.0/api/connector-groups/{oid}/scheduled-upgrade | Create Connector Group Scheduled Upgrade
[**delete_connector_group_by_id**](ConnectorGroupApi.md#delete_connector_group_by_id) | **DELETE** /sse/connector/v2.0/api/connector-groups/{oid} | Delete Connector Group
[**delete_connector_group_scheduled_upgrade**](ConnectorGroupApi.md#delete_connector_group_scheduled_upgrade) | **DELETE** /sse/connector/v2.0/api/connector-groups/{oid}/scheduled-upgrade | Delete Connector Group Scheduled Upgrade
[**get_connector_group_by_id**](ConnectorGroupApi.md#get_connector_group_by_id) | **GET** /sse/connector/v2.0/api/connector-groups/{oid} | Get Connector Group
[**get_connector_group_scheduled_upgrade**](ConnectorGroupApi.md#get_connector_group_scheduled_upgrade) | **GET** /sse/connector/v2.0/api/connector-groups/{oid}/scheduled-upgrade | Get Connector Group Scheduled Upgrade
[**get_connector_group_scheduled_upgrade_status**](ConnectorGroupApi.md#get_connector_group_scheduled_upgrade_status) | **GET** /sse/connector/v2.0/api/connector-groups/{oid}/scheduled-upgrade-status | Get Connector Group Scheduled Upgrade Status
[**list_connector_group_applications**](ConnectorGroupApi.md#list_connector_group_applications) | **GET** /sse/connector/v2.0/api/connector-groups/{oid}/applications | List FQDNs per Connector Group
[**list_connector_group_connectors**](ConnectorGroupApi.md#list_connector_group_connectors) | **GET** /sse/connector/v2.0/api/connector-groups/{oid}/connectors | List Connectors per Connector Group
[**list_connector_group_filters**](ConnectorGroupApi.md#list_connector_group_filters) | **GET** /sse/connector/v2.0/api/connector-groups/filters | List Connector Group Filters
[**list_connector_group_subnets**](ConnectorGroupApi.md#list_connector_group_subnets) | **GET** /sse/connector/v2.0/api/connector-groups/{oid}/subnets | List Subnets per Connector Group
[**list_connector_group_wildcards**](ConnectorGroupApi.md#list_connector_group_wildcards) | **GET** /sse/connector/v2.0/api/connector-groups/{oid}/wildcards | List Wildcards per Connector Group
[**list_connector_groups**](ConnectorGroupApi.md#list_connector_groups) | **GET** /sse/connector/v2.0/api/connector-groups | List Connector Groups
[**update_connector_group_by_id**](ConnectorGroupApi.md#update_connector_group_by_id) | **PUT** /sse/connector/v2.0/api/connector-groups/{oid} | Update Connector Group
[**update_connector_group_scheduled_upgrade**](ConnectorGroupApi.md#update_connector_group_scheduled_upgrade) | **PUT** /sse/connector/v2.0/api/connector-groups/{oid}/scheduled-upgrade | Update Connector Group Scheduled Upgrade


# **create_connector_group**
> create_connector_group(connector_groups, x_panw_region=x_panw_region)

Create Connector Group

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import scm.ztna_connector_all
from scm.ztna_connector_all.models.connector_groups import ConnectorGroups
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
    api_instance = scm.ztna_connector_all.ConnectorGroupApi(api_client)
    connector_groups = scm.ztna_connector_all.ConnectorGroups() # ConnectorGroups | 
    x_panw_region = 'x_panw_region_example' # str | The region of the tenant (optional)

    try:
        # Create Connector Group
        api_instance.create_connector_group(connector_groups, x_panw_region=x_panw_region)
    except Exception as e:
        print("Exception when calling ConnectorGroupApi->create_connector_group: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **connector_groups** | [**ConnectorGroups**](ConnectorGroups.md)|  | 
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

# **create_connector_group_scheduled_upgrade**
> create_connector_group_scheduled_upgrade(oid, connector_group_scheduled_upgrade)

Create Connector Group Scheduled Upgrade

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import scm.ztna_connector_all
from scm.ztna_connector_all.models.connector_group_scheduled_upgrade import ConnectorGroupScheduledUpgrade
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
    api_instance = scm.ztna_connector_all.ConnectorGroupApi(api_client)
    oid = 'oid_example' # str | Object ID
    connector_group_scheduled_upgrade = scm.ztna_connector_all.ConnectorGroupScheduledUpgrade() # ConnectorGroupScheduledUpgrade | 

    try:
        # Create Connector Group Scheduled Upgrade
        api_instance.create_connector_group_scheduled_upgrade(oid, connector_group_scheduled_upgrade)
    except Exception as e:
        print("Exception when calling ConnectorGroupApi->create_connector_group_scheduled_upgrade: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **oid** | **str**| Object ID | 
 **connector_group_scheduled_upgrade** | [**ConnectorGroupScheduledUpgrade**](ConnectorGroupScheduledUpgrade.md)|  | 

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

# **delete_connector_group_by_id**
> delete_connector_group_by_id(oid, x_panw_region=x_panw_region)

Delete Connector Group

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
    api_instance = scm.ztna_connector_all.ConnectorGroupApi(api_client)
    oid = 'oid_example' # str | Object ID
    x_panw_region = 'x_panw_region_example' # str | The region of the tenant (optional)

    try:
        # Delete Connector Group
        api_instance.delete_connector_group_by_id(oid, x_panw_region=x_panw_region)
    except Exception as e:
        print("Exception when calling ConnectorGroupApi->delete_connector_group_by_id: %s\n" % e)
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

# **delete_connector_group_scheduled_upgrade**
> delete_connector_group_scheduled_upgrade(oid)

Delete Connector Group Scheduled Upgrade

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
    api_instance = scm.ztna_connector_all.ConnectorGroupApi(api_client)
    oid = 'oid_example' # str | Object ID

    try:
        # Delete Connector Group Scheduled Upgrade
        api_instance.delete_connector_group_scheduled_upgrade(oid)
    except Exception as e:
        print("Exception when calling ConnectorGroupApi->delete_connector_group_scheduled_upgrade: %s\n" % e)
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

# **get_connector_group_by_id**
> ConnectorGroups get_connector_group_by_id(oid, x_panw_region=x_panw_region)

Get Connector Group

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import scm.ztna_connector_all
from scm.ztna_connector_all.models.connector_groups import ConnectorGroups
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
    api_instance = scm.ztna_connector_all.ConnectorGroupApi(api_client)
    oid = 'oid_example' # str | Object ID
    x_panw_region = 'x_panw_region_example' # str | The region of the tenant (optional)

    try:
        # Get Connector Group
        api_response = api_instance.get_connector_group_by_id(oid, x_panw_region=x_panw_region)
        print("The response of ConnectorGroupApi->get_connector_group_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConnectorGroupApi->get_connector_group_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **oid** | **str**| Object ID | 
 **x_panw_region** | **str**| The region of the tenant | [optional] 

### Return type

[**ConnectorGroups**](ConnectorGroups.md)

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

# **get_connector_group_scheduled_upgrade**
> ConnectorGroupScheduledUpgrade get_connector_group_scheduled_upgrade(oid)

Get Connector Group Scheduled Upgrade

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import scm.ztna_connector_all
from scm.ztna_connector_all.models.connector_group_scheduled_upgrade import ConnectorGroupScheduledUpgrade
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
    api_instance = scm.ztna_connector_all.ConnectorGroupApi(api_client)
    oid = 'oid_example' # str | Object ID

    try:
        # Get Connector Group Scheduled Upgrade
        api_response = api_instance.get_connector_group_scheduled_upgrade(oid)
        print("The response of ConnectorGroupApi->get_connector_group_scheduled_upgrade:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConnectorGroupApi->get_connector_group_scheduled_upgrade: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **oid** | **str**| Object ID | 

### Return type

[**ConnectorGroupScheduledUpgrade**](ConnectorGroupScheduledUpgrade.md)

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

# **get_connector_group_scheduled_upgrade_status**
> ConnectorGroupUpgradeStatus get_connector_group_scheduled_upgrade_status(oid, x_panw_region=x_panw_region)

Get Connector Group Scheduled Upgrade Status

Retrieves the scheduled upgrade status for a connector group, including the upgrade status of all connectors in the group

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import scm.ztna_connector_all
from scm.ztna_connector_all.models.connector_group_upgrade_status import ConnectorGroupUpgradeStatus
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
    api_instance = scm.ztna_connector_all.ConnectorGroupApi(api_client)
    oid = 'oid_example' # str | Object ID
    x_panw_region = 'x_panw_region_example' # str | The region of the tenant (optional)

    try:
        # Get Connector Group Scheduled Upgrade Status
        api_response = api_instance.get_connector_group_scheduled_upgrade_status(oid, x_panw_region=x_panw_region)
        print("The response of ConnectorGroupApi->get_connector_group_scheduled_upgrade_status:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConnectorGroupApi->get_connector_group_scheduled_upgrade_status: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **oid** | **str**| Object ID | 
 **x_panw_region** | **str**| The region of the tenant | [optional] 

### Return type

[**ConnectorGroupUpgradeStatus**](ConnectorGroupUpgradeStatus.md)

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

# **list_connector_group_applications**
> ConnectorGroupFqdnRules list_connector_group_applications(oid, x_panw_region=x_panw_region, sort=sort, search=search, filters=filters)

List FQDNs per Connector Group

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import scm.ztna_connector_all
from scm.ztna_connector_all.models.connector_group_fqdn_rules import ConnectorGroupFqdnRules
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
    api_instance = scm.ztna_connector_all.ConnectorGroupApi(api_client)
    oid = 'oid_example' # str | Object ID
    x_panw_region = 'x_panw_region_example' # str | The region of the tenant (optional)
    sort = 'A[asc],B[desc],C' # str | List of fields from item response to sort by. (optional)
    search = 'connector1' # str | String to filter list results by. Is searched over multiple fields in each object. Multiple searches can be specified. (optional)
    filters = '{\"field\":\"name\",\"search\":\"abc\"}' # str | String to filter list results by searching one specified field of an object. Multiple filters can be specified. (optional)

    try:
        # List FQDNs per Connector Group
        api_response = api_instance.list_connector_group_applications(oid, x_panw_region=x_panw_region, sort=sort, search=search, filters=filters)
        print("The response of ConnectorGroupApi->list_connector_group_applications:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConnectorGroupApi->list_connector_group_applications: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **oid** | **str**| Object ID | 
 **x_panw_region** | **str**| The region of the tenant | [optional] 
 **sort** | **str**| List of fields from item response to sort by. | [optional] 
 **search** | **str**| String to filter list results by. Is searched over multiple fields in each object. Multiple searches can be specified. | [optional] 
 **filters** | **str**| String to filter list results by searching one specified field of an object. Multiple filters can be specified. | [optional] 

### Return type

[**ConnectorGroupFqdnRules**](ConnectorGroupFqdnRules.md)

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

# **list_connector_group_connectors**
> ConnectorGroupConnectors list_connector_group_connectors(oid, x_panw_region=x_panw_region, sort=sort, search=search, filters=filters)

List Connectors per Connector Group

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import scm.ztna_connector_all
from scm.ztna_connector_all.models.connector_group_connectors import ConnectorGroupConnectors
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
    api_instance = scm.ztna_connector_all.ConnectorGroupApi(api_client)
    oid = 'oid_example' # str | Object ID
    x_panw_region = 'x_panw_region_example' # str | The region of the tenant (optional)
    sort = 'A[asc],B[desc],C' # str | List of fields from item response to sort by. (optional)
    search = 'connector1' # str | String to filter list results by. Is searched over multiple fields in each object. Multiple searches can be specified. (optional)
    filters = '{\"field\":\"name\",\"search\":\"abc\"}' # str | String to filter list results by searching one specified field of an object. Multiple filters can be specified. (optional)

    try:
        # List Connectors per Connector Group
        api_response = api_instance.list_connector_group_connectors(oid, x_panw_region=x_panw_region, sort=sort, search=search, filters=filters)
        print("The response of ConnectorGroupApi->list_connector_group_connectors:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConnectorGroupApi->list_connector_group_connectors: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **oid** | **str**| Object ID | 
 **x_panw_region** | **str**| The region of the tenant | [optional] 
 **sort** | **str**| List of fields from item response to sort by. | [optional] 
 **search** | **str**| String to filter list results by. Is searched over multiple fields in each object. Multiple searches can be specified. | [optional] 
 **filters** | **str**| String to filter list results by searching one specified field of an object. Multiple filters can be specified. | [optional] 

### Return type

[**ConnectorGroupConnectors**](ConnectorGroupConnectors.md)

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

# **list_connector_group_filters**
> List[str] list_connector_group_filters(x_panw_region=x_panw_region, var_field=var_field, search=search)

List Connector Group Filters

Get filter values for connector group fields. 

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
    api_instance = scm.ztna_connector_all.ConnectorGroupApi(api_client)
    x_panw_region = 'x_panw_region_example' # str | The region of the tenant (optional)
    var_field = 'connector_group' # str | String that represents a static filter field. Call any of the /filters endpoints without specifying a field to get a list of all available fields. (optional)
    search = 'connector1' # str | String to filter list results by. Is searched over multiple fields in each object. Multiple searches can be specified. (optional)

    try:
        # List Connector Group Filters
        api_response = api_instance.list_connector_group_filters(x_panw_region=x_panw_region, var_field=var_field, search=search)
        print("The response of ConnectorGroupApi->list_connector_group_filters:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConnectorGroupApi->list_connector_group_filters: %s\n" % e)
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

# **list_connector_group_subnets**
> ConnectorGroupSubnetRules list_connector_group_subnets(oid, x_panw_region=x_panw_region, sort=sort, search=search, filters=filters)

List Subnets per Connector Group

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import scm.ztna_connector_all
from scm.ztna_connector_all.models.connector_group_subnet_rules import ConnectorGroupSubnetRules
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
    api_instance = scm.ztna_connector_all.ConnectorGroupApi(api_client)
    oid = 'oid_example' # str | Object ID
    x_panw_region = 'x_panw_region_example' # str | The region of the tenant (optional)
    sort = 'A[asc],B[desc],C' # str | List of fields from item response to sort by. (optional)
    search = 'connector1' # str | String to filter list results by. Is searched over multiple fields in each object. Multiple searches can be specified. (optional)
    filters = '{\"field\":\"name\",\"search\":\"abc\"}' # str | String to filter list results by searching one specified field of an object. Multiple filters can be specified. (optional)

    try:
        # List Subnets per Connector Group
        api_response = api_instance.list_connector_group_subnets(oid, x_panw_region=x_panw_region, sort=sort, search=search, filters=filters)
        print("The response of ConnectorGroupApi->list_connector_group_subnets:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConnectorGroupApi->list_connector_group_subnets: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **oid** | **str**| Object ID | 
 **x_panw_region** | **str**| The region of the tenant | [optional] 
 **sort** | **str**| List of fields from item response to sort by. | [optional] 
 **search** | **str**| String to filter list results by. Is searched over multiple fields in each object. Multiple searches can be specified. | [optional] 
 **filters** | **str**| String to filter list results by searching one specified field of an object. Multiple filters can be specified. | [optional] 

### Return type

[**ConnectorGroupSubnetRules**](ConnectorGroupSubnetRules.md)

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

# **list_connector_group_wildcards**
> ConnectorGroupWildcards list_connector_group_wildcards(oid, x_panw_region=x_panw_region, sort=sort, search=search, filters=filters)

List Wildcards per Connector Group

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import scm.ztna_connector_all
from scm.ztna_connector_all.models.connector_group_wildcards import ConnectorGroupWildcards
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
    api_instance = scm.ztna_connector_all.ConnectorGroupApi(api_client)
    oid = 'oid_example' # str | Object ID
    x_panw_region = 'x_panw_region_example' # str | The region of the tenant (optional)
    sort = 'A[asc],B[desc],C' # str | List of fields from item response to sort by. (optional)
    search = 'connector1' # str | String to filter list results by. Is searched over multiple fields in each object. Multiple searches can be specified. (optional)
    filters = '{\"field\":\"name\",\"search\":\"abc\"}' # str | String to filter list results by searching one specified field of an object. Multiple filters can be specified. (optional)

    try:
        # List Wildcards per Connector Group
        api_response = api_instance.list_connector_group_wildcards(oid, x_panw_region=x_panw_region, sort=sort, search=search, filters=filters)
        print("The response of ConnectorGroupApi->list_connector_group_wildcards:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConnectorGroupApi->list_connector_group_wildcards: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **oid** | **str**| Object ID | 
 **x_panw_region** | **str**| The region of the tenant | [optional] 
 **sort** | **str**| List of fields from item response to sort by. | [optional] 
 **search** | **str**| String to filter list results by. Is searched over multiple fields in each object. Multiple searches can be specified. | [optional] 
 **filters** | **str**| String to filter list results by searching one specified field of an object. Multiple filters can be specified. | [optional] 

### Return type

[**ConnectorGroupWildcards**](ConnectorGroupWildcards.md)

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

# **list_connector_groups**
> ConnectorGroupsListResponse list_connector_groups(x_panw_region=x_panw_region, offset=offset, limit=limit, sort=sort, search=search, filters=filters)

List Connector Groups

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import scm.ztna_connector_all
from scm.ztna_connector_all.models.connector_groups_list_response import ConnectorGroupsListResponse
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
    api_instance = scm.ztna_connector_all.ConnectorGroupApi(api_client)
    x_panw_region = 'x_panw_region_example' # str | The region of the tenant (optional)
    offset = 56 # int | A 0-based offset into the collection. It is the index of the starting entry of the page  (optional)
    limit = 56 # int | The max count in result entry (count per page) (optional)
    sort = 'A[asc],B[desc],C' # str | List of fields from item response to sort by. (optional)
    search = 'connector1' # str | String to filter list results by. Is searched over multiple fields in each object. Multiple searches can be specified. (optional)
    filters = '{\"field\":\"name\",\"search\":\"abc\"}' # str | String to filter list results by searching one specified field of an object. Multiple filters can be specified. (optional)

    try:
        # List Connector Groups
        api_response = api_instance.list_connector_groups(x_panw_region=x_panw_region, offset=offset, limit=limit, sort=sort, search=search, filters=filters)
        print("The response of ConnectorGroupApi->list_connector_groups:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConnectorGroupApi->list_connector_groups: %s\n" % e)
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

[**ConnectorGroupsListResponse**](ConnectorGroupsListResponse.md)

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

# **update_connector_group_by_id**
> update_connector_group_by_id(oid, connector_groups, x_panw_region=x_panw_region)

Update Connector Group

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import scm.ztna_connector_all
from scm.ztna_connector_all.models.connector_groups import ConnectorGroups
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
    api_instance = scm.ztna_connector_all.ConnectorGroupApi(api_client)
    oid = 'oid_example' # str | Object ID
    connector_groups = scm.ztna_connector_all.ConnectorGroups() # ConnectorGroups | 
    x_panw_region = 'x_panw_region_example' # str | The region of the tenant (optional)

    try:
        # Update Connector Group
        api_instance.update_connector_group_by_id(oid, connector_groups, x_panw_region=x_panw_region)
    except Exception as e:
        print("Exception when calling ConnectorGroupApi->update_connector_group_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **oid** | **str**| Object ID | 
 **connector_groups** | [**ConnectorGroups**](ConnectorGroups.md)|  | 
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

# **update_connector_group_scheduled_upgrade**
> update_connector_group_scheduled_upgrade(oid, connector_group_scheduled_upgrade)

Update Connector Group Scheduled Upgrade

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import scm.ztna_connector_all
from scm.ztna_connector_all.models.connector_group_scheduled_upgrade import ConnectorGroupScheduledUpgrade
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
    api_instance = scm.ztna_connector_all.ConnectorGroupApi(api_client)
    oid = 'oid_example' # str | Object ID
    connector_group_scheduled_upgrade = scm.ztna_connector_all.ConnectorGroupScheduledUpgrade() # ConnectorGroupScheduledUpgrade | 

    try:
        # Update Connector Group Scheduled Upgrade
        api_instance.update_connector_group_scheduled_upgrade(oid, connector_group_scheduled_upgrade)
    except Exception as e:
        print("Exception when calling ConnectorGroupApi->update_connector_group_scheduled_upgrade: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **oid** | **str**| Object ID | 
 **connector_group_scheduled_upgrade** | [**ConnectorGroupScheduledUpgrade**](ConnectorGroupScheduledUpgrade.md)|  | 

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

