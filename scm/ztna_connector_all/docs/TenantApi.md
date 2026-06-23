# scm.ztna_connector_all.TenantApi

All URIs are relative to *https://api.sase.paloaltonetworks.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_license**](TenantApi.md#get_license) | **GET** /sse/connector/v2.0/api/license | Get Tenant License Info
[**get_tenant_status**](TenantApi.md#get_tenant_status) | **GET** /sse/connector/v2.0/api/tenant:status | Get Tenant Status
[**start_tenant_offboarding**](TenantApi.md#start_tenant_offboarding) | **POST** /sse/connector/v2.0/api/tenant:start-offboarding | Start Tenant Offboarding
[**start_tenant_onboarding**](TenantApi.md#start_tenant_onboarding) | **POST** /sse/connector/v2.0/api/tenant:start-onboarding | Start Tenant Onboarding


# **get_license**
> LicenseInfo get_license(x_panw_region=x_panw_region)

Get Tenant License Info

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import scm.ztna_connector_all
from scm.ztna_connector_all.models.license_info import LicenseInfo
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
    api_instance = scm.ztna_connector_all.TenantApi(api_client)
    x_panw_region = 'x_panw_region_example' # str | The region of the tenant (optional)

    try:
        # Get Tenant License Info
        api_response = api_instance.get_license(x_panw_region=x_panw_region)
        print("The response of TenantApi->get_license:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TenantApi->get_license: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_panw_region** | **str**| The region of the tenant | [optional] 

### Return type

[**LicenseInfo**](LicenseInfo.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |
**424** | Failed Dependency |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tenant_status**
> TenantStatus get_tenant_status(x_panw_region=x_panw_region)

Get Tenant Status

Retrieves the current status of the tenant

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import scm.ztna_connector_all
from scm.ztna_connector_all.models.tenant_status import TenantStatus
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
    api_instance = scm.ztna_connector_all.TenantApi(api_client)
    x_panw_region = 'x_panw_region_example' # str | The region of the tenant (optional)

    try:
        # Get Tenant Status
        api_response = api_instance.get_tenant_status(x_panw_region=x_panw_region)
        print("The response of TenantApi->get_tenant_status:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TenantApi->get_tenant_status: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_panw_region** | **str**| The region of the tenant | [optional] 

### Return type

[**TenantStatus**](TenantStatus.md)

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

# **start_tenant_offboarding**
> StartTenantOffboarding202Response start_tenant_offboarding(x_panw_region=x_panw_region)

Start Tenant Offboarding

Initiates tenant deletion. This marks the tenant for deletion and triggers the cleanup process.

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import scm.ztna_connector_all
from scm.ztna_connector_all.models.start_tenant_offboarding202_response import StartTenantOffboarding202Response
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
    api_instance = scm.ztna_connector_all.TenantApi(api_client)
    x_panw_region = 'x_panw_region_example' # str | The region of the tenant (optional)

    try:
        # Start Tenant Offboarding
        api_response = api_instance.start_tenant_offboarding(x_panw_region=x_panw_region)
        print("The response of TenantApi->start_tenant_offboarding:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TenantApi->start_tenant_offboarding: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_panw_region** | **str**| The region of the tenant | [optional] 

### Return type

[**StartTenantOffboarding202Response**](StartTenantOffboarding202Response.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Accepted |  -  |
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **start_tenant_onboarding**
> start_tenant_onboarding(x_panw_region=x_panw_region)

Start Tenant Onboarding

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
    api_instance = scm.ztna_connector_all.TenantApi(api_client)
    x_panw_region = 'x_panw_region_example' # str | The region of the tenant (optional)

    try:
        # Start Tenant Onboarding
        api_instance.start_tenant_onboarding(x_panw_region=x_panw_region)
    except Exception as e:
        print("Exception when calling TenantApi->start_tenant_onboarding: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

