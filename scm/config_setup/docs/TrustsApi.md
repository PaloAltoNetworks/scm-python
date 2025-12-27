# scm_config_setup.TrustsApi

All URIs are relative to *https://api.strata.paloaltonetworks.com/config/setup/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_trust**](TrustsApi.md#create_trust) | **POST** /trusts | Create a trust
[**delete_trust**](TrustsApi.md#delete_trust) | **DELETE** /trusts | Delete a Trust


# **create_trust**
> TenantTrustInfo create_trust(trusts=trusts)

Create a trust

Create a new trust. 

### Example

* Bearer (JWT) Authentication (scmToken):

```python
import scm_config_setup
from scm_config_setup.models.tenant_trust_info import TenantTrustInfo
from scm_config_setup.models.trusts import Trusts
from scm_config_setup.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.strata.paloaltonetworks.com/config/setup/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = scm_config_setup.Configuration(
    host = "https://api.strata.paloaltonetworks.com/config/setup/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): scmToken
configuration = scm_config_setup.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with scm_config_setup.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = scm_config_setup.TrustsApi(api_client)
    trusts = scm_config_setup.Trusts() # Trusts | The `trusts` resource definition (optional)

    try:
        # Create a trust
        api_response = api_instance.create_trust(trusts=trusts)
        print("The response of TrustsApi->create_trust:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TrustsApi->create_trust: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **trusts** | [**Trusts**](Trusts.md)| The &#x60;trusts&#x60; resource definition | [optional] 

### Return type

[**TenantTrustInfo**](TenantTrustInfo.md)

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

# **delete_trust**
> delete_trust(trustids, type)

Delete a Trust

Delete an existing Trust. 

### Example

* Bearer (JWT) Authentication (scmToken):

```python
import scm_config_setup
from scm_config_setup.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.strata.paloaltonetworks.com/config/setup/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = scm_config_setup.Configuration(
    host = "https://api.strata.paloaltonetworks.com/config/setup/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): scmToken
configuration = scm_config_setup.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with scm_config_setup.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = scm_config_setup.TrustsApi(api_client)
    trustids = 'trustids_example' # str | Comma-separated list of trust IDs 
    type = 'type_example' # str | Specifies the type of the tenant that is trusted, either 'subscriber' or 'publisher'. 

    try:
        # Delete a Trust
        api_instance.delete_trust(trustids, type)
    except Exception as e:
        print("Exception when calling TrustsApi->delete_trust: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **trustids** | **str**| Comma-separated list of trust IDs  | 
 **type** | **str**| Specifies the type of the tenant that is trusted, either &#39;subscriber&#39; or &#39;publisher&#39;.  | 

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

