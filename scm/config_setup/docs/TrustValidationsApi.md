# scm_config_setup.TrustValidationsApi

All URIs are relative to *https://api.strata.paloaltonetworks.com/config/setup/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**validate_trust**](TrustValidationsApi.md#validate_trust) | **POST** /trust-validations | Validates Trust


# **validate_trust**
> TenantTrustInfo validate_trust(trusts_validation_payload=trusts_validation_payload)

Validates Trust

Validate trust. 

### Example

* Bearer (JWT) Authentication (scmToken):

```python
import scm_config_setup
from scm_config_setup.models.tenant_trust_info import TenantTrustInfo
from scm_config_setup.models.trusts_validation_payload import TrustsValidationPayload
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
    api_instance = scm_config_setup.TrustValidationsApi(api_client)
    trusts_validation_payload = scm_config_setup.TrustsValidationPayload() # TrustsValidationPayload | The `trust validation` resource definition (optional)

    try:
        # Validates Trust
        api_response = api_instance.validate_trust(trusts_validation_payload=trusts_validation_payload)
        print("The response of TrustValidationsApi->validate_trust:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TrustValidationsApi->validate_trust: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **trusts_validation_payload** | [**TrustsValidationPayload**](TrustsValidationPayload.md)| The &#x60;trust validation&#x60; resource definition | [optional] 

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
**200** | OK |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**409** | Conflict |  -  |
**0** | General Errors |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

