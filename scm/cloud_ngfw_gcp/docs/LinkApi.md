# scm.cloud_ngfw_gcp.LinkApi

All URIs are relative to *https://api.strata.paloaltonetworks.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**generate_link_code**](LinkApi.md#generate_link_code) | **POST** /cngfw-gcp/v2/link/generate | Generate a link code
[**unlink_tenant**](LinkApi.md#unlink_tenant) | **POST** /cngfw-gcp/v2/link/unlink | Unlink a firewall endpoint


# **generate_link_code**
> LinkGenerateResponse generate_link_code(link_generate_request, x_panw_region=x_panw_region)

Generate a link code

Generates a one-time link code for a Google Cloud tenant. The customer enters the code in the Google Cloud console when creating a firewall endpoint, which links the Google Cloud tenant to the TSG the access token is scoped to. The code expires after 48 hours.  The response is the only place the code is returned: the service stores only its hash. Treat the code as a secret and do not log the response body.  The service looks up the TSG's Customer Support Portal account ID and cloud management tenant ID itself. ResponseStatus.Code on a failed call is one of FIELD_MISSING, FIELD_INVALID, SCM_NOT_PROVISIONED (the TSG has no Strata Cloud Manager), UNAUTHENTICATED or INTERNAL_ERROR. 

### Example

* Bearer (JWT) Authentication (scmToken):

```python
import scm.cloud_ngfw_gcp
from scm.cloud_ngfw_gcp.models.link_generate_request import LinkGenerateRequest
from scm.cloud_ngfw_gcp.models.link_generate_response import LinkGenerateResponse
from scm.cloud_ngfw_gcp.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.strata.paloaltonetworks.com
# See configuration.py for a list of all supported configuration parameters.
configuration = scm.cloud_ngfw_gcp.Configuration(
    host = "https://api.strata.paloaltonetworks.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): scmToken
configuration = scm.cloud_ngfw_gcp.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with scm.cloud_ngfw_gcp.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = scm.cloud_ngfw_gcp.LinkApi(api_client)
    link_generate_request = scm.cloud_ngfw_gcp.LinkGenerateRequest() # LinkGenerateRequest | The Google Cloud tenant to link
    x_panw_region = 'x_panw_region_example' # str | The Cloud NGFW region the link is stored in. If omitted, the API gateway default is used. (optional)

    try:
        # Generate a link code
        api_response = api_instance.generate_link_code(link_generate_request, x_panw_region=x_panw_region)
        print("The response of LinkApi->generate_link_code:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LinkApi->generate_link_code: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **link_generate_request** | [**LinkGenerateRequest**](LinkGenerateRequest.md)| The Google Cloud tenant to link | 
 **x_panw_region** | **str**| The Cloud NGFW region the link is stored in. If omitted, the API gateway default is used. | [optional] 

### Return type

[**LinkGenerateResponse**](LinkGenerateResponse.md)

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
**0** | General Errors |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **unlink_tenant**
> LinkUnlinkResponse unlink_tenant(link_unlink_request, x_panw_region=x_panw_region)

Unlink a firewall endpoint

Retires the binding made when Google redeemed a link code, offboarding the firewall endpoint created with that code. Google calls this when it deletes the endpoint.  Only a redeemed code is bound to anything. Unlinking a code that was never used, or naming a Google Cloud tenant the code was not generated for, retires nothing: the call still succeeds with Unlinked set to true, and an unused code stays valid until it expires. ResponseStatus.Code on a failed call is one of FIELD_MISSING, FIELD_INVALID or INTERNAL_ERROR. 

### Example

* Bearer (JWT) Authentication (scmToken):

```python
import scm.cloud_ngfw_gcp
from scm.cloud_ngfw_gcp.models.link_unlink_request import LinkUnlinkRequest
from scm.cloud_ngfw_gcp.models.link_unlink_response import LinkUnlinkResponse
from scm.cloud_ngfw_gcp.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.strata.paloaltonetworks.com
# See configuration.py for a list of all supported configuration parameters.
configuration = scm.cloud_ngfw_gcp.Configuration(
    host = "https://api.strata.paloaltonetworks.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): scmToken
configuration = scm.cloud_ngfw_gcp.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with scm.cloud_ngfw_gcp.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = scm.cloud_ngfw_gcp.LinkApi(api_client)
    link_unlink_request = scm.cloud_ngfw_gcp.LinkUnlinkRequest() # LinkUnlinkRequest | The link code and the Google Cloud tenant it was generated for
    x_panw_region = 'x_panw_region_example' # str | The Cloud NGFW region the link is stored in. If omitted, the API gateway default is used. (optional)

    try:
        # Unlink a firewall endpoint
        api_response = api_instance.unlink_tenant(link_unlink_request, x_panw_region=x_panw_region)
        print("The response of LinkApi->unlink_tenant:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LinkApi->unlink_tenant: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **link_unlink_request** | [**LinkUnlinkRequest**](LinkUnlinkRequest.md)| The link code and the Google Cloud tenant it was generated for | 
 **x_panw_region** | **str**| The Cloud NGFW region the link is stored in. If omitted, the API gateway default is used. | [optional] 

### Return type

[**LinkUnlinkResponse**](LinkUnlinkResponse.md)

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
**0** | General Errors |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

