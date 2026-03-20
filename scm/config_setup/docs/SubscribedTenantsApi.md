# scm.config_setup.SubscribedTenantsApi

All URIs are relative to *https://api.strata.paloaltonetworks.com/config/setup/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_subscribed_tenant**](SubscribedTenantsApi.md#create_subscribed_tenant) | **POST** /subscribed-tenants | Create Subscribed Tenant
[**delete_subscribed_tenant_by_snipped_id**](SubscribedTenantsApi.md#delete_subscribed_tenant_by_snipped_id) | **DELETE** /subscribed-tenants | Delete a subscribed tenant
[**list_subscribed_tenants_by_id**](SubscribedTenantsApi.md#list_subscribed_tenants_by_id) | **GET** /subscribed-tenants/{id} | Get Subscribed Tenants
[**update_subscribed_tenant_by_snippet_id**](SubscribedTenantsApi.md#update_subscribed_tenant_by_snippet_id) | **PUT** /subscribed-tenants | Update a subscribed tenant


# **create_subscribed_tenant**
> TenantTrustInfo create_subscribed_tenant(add_subscriber_request_payload_inner=add_subscriber_request_payload_inner)

Create Subscribed Tenant

Create Subscribed Tenant. 

### Example

* Bearer (JWT) Authentication (scmToken):

```python
import scm.config_setup
from scm.config_setup.models.add_subscriber_request_payload_inner import AddSubscriberRequestPayloadInner
from scm.config_setup.models.tenant_trust_info import TenantTrustInfo
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
    api_instance = scm.config_setup.SubscribedTenantsApi(api_client)
    add_subscriber_request_payload_inner = [scm.config_setup.AddSubscriberRequestPayloadInner()] # List[AddSubscriberRequestPayloadInner] | The `Subscribed Tenant` resource definition (optional)

    try:
        # Create Subscribed Tenant
        api_response = api_instance.create_subscribed_tenant(add_subscriber_request_payload_inner=add_subscriber_request_payload_inner)
        print("The response of SubscribedTenantsApi->create_subscribed_tenant:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SubscribedTenantsApi->create_subscribed_tenant: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **add_subscriber_request_payload_inner** | [**List[AddSubscriberRequestPayloadInner]**](AddSubscriberRequestPayloadInner.md)| The &#x60;Subscribed Tenant&#x60; resource definition | [optional] 

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

# **delete_subscribed_tenant_by_snipped_id**
> delete_subscribed_tenant_by_snipped_id(snippet_id, tsgs)

Delete a subscribed tenant

Delete an existing subscribed tenant. 

### Example

* Bearer (JWT) Authentication (scmToken):

```python
import scm.config_setup
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
    api_instance = scm.config_setup.SubscribedTenantsApi(api_client)
    snippet_id = 'snippet_id_example' # str | The ID of the snippet 
    tsgs = 'tsgs_example' # str | Comma-separated list of recipient TSG IDs 

    try:
        # Delete a subscribed tenant
        api_instance.delete_subscribed_tenant_by_snipped_id(snippet_id, tsgs)
    except Exception as e:
        print("Exception when calling SubscribedTenantsApi->delete_subscribed_tenant_by_snipped_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **snippet_id** | **str**| The ID of the snippet  | 
 **tsgs** | **str**| Comma-separated list of recipient TSG IDs  | 

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

# **list_subscribed_tenants_by_id**
> List[SnippetShareInfo] list_subscribed_tenants_by_id(id)

Get Subscribed Tenants

Retrieve a list of subscribed tenants. 

### Example

* Bearer (JWT) Authentication (scmToken):

```python
import scm.config_setup
from scm.config_setup.models.snippet_share_info import SnippetShareInfo
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
    api_instance = scm.config_setup.SubscribedTenantsApi(api_client)
    id = 'id_example' # str | The UUID of the resource

    try:
        # Get Subscribed Tenants
        api_response = api_instance.list_subscribed_tenants_by_id(id)
        print("The response of SubscribedTenantsApi->list_subscribed_tenants_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SubscribedTenantsApi->list_subscribed_tenants_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The UUID of the resource | 

### Return type

[**List[SnippetShareInfo]**](SnippetShareInfo.md)

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

# **update_subscribed_tenant_by_snippet_id**
> SubscriberPropertyPayload update_subscribed_tenant_by_snippet_id(subscriber_property_payload=subscriber_property_payload)

Update a subscribed tenant

Update an existing subscribed tenant. 

### Example

* Bearer (JWT) Authentication (scmToken):

```python
import scm.config_setup
from scm.config_setup.models.subscriber_property_payload import SubscriberPropertyPayload
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
    api_instance = scm.config_setup.SubscribedTenantsApi(api_client)
    subscriber_property_payload = scm.config_setup.SubscriberPropertyPayload() # SubscriberPropertyPayload | The `subscribed tenant` resource definition. (optional)

    try:
        # Update a subscribed tenant
        api_response = api_instance.update_subscribed_tenant_by_snippet_id(subscriber_property_payload=subscriber_property_payload)
        print("The response of SubscribedTenantsApi->update_subscribed_tenant_by_snippet_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SubscribedTenantsApi->update_subscribed_tenant_by_snippet_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscriber_property_payload** | [**SubscriberPropertyPayload**](SubscriberPropertyPayload.md)| The &#x60;subscribed tenant&#x60; resource definition. | [optional] 

### Return type

[**SubscriberPropertyPayload**](SubscriberPropertyPayload.md)

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

