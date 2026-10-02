# scm.ztna_connector_all.FQDNApi

All URIs are relative to *https://api.sase.paloaltonetworks.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_applications**](FQDNApi.md#create_applications) | **POST** /sse/connector/v2.0/api/applications | Create FQDN
[**delete_applications_by_id**](FQDNApi.md#delete_applications_by_id) | **DELETE** /sse/connector/v2.0/api/applications/{oid} | Delete FQDN
[**get_applications_by_id**](FQDNApi.md#get_applications_by_id) | **GET** /sse/connector/v2.0/api/applications/{oid} | Get FQDN
[**list_application_filters**](FQDNApi.md#list_application_filters) | **GET** /sse/connector/v2.0/api/applications/filters | List FQDN Filters
[**list_applications**](FQDNApi.md#list_applications) | **GET** /sse/connector/v2.0/api/applications | List FQDNs
[**update_applications_by_id**](FQDNApi.md#update_applications_by_id) | **PUT** /sse/connector/v2.0/api/applications/{oid} | Update FQDN


# **create_applications**
> create_applications(applications, x_panw_region=x_panw_region)

Create FQDN

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import scm.ztna_connector_all
from scm.ztna_connector_all.models.applications import Applications
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
    api_instance = scm.ztna_connector_all.FQDNApi(api_client)
    applications = scm.ztna_connector_all.Applications() # Applications | 
    x_panw_region = 'x_panw_region_example' # str | The region of the tenant (optional)

    try:
        # Create FQDN
        api_instance.create_applications(applications, x_panw_region=x_panw_region)
    except Exception as e:
        print("Exception when calling FQDNApi->create_applications: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **applications** | [**Applications**](Applications.md)|  | 
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

# **delete_applications_by_id**
> delete_applications_by_id(oid, x_panw_region=x_panw_region)

Delete FQDN

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
    api_instance = scm.ztna_connector_all.FQDNApi(api_client)
    oid = 'oid_example' # str | Object ID
    x_panw_region = 'x_panw_region_example' # str | The region of the tenant (optional)

    try:
        # Delete FQDN
        api_instance.delete_applications_by_id(oid, x_panw_region=x_panw_region)
    except Exception as e:
        print("Exception when calling FQDNApi->delete_applications_by_id: %s\n" % e)
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

# **get_applications_by_id**
> Applications get_applications_by_id(oid, x_panw_region=x_panw_region)

Get FQDN

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import scm.ztna_connector_all
from scm.ztna_connector_all.models.applications import Applications
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
    api_instance = scm.ztna_connector_all.FQDNApi(api_client)
    oid = 'oid_example' # str | Object ID
    x_panw_region = 'x_panw_region_example' # str | The region of the tenant (optional)

    try:
        # Get FQDN
        api_response = api_instance.get_applications_by_id(oid, x_panw_region=x_panw_region)
        print("The response of FQDNApi->get_applications_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FQDNApi->get_applications_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **oid** | **str**| Object ID | 
 **x_panw_region** | **str**| The region of the tenant | [optional] 

### Return type

[**Applications**](Applications.md)

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

# **list_application_filters**
> List[str] list_application_filters(x_panw_region=x_panw_region, var_field=var_field, search=search)

List FQDN Filters

Get filter values for FQDN rule fields. 

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
    api_instance = scm.ztna_connector_all.FQDNApi(api_client)
    x_panw_region = 'x_panw_region_example' # str | The region of the tenant (optional)
    var_field = 'connector_group' # str | String that represents a static filter field. Call any of the /filters endpoints without specifying a field to get a list of all available fields. (optional)
    search = 'connector1' # str | String to filter list results by. Is searched over multiple fields in each object. Multiple searches can be specified. (optional)

    try:
        # List FQDN Filters
        api_response = api_instance.list_application_filters(x_panw_region=x_panw_region, var_field=var_field, search=search)
        print("The response of FQDNApi->list_application_filters:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FQDNApi->list_application_filters: %s\n" % e)
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

# **list_applications**
> ApplicationsListResponse list_applications(x_panw_region=x_panw_region, offset=offset, limit=limit, sort=sort, search=search, filters=filters)

List FQDNs

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import scm.ztna_connector_all
from scm.ztna_connector_all.models.applications_list_response import ApplicationsListResponse
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
    api_instance = scm.ztna_connector_all.FQDNApi(api_client)
    x_panw_region = 'x_panw_region_example' # str | The region of the tenant (optional)
    offset = 56 # int | A 0-based offset into the collection. It is the index of the starting entry of the page  (optional)
    limit = 56 # int | The max count in result entry (count per page) (optional)
    sort = 'A[asc],B[desc],C' # str | List of fields from item response to sort by. (optional)
    search = 'connector1' # str | String to filter list results by. Is searched over multiple fields in each object. Multiple searches can be specified. (optional)
    filters = '{\"field\":\"name\",\"search\":\"abc\"}' # str | String to filter list results by searching one specified field of an object. Multiple filters can be specified. (optional)

    try:
        # List FQDNs
        api_response = api_instance.list_applications(x_panw_region=x_panw_region, offset=offset, limit=limit, sort=sort, search=search, filters=filters)
        print("The response of FQDNApi->list_applications:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FQDNApi->list_applications: %s\n" % e)
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

[**ApplicationsListResponse**](ApplicationsListResponse.md)

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

# **update_applications_by_id**
> update_applications_by_id(oid, applications, x_panw_region=x_panw_region)

Update FQDN

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import scm.ztna_connector_all
from scm.ztna_connector_all.models.applications import Applications
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
    api_instance = scm.ztna_connector_all.FQDNApi(api_client)
    oid = 'oid_example' # str | Object ID
    applications = scm.ztna_connector_all.Applications() # Applications | 
    x_panw_region = 'x_panw_region_example' # str | The region of the tenant (optional)

    try:
        # Update FQDN
        api_instance.update_applications_by_id(oid, applications, x_panw_region=x_panw_region)
    except Exception as e:
        print("Exception when calling FQDNApi->update_applications_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **oid** | **str**| Object ID | 
 **applications** | [**Applications**](Applications.md)|  | 
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

