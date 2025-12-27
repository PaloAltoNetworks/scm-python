# scm.config_setup.TrustedTenantsOverviewApi

All URIs are relative to *https://api.strata.paloaltonetworks.com/config/setup/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_trusted_tenants_overview**](TrustedTenantsOverviewApi.md#get_trusted_tenants_overview) | **GET** /trusted-tenant-overview | Trusted Tenants Overview


# **get_trusted_tenants_overview**
> TrustedTenantOverview get_trusted_tenants_overview()

Trusted Tenants Overview

Overview of publishers and subscribers. 

### Example

* Bearer (JWT) Authentication (scmToken):

```python
import scm.config_setup
from scm.config_setup.models.trusted_tenant_overview import TrustedTenantOverview
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
    api_instance = scm.config_setup.TrustedTenantsOverviewApi(api_client)

    try:
        # Trusted Tenants Overview
        api_response = api_instance.get_trusted_tenants_overview()
        print("The response of TrustedTenantsOverviewApi->get_trusted_tenants_overview:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TrustedTenantsOverviewApi->get_trusted_tenants_overview: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**TrustedTenantOverview**](TrustedTenantOverview.md)

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

