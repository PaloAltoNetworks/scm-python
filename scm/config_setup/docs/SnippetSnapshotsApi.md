# scm_config_setup.SnippetSnapshotsApi

All URIs are relative to *https://api.strata.paloaltonetworks.com/config/setup/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**compare_snippet_snapshot**](SnippetSnapshotsApi.md#compare_snippet_snapshot) | **POST** /snippet-snapshots:compare | Compare Snippet Snapshots
[**convert_snippet_snapshot**](SnippetSnapshotsApi.md#convert_snippet_snapshot) | **POST** /snippet-snapshots:convert | Convert Snippet Snapshots
[**diff_snippet_snapshot**](SnippetSnapshotsApi.md#diff_snippet_snapshot) | **POST** /snippet-snapshots:diff | Diff Snippet Snapshots
[**load_snippet_snapshot**](SnippetSnapshotsApi.md#load_snippet_snapshot) | **POST** /snippet-snapshots:load | Load Snippet Snapshots
[**publish_snippet_snapshot**](SnippetSnapshotsApi.md#publish_snippet_snapshot) | **POST** /snippet-snapshots:publish | Publish Snippet Snapshots
[**save_snippet_snapshot**](SnippetSnapshotsApi.md#save_snippet_snapshot) | **POST** /snippet-snapshots | Save Snippet Snapshots
[**update_snippet_snapshot**](SnippetSnapshotsApi.md#update_snippet_snapshot) | **POST** /snippet-snapshots:updates | Update Snippet Snapshots


# **compare_snippet_snapshot**
> List[SnippetSnapshotCompareEntry] compare_snippet_snapshot(compare_snippet_snapshot_config_payload=compare_snippet_snapshot_config_payload)

Compare Snippet Snapshots

Compare Snippet Snapshots. 

### Example

* Bearer (JWT) Authentication (scmToken):

```python
import scm_config_setup
from scm_config_setup.models.compare_snippet_snapshot_config_payload import CompareSnippetSnapshotConfigPayload
from scm_config_setup.models.snippet_snapshot_compare_entry import SnippetSnapshotCompareEntry
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
    api_instance = scm_config_setup.SnippetSnapshotsApi(api_client)
    compare_snippet_snapshot_config_payload = scm_config_setup.CompareSnippetSnapshotConfigPayload() # CompareSnippetSnapshotConfigPayload | The `Snippet Snapshots To Compare` resource definition (optional)

    try:
        # Compare Snippet Snapshots
        api_response = api_instance.compare_snippet_snapshot(compare_snippet_snapshot_config_payload=compare_snippet_snapshot_config_payload)
        print("The response of SnippetSnapshotsApi->compare_snippet_snapshot:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SnippetSnapshotsApi->compare_snippet_snapshot: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **compare_snippet_snapshot_config_payload** | [**CompareSnippetSnapshotConfigPayload**](CompareSnippetSnapshotConfigPayload.md)| The &#x60;Snippet Snapshots To Compare&#x60; resource definition | [optional] 

### Return type

[**List[SnippetSnapshotCompareEntry]**](SnippetSnapshotCompareEntry.md)

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

# **convert_snippet_snapshot**
> object convert_snippet_snapshot(common_snippet_snapshot_payload=common_snippet_snapshot_payload)

Convert Snippet Snapshots

Convert Snippet Snapshots. 

### Example

* Bearer (JWT) Authentication (scmToken):

```python
import scm_config_setup
from scm_config_setup.models.common_snippet_snapshot_payload import CommonSnippetSnapshotPayload
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
    api_instance = scm_config_setup.SnippetSnapshotsApi(api_client)
    common_snippet_snapshot_payload = scm_config_setup.CommonSnippetSnapshotPayload() # CommonSnippetSnapshotPayload | The `Snippet Snapshots To Convert` resource definition (optional)

    try:
        # Convert Snippet Snapshots
        api_response = api_instance.convert_snippet_snapshot(common_snippet_snapshot_payload=common_snippet_snapshot_payload)
        print("The response of SnippetSnapshotsApi->convert_snippet_snapshot:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SnippetSnapshotsApi->convert_snippet_snapshot: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **common_snippet_snapshot_payload** | [**CommonSnippetSnapshotPayload**](CommonSnippetSnapshotPayload.md)| The &#x60;Snippet Snapshots To Convert&#x60; resource definition | [optional] 

### Return type

**object**

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

# **diff_snippet_snapshot**
> SnippetSnapshotDiffResponse diff_snippet_snapshot(compare_tlo_payload=compare_tlo_payload)

Diff Snippet Snapshots

Diff Snippet Snapshots. 

### Example

* Bearer (JWT) Authentication (scmToken):

```python
import scm_config_setup
from scm_config_setup.models.compare_tlo_payload import CompareTloPayload
from scm_config_setup.models.snippet_snapshot_diff_response import SnippetSnapshotDiffResponse
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
    api_instance = scm_config_setup.SnippetSnapshotsApi(api_client)
    compare_tlo_payload = scm_config_setup.CompareTloPayload() # CompareTloPayload | The `Snippet Snapshots To Differentiate` resource definition (optional)

    try:
        # Diff Snippet Snapshots
        api_response = api_instance.diff_snippet_snapshot(compare_tlo_payload=compare_tlo_payload)
        print("The response of SnippetSnapshotsApi->diff_snippet_snapshot:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SnippetSnapshotsApi->diff_snippet_snapshot: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **compare_tlo_payload** | [**CompareTloPayload**](CompareTloPayload.md)| The &#x60;Snippet Snapshots To Differentiate&#x60; resource definition | [optional] 

### Return type

[**SnippetSnapshotDiffResponse**](SnippetSnapshotDiffResponse.md)

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

# **load_snippet_snapshot**
> SnippetSnapshotLoadSnippetResponse load_snippet_snapshot(snippet_snapshot_load_snippet_payload=snippet_snapshot_load_snippet_payload)

Load Snippet Snapshots

Load Snippet Snapshots. 

### Example

* Bearer (JWT) Authentication (scmToken):

```python
import scm_config_setup
from scm_config_setup.models.snippet_snapshot_load_snippet_payload import SnippetSnapshotLoadSnippetPayload
from scm_config_setup.models.snippet_snapshot_load_snippet_response import SnippetSnapshotLoadSnippetResponse
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
    api_instance = scm_config_setup.SnippetSnapshotsApi(api_client)
    snippet_snapshot_load_snippet_payload = scm_config_setup.SnippetSnapshotLoadSnippetPayload() # SnippetSnapshotLoadSnippetPayload | The `Snippet Snapshots To Load` resource definition (optional)

    try:
        # Load Snippet Snapshots
        api_response = api_instance.load_snippet_snapshot(snippet_snapshot_load_snippet_payload=snippet_snapshot_load_snippet_payload)
        print("The response of SnippetSnapshotsApi->load_snippet_snapshot:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SnippetSnapshotsApi->load_snippet_snapshot: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **snippet_snapshot_load_snippet_payload** | [**SnippetSnapshotLoadSnippetPayload**](SnippetSnapshotLoadSnippetPayload.md)| The &#x60;Snippet Snapshots To Load&#x60; resource definition | [optional] 

### Return type

[**SnippetSnapshotLoadSnippetResponse**](SnippetSnapshotLoadSnippetResponse.md)

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

# **publish_snippet_snapshot**
> SnippetSnapshotPublishResponse publish_snippet_snapshot(snippet_snapshot_publish_request=snippet_snapshot_publish_request)

Publish Snippet Snapshots

Publish Snippet Snapshots. 

### Example

* Bearer (JWT) Authentication (scmToken):

```python
import scm_config_setup
from scm_config_setup.models.snippet_snapshot_publish_request import SnippetSnapshotPublishRequest
from scm_config_setup.models.snippet_snapshot_publish_response import SnippetSnapshotPublishResponse
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
    api_instance = scm_config_setup.SnippetSnapshotsApi(api_client)
    snippet_snapshot_publish_request = scm_config_setup.SnippetSnapshotPublishRequest() # SnippetSnapshotPublishRequest | The `Snippet Snapshots To Publish` resource definition (optional)

    try:
        # Publish Snippet Snapshots
        api_response = api_instance.publish_snippet_snapshot(snippet_snapshot_publish_request=snippet_snapshot_publish_request)
        print("The response of SnippetSnapshotsApi->publish_snippet_snapshot:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SnippetSnapshotsApi->publish_snippet_snapshot: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **snippet_snapshot_publish_request** | [**SnippetSnapshotPublishRequest**](SnippetSnapshotPublishRequest.md)| The &#x60;Snippet Snapshots To Publish&#x60; resource definition | [optional] 

### Return type

[**SnippetSnapshotPublishResponse**](SnippetSnapshotPublishResponse.md)

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

# **save_snippet_snapshot**
> SaveSnippetSnapshotConfigResponse save_snippet_snapshot(save_snippet_snapshot_payload=save_snippet_snapshot_payload)

Save Snippet Snapshots

Save Snippet Snapshots. 

### Example

* Bearer (JWT) Authentication (scmToken):

```python
import scm_config_setup
from scm_config_setup.models.save_snippet_snapshot_config_response import SaveSnippetSnapshotConfigResponse
from scm_config_setup.models.save_snippet_snapshot_payload import SaveSnippetSnapshotPayload
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
    api_instance = scm_config_setup.SnippetSnapshotsApi(api_client)
    save_snippet_snapshot_payload = scm_config_setup.SaveSnippetSnapshotPayload() # SaveSnippetSnapshotPayload | The `Save Snippet Snapshots` resource definition (optional)

    try:
        # Save Snippet Snapshots
        api_response = api_instance.save_snippet_snapshot(save_snippet_snapshot_payload=save_snippet_snapshot_payload)
        print("The response of SnippetSnapshotsApi->save_snippet_snapshot:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SnippetSnapshotsApi->save_snippet_snapshot: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **save_snippet_snapshot_payload** | [**SaveSnippetSnapshotPayload**](SaveSnippetSnapshotPayload.md)| The &#x60;Save Snippet Snapshots&#x60; resource definition | [optional] 

### Return type

[**SaveSnippetSnapshotConfigResponse**](SaveSnippetSnapshotConfigResponse.md)

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

# **update_snippet_snapshot**
> SnippetSnapshotSubscriberCompareResponse update_snippet_snapshot(snippet_snapshot_subscriber_compare_payload=snippet_snapshot_subscriber_compare_payload)

Update Snippet Snapshots

Update Snippet Snapshots. 

### Example

* Bearer (JWT) Authentication (scmToken):

```python
import scm_config_setup
from scm_config_setup.models.snippet_snapshot_subscriber_compare_payload import SnippetSnapshotSubscriberComparePayload
from scm_config_setup.models.snippet_snapshot_subscriber_compare_response import SnippetSnapshotSubscriberCompareResponse
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
    api_instance = scm_config_setup.SnippetSnapshotsApi(api_client)
    snippet_snapshot_subscriber_compare_payload = scm_config_setup.SnippetSnapshotSubscriberComparePayload() # SnippetSnapshotSubscriberComparePayload | The `Snippet Snapshots To Update` resource definition (optional)

    try:
        # Update Snippet Snapshots
        api_response = api_instance.update_snippet_snapshot(snippet_snapshot_subscriber_compare_payload=snippet_snapshot_subscriber_compare_payload)
        print("The response of SnippetSnapshotsApi->update_snippet_snapshot:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SnippetSnapshotsApi->update_snippet_snapshot: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **snippet_snapshot_subscriber_compare_payload** | [**SnippetSnapshotSubscriberComparePayload**](SnippetSnapshotSubscriberComparePayload.md)| The &#x60;Snippet Snapshots To Update&#x60; resource definition | [optional] 

### Return type

[**SnippetSnapshotSubscriberCompareResponse**](SnippetSnapshotSubscriberCompareResponse.md)

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

