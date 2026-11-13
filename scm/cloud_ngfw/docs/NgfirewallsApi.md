# scm.cloud_ngfw.NgfirewallsApi

All URIs are relative to *https://api.strata.paloaltonetworks.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_ngfirewalls**](NgfirewallsApi.md#create_ngfirewalls) | **POST** /cngfw-aws/v2/config/ngfirewalls | Create a Cloud NGFW firewall
[**delete_ngfirewalls_by_id**](NgfirewallsApi.md#delete_ngfirewalls_by_id) | **DELETE** /cngfw-aws/v2/config/ngfirewalls/{id} | Delete a Cloud NGFW firewall.
[**get_ngfirewalls_by_id**](NgfirewallsApi.md#get_ngfirewalls_by_id) | **GET** /cngfw-aws/v2/config/ngfirewalls/{id} | Get a Cloud NGFW firewall
[**list_ngfirewalls**](NgfirewallsApi.md#list_ngfirewalls) | **GET** /cngfw-aws/v2/config/ngfirewalls | List Cloud NGFW firewalls
[**update_ngfirewalls_by_id**](NgfirewallsApi.md#update_ngfirewalls_by_id) | **PATCH** /cngfw-aws/v2/config/ngfirewalls/{id} | Update a Cloud NGFW firewall


# **create_ngfirewalls**
> NgfirewallCreateResponse create_ngfirewalls(region, ngfirewall_create_request)

Create a Cloud NGFW firewall

Creates a Cloud NGFW firewall. Use CreateCloudNGFirewall (Go SDK) or create_cloud_ng_firewall (Python SDK) instead. 

### Example

* Bearer (JWT) Authentication (scmToken):

```python
import scm.cloud_ngfw
from scm.cloud_ngfw.models.ngfirewall_create_request import NgfirewallCreateRequest
from scm.cloud_ngfw.models.ngfirewall_create_response import NgfirewallCreateResponse
from scm.cloud_ngfw.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.strata.paloaltonetworks.com
# See configuration.py for a list of all supported configuration parameters.
configuration = scm.cloud_ngfw.Configuration(
    host = "https://api.strata.paloaltonetworks.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): scmToken
configuration = scm.cloud_ngfw.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with scm.cloud_ngfw.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = scm.cloud_ngfw.NgfirewallsApi(api_client)
    region = 'region_example' # str | The AWS region where the Cloud NGFW firewall is deployed
    ngfirewall_create_request = scm.cloud_ngfw.NgfirewallCreateRequest() # NgfirewallCreateRequest | Firewall configuration

    try:
        # Create a Cloud NGFW firewall
        api_response = api_instance.create_ngfirewalls(region, ngfirewall_create_request)
        print("The response of NgfirewallsApi->create_ngfirewalls:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NgfirewallsApi->create_ngfirewalls: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **region** | **str**| The AWS region where the Cloud NGFW firewall is deployed | 
 **ngfirewall_create_request** | [**NgfirewallCreateRequest**](NgfirewallCreateRequest.md)| Firewall configuration | 

### Return type

[**NgfirewallCreateResponse**](NgfirewallCreateResponse.md)

### Authorization

[scmToken](../README.md#scmToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Created |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**0** | General Errors |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_ngfirewalls_by_id**
> delete_ngfirewalls_by_id(id, region, source=source)

Delete a Cloud NGFW firewall.

Deletes a Cloud NGFW firewall. Use DeleteCloudNGFirewall (Go SDK) or delete_cloud_ng_firewall (Python SDK) instead. 

### Example

* Bearer (JWT) Authentication (scmToken):

```python
import scm.cloud_ngfw
from scm.cloud_ngfw.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.strata.paloaltonetworks.com
# See configuration.py for a list of all supported configuration parameters.
configuration = scm.cloud_ngfw.Configuration(
    host = "https://api.strata.paloaltonetworks.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): scmToken
configuration = scm.cloud_ngfw.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with scm.cloud_ngfw.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = scm.cloud_ngfw.NgfirewallsApi(api_client)
    id = 'id_example' # str | The ID of the Cloud NGFW firewall.
    region = 'region_example' # str | The AWS region where the Cloud NGFW firewall is deployed
    source = 'source_example' # str | Identifies the client that originated the request (e.g. SCM-SDK, Terraform-Provider-SCM). (optional)

    try:
        # Delete a Cloud NGFW firewall.
        api_instance.delete_ngfirewalls_by_id(id, region, source=source)
    except Exception as e:
        print("Exception when calling NgfirewallsApi->delete_ngfirewalls_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the Cloud NGFW firewall. | 
 **region** | **str**| The AWS region where the Cloud NGFW firewall is deployed | 
 **source** | **str**| Identifies the client that originated the request (e.g. SCM-SDK, Terraform-Provider-SCM). | [optional] 

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
**0** | General Errors |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_ngfirewalls_by_id**
> Ngfirewalls get_ngfirewalls_by_id(id, region)

Get a Cloud NGFW firewall

Retrieve details of a specific Cloud NGFW firewall by its ID. 

### Example

* Bearer (JWT) Authentication (scmToken):

```python
import scm.cloud_ngfw
from scm.cloud_ngfw.models.ngfirewalls import Ngfirewalls
from scm.cloud_ngfw.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.strata.paloaltonetworks.com
# See configuration.py for a list of all supported configuration parameters.
configuration = scm.cloud_ngfw.Configuration(
    host = "https://api.strata.paloaltonetworks.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): scmToken
configuration = scm.cloud_ngfw.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with scm.cloud_ngfw.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = scm.cloud_ngfw.NgfirewallsApi(api_client)
    id = 'id_example' # str | The ID of the Cloud NGFW firewall.
    region = 'region_example' # str | The AWS region where the Cloud NGFW firewall is deployed

    try:
        # Get a Cloud NGFW firewall
        api_response = api_instance.get_ngfirewalls_by_id(id, region)
        print("The response of NgfirewallsApi->get_ngfirewalls_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NgfirewallsApi->get_ngfirewalls_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the Cloud NGFW firewall. | 
 **region** | **str**| The AWS region where the Cloud NGFW firewall is deployed | 

### Return type

[**Ngfirewalls**](Ngfirewalls.md)

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

# **list_ngfirewalls**
> NgfirewallsListResponse list_ngfirewalls(region, globalrulestackname=globalrulestackname, describe=describe)

List Cloud NGFW firewalls

List Cloud NGFW firewalls with optional filtering parameters. Use ListCloudNGFirewalls (Go SDK) or list_cloud_ng_firewalls (Python SDK) instead; they return the complete list across all pages. 

### Example

* Bearer (JWT) Authentication (scmToken):

```python
import scm.cloud_ngfw
from scm.cloud_ngfw.models.ngfirewalls_list_response import NgfirewallsListResponse
from scm.cloud_ngfw.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.strata.paloaltonetworks.com
# See configuration.py for a list of all supported configuration parameters.
configuration = scm.cloud_ngfw.Configuration(
    host = "https://api.strata.paloaltonetworks.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): scmToken
configuration = scm.cloud_ngfw.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with scm.cloud_ngfw.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = scm.cloud_ngfw.NgfirewallsApi(api_client)
    region = 'region_example' # str | The AWS region where the Cloud NGFW firewall is deployed
    globalrulestackname = 'globalrulestackname_example' # str | Name of the global rulestack to filter by. (optional)
    describe = 'describe_example' # str | Controls how much detail the list response contains. Use ListCloudNGFirewalls (Go SDK) or list_cloud_ng_firewalls (Python SDK), which always request the detailed listing (describe=true) and return it in FirewallsDescribe. Calling the raw list method with describe=false returns only a summary that this SDK does not expose.  (optional)

    try:
        # List Cloud NGFW firewalls
        api_response = api_instance.list_ngfirewalls(region, globalrulestackname=globalrulestackname, describe=describe)
        print("The response of NgfirewallsApi->list_ngfirewalls:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NgfirewallsApi->list_ngfirewalls: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **region** | **str**| The AWS region where the Cloud NGFW firewall is deployed | 
 **globalrulestackname** | **str**| Name of the global rulestack to filter by. | [optional] 
 **describe** | **str**| Controls how much detail the list response contains. Use ListCloudNGFirewalls (Go SDK) or list_cloud_ng_firewalls (Python SDK), which always request the detailed listing (describe&#x3D;true) and return it in FirewallsDescribe. Calling the raw list method with describe&#x3D;false returns only a summary that this SDK does not expose.  | [optional] 

### Return type

[**NgfirewallsListResponse**](NgfirewallsListResponse.md)

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
**0** | General Errors |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_ngfirewalls_by_id**
> NgfirewallUpdateResponse update_ngfirewalls_by_id(id, region, ngfirewall_update_request)

Update a Cloud NGFW firewall

Update an existing Cloud NGFW firewall. Supports updating Tags, Description, Tier (upgrade only: standard to premium), AllowListAccounts, ChangeProtection, CustomerZoneIdList, EgressNAT, ScmLabels, LinkId, GwlbTcpIdleTimeout, PrivateAccess, Endpoints, and UserID. The request must include the UpdateToken and DeploymentUpdateToken values from a recent GET of the same firewall. 

### Example

* Bearer (JWT) Authentication (scmToken):

```python
import scm.cloud_ngfw
from scm.cloud_ngfw.models.ngfirewall_update_request import NgfirewallUpdateRequest
from scm.cloud_ngfw.models.ngfirewall_update_response import NgfirewallUpdateResponse
from scm.cloud_ngfw.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.strata.paloaltonetworks.com
# See configuration.py for a list of all supported configuration parameters.
configuration = scm.cloud_ngfw.Configuration(
    host = "https://api.strata.paloaltonetworks.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): scmToken
configuration = scm.cloud_ngfw.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with scm.cloud_ngfw.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = scm.cloud_ngfw.NgfirewallsApi(api_client)
    id = 'id_example' # str | The ID of the Cloud NGFW firewall.
    region = 'region_example' # str | The AWS region where the Cloud NGFW firewall is deployed
    ngfirewall_update_request = scm.cloud_ngfw.NgfirewallUpdateRequest() # NgfirewallUpdateRequest | Firewall configuration

    try:
        # Update a Cloud NGFW firewall
        api_response = api_instance.update_ngfirewalls_by_id(id, region, ngfirewall_update_request)
        print("The response of NgfirewallsApi->update_ngfirewalls_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NgfirewallsApi->update_ngfirewalls_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the Cloud NGFW firewall. | 
 **region** | **str**| The AWS region where the Cloud NGFW firewall is deployed | 
 **ngfirewall_update_request** | [**NgfirewallUpdateRequest**](NgfirewallUpdateRequest.md)| Firewall configuration | 

### Return type

[**NgfirewallUpdateResponse**](NgfirewallUpdateResponse.md)

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
**0** | General Errors |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

