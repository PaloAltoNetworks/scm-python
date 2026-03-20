# scm.config_setup.TrustInformationApi

All URIs are relative to *https://api.strata.paloaltonetworks.com/config/setup/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_trusted_tenants_with_snippets**](TrustInformationApi.md#list_trusted_tenants_with_snippets) | **GET** /trusted-tenants | Trusted Tenants With Snippets


# **list_trusted_tenants_with_snippets**
> List[TrustInfoWithSharedSnippets] list_trusted_tenants_with_snippets(type)

Trusted Tenants With Snippets

Retrieve a list of trusted tenants with snippets. 

### Example

* Bearer (JWT) Authentication (scmToken):

```python
import scm.config_setup
from scm.config_setup.models.trust_info_with_shared_snippets import TrustInfoWithSharedSnippets
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
    api_instance = scm.config_setup.TrustInformationApi(api_client)
    type = 'type_example' # str | Specifies the type of the tenant that is trusted, either 'subscriber' or 'publisher'. 

    try:
        # Trusted Tenants With Snippets
        api_response = api_instance.list_trusted_tenants_with_snippets(type)
        print("The response of TrustInformationApi->list_trusted_tenants_with_snippets:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TrustInformationApi->list_trusted_tenants_with_snippets: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**| Specifies the type of the tenant that is trusted, either &#39;subscriber&#39; or &#39;publisher&#39;.  | 

### Return type

[**List[TrustInfoWithSharedSnippets]**](TrustInfoWithSharedSnippets.md)

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

