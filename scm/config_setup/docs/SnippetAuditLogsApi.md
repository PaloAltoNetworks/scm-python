# scm_config_setup.SnippetAuditLogsApi

All URIs are relative to *https://api.strata.paloaltonetworks.com/config/setup/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_snippet_audit_logs**](SnippetAuditLogsApi.md#create_snippet_audit_logs) | **POST** /snippet-audit-logs | Create snippet audit logs configuration
[**get_snippet_audit_logs_by_id**](SnippetAuditLogsApi.md#get_snippet_audit_logs_by_id) | **GET** /snippet-audit-logs/{id} | Get a snippet audit logs


# **create_snippet_audit_logs**
> SnippetAuditHistory create_snippet_audit_logs(snippet_audit_payload=snippet_audit_payload)

Create snippet audit logs configuration

Create snippet audit logs configuration. 

### Example

* Bearer (JWT) Authentication (scmToken):

```python
import scm_config_setup
from scm_config_setup.models.snippet_audit_history import SnippetAuditHistory
from scm_config_setup.models.snippet_audit_payload import SnippetAuditPayload
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
    api_instance = scm_config_setup.SnippetAuditLogsApi(api_client)
    snippet_audit_payload = scm_config_setup.SnippetAuditPayload() # SnippetAuditPayload | The `Snippet Snapshots To Convert` resource definition (optional)

    try:
        # Create snippet audit logs configuration
        api_response = api_instance.create_snippet_audit_logs(snippet_audit_payload=snippet_audit_payload)
        print("The response of SnippetAuditLogsApi->create_snippet_audit_logs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SnippetAuditLogsApi->create_snippet_audit_logs: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **snippet_audit_payload** | [**SnippetAuditPayload**](SnippetAuditPayload.md)| The &#x60;Snippet Snapshots To Convert&#x60; resource definition | [optional] 

### Return type

[**SnippetAuditHistory**](SnippetAuditHistory.md)

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

# **get_snippet_audit_logs_by_id**
> SnippetAuditHistory get_snippet_audit_logs_by_id(id, type)

Get a snippet audit logs

Retrieve an existing snippet audit logs by UUID. 

### Example

* Bearer (JWT) Authentication (scmToken):

```python
import scm_config_setup
from scm_config_setup.models.snippet_audit_history import SnippetAuditHistory
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
    api_instance = scm_config_setup.SnippetAuditLogsApi(api_client)
    id = 'id_example' # str | The UUID of the resource
    type = 'type_example' # str | Specifies the type of the tenant that is trusted, either 'subscriber' or 'publisher'. 

    try:
        # Get a snippet audit logs
        api_response = api_instance.get_snippet_audit_logs_by_id(id, type)
        print("The response of SnippetAuditLogsApi->get_snippet_audit_logs_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SnippetAuditLogsApi->get_snippet_audit_logs_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The UUID of the resource | 
 **type** | **str**| Specifies the type of the tenant that is trusted, either &#39;subscriber&#39; or &#39;publisher&#39;.  | 

### Return type

[**SnippetAuditHistory**](SnippetAuditHistory.md)

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

