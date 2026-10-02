# scm.ztna_connector_all.DiscoveredApplicationApi

All URIs are relative to *https://api.sase.paloaltonetworks.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_discovered_application_filters**](DiscoveredApplicationApi.md#list_discovered_application_filters) | **GET** /sse/connector/v2.0/api/discovered-applications/filters | List Discovered Application Filters
[**list_discovered_applications**](DiscoveredApplicationApi.md#list_discovered_applications) | **GET** /sse/connector/v2.0/api/discovered-applications | List Discovered Applications


# **list_discovered_application_filters**
> List[str] list_discovered_application_filters(x_panw_region=x_panw_region, var_field=var_field, search=search)

List Discovered Application Filters

Get filter values for discovered application fields. 

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
    api_instance = scm.ztna_connector_all.DiscoveredApplicationApi(api_client)
    x_panw_region = 'x_panw_region_example' # str | The region of the tenant (optional)
    var_field = 'connector_group' # str | String that represents a static filter field. Call any of the /filters endpoints without specifying a field to get a list of all available fields. (optional)
    search = 'connector1' # str | String to filter list results by. Is searched over multiple fields in each object. Multiple searches can be specified. (optional)

    try:
        # List Discovered Application Filters
        api_response = api_instance.list_discovered_application_filters(x_panw_region=x_panw_region, var_field=var_field, search=search)
        print("The response of DiscoveredApplicationApi->list_discovered_application_filters:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DiscoveredApplicationApi->list_discovered_application_filters: %s\n" % e)
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

# **list_discovered_applications**
> DiscoveredApplicationsListResponse list_discovered_applications(x_panw_region=x_panw_region, offset=offset, limit=limit, sort=sort, search=search, filters=filters)

List Discovered Applications

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import scm.ztna_connector_all
from scm.ztna_connector_all.models.discovered_applications_list_response import DiscoveredApplicationsListResponse
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
    api_instance = scm.ztna_connector_all.DiscoveredApplicationApi(api_client)
    x_panw_region = 'x_panw_region_example' # str | The region of the tenant (optional)
    offset = 56 # int | A 0-based offset into the collection. It is the index of the starting entry of the page  (optional)
    limit = 56 # int | The max count in result entry (count per page) (optional)
    sort = 'A[asc],B[desc],C' # str | List of fields from item response to sort by. (optional)
    search = 'connector1' # str | String to filter list results by. Is searched over multiple fields in each object. Multiple searches can be specified. (optional)
    filters = '{\"field\":\"name\",\"search\":\"abc\"}' # str | String to filter list results by searching one specified field of an object. Multiple filters can be specified. (optional)

    try:
        # List Discovered Applications
        api_response = api_instance.list_discovered_applications(x_panw_region=x_panw_region, offset=offset, limit=limit, sort=sort, search=search, filters=filters)
        print("The response of DiscoveredApplicationApi->list_discovered_applications:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DiscoveredApplicationApi->list_discovered_applications: %s\n" % e)
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

[**DiscoveredApplicationsListResponse**](DiscoveredApplicationsListResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**202** | [202 Accepted](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/202)  The request has been accepted for processing, but the processing has not been completed. The client should retry the request after the time specified in the Retry-After header.  |  * Retry-After - Indicates how long the client should wait before making a follow-up request <br>  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

