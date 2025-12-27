# scm_security_services.SaasTenantRestrictionsApi

All URIs are relative to *https://api.strata.paloaltonetworks.com/config/security/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_saas_tenant_restrictions**](SaasTenantRestrictionsApi.md#get_saas_tenant_restrictions) | **GET** /saas-tenant-restrictions | Get Saas Tenant Restrictions
[**update_saas_tenant_restrictions**](SaasTenantRestrictionsApi.md#update_saas_tenant_restrictions) | **PUT** /saas-tenant-restrictions | Update Saas Tenant Restrictions


# **get_saas_tenant_restrictions**
> GetSaasTenantRestrictionsListResponse get_saas_tenant_restrictions(name=name, folder=folder, snippet=snippet, device=device, offset=offset, limit=limit)

Get Saas Tenant Restrictions

Get Saas Tenant Restrictions

### Example

* Bearer (JWT) Authentication (scmToken):

```python
import scm_security_services
from scm_security_services.models.get_saas_tenant_restrictions_list_response import GetSaasTenantRestrictionsListResponse
from scm_security_services.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.strata.paloaltonetworks.com/config/security/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = scm_security_services.Configuration(
    host = "https://api.strata.paloaltonetworks.com/config/security/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): scmToken
configuration = scm_security_services.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with scm_security_services.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = scm_security_services.SaasTenantRestrictionsApi(api_client)
    name = 'name_example' # str | The name of the configuration resource (optional)
    folder = 'folder_example' # str | The folder in which the resource is defined  (optional)
    snippet = 'snippet_example' # str | The snippet in which the resource is defined  (optional)
    device = 'device_example' # str | The device in which the resource is defined  (optional)
    offset = 0 # int | The offset into the list of results returned (optional) (default to 0)
    limit = 200 # int | The maximum number of results per page (optional) (default to 200)

    try:
        # Get Saas Tenant Restrictions
        api_response = api_instance.get_saas_tenant_restrictions(name=name, folder=folder, snippet=snippet, device=device, offset=offset, limit=limit)
        print("The response of SaasTenantRestrictionsApi->get_saas_tenant_restrictions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SaasTenantRestrictionsApi->get_saas_tenant_restrictions: %s\n" % e)
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

[**GetSaasTenantRestrictionsListResponse**](GetSaasTenantRestrictionsListResponse.md)

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

# **update_saas_tenant_restrictions**
> SaasTenantRestrictions update_saas_tenant_restrictions(snippet=snippet, saas_tenant_restrictions=saas_tenant_restrictions)

Update Saas Tenant Restrictions

Update Saas Tenant Restrictions

### Example

* Bearer (JWT) Authentication (scmToken):

```python
import scm_security_services
from scm_security_services.models.saas_tenant_restrictions import SaasTenantRestrictions
from scm_security_services.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.strata.paloaltonetworks.com/config/security/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = scm_security_services.Configuration(
    host = "https://api.strata.paloaltonetworks.com/config/security/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): scmToken
configuration = scm_security_services.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with scm_security_services.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = scm_security_services.SaasTenantRestrictionsApi(api_client)
    snippet = 'snippet_example' # str | The snippet in which the resource is defined  (optional)
    saas_tenant_restrictions = scm_security_services.SaasTenantRestrictions() # SaasTenantRestrictions | OK (optional)

    try:
        # Update Saas Tenant Restrictions
        api_response = api_instance.update_saas_tenant_restrictions(snippet=snippet, saas_tenant_restrictions=saas_tenant_restrictions)
        print("The response of SaasTenantRestrictionsApi->update_saas_tenant_restrictions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SaasTenantRestrictionsApi->update_saas_tenant_restrictions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **snippet** | **str**| The snippet in which the resource is defined  | [optional] 
 **saas_tenant_restrictions** | [**SaasTenantRestrictions**](SaasTenantRestrictions.md)| OK | [optional] 

### Return type

[**SaasTenantRestrictions**](SaasTenantRestrictions.md)

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

