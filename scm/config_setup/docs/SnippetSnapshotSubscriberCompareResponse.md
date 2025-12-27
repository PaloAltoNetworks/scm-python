# SnippetSnapshotSubscriberCompareResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**publisher** | [**SnippetSnapshotSubscriberCompareResponsePublisher**](SnippetSnapshotSubscriberCompareResponsePublisher.md) |  | [optional] 
**subscriber** | [**SnippetSnapshotSubscriberCompareResponsePublisher**](SnippetSnapshotSubscriberCompareResponsePublisher.md) |  | [optional] 

## Example

```python
from scm_config_setup.models.snippet_snapshot_subscriber_compare_response import SnippetSnapshotSubscriberCompareResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SnippetSnapshotSubscriberCompareResponse from a JSON string
snippet_snapshot_subscriber_compare_response_instance = SnippetSnapshotSubscriberCompareResponse.from_json(json)
# print the JSON string representation of the object
print(SnippetSnapshotSubscriberCompareResponse.to_json())

# convert the object into a dict
snippet_snapshot_subscriber_compare_response_dict = snippet_snapshot_subscriber_compare_response_instance.to_dict()
# create an instance of SnippetSnapshotSubscriberCompareResponse from a dict
snippet_snapshot_subscriber_compare_response_from_dict = SnippetSnapshotSubscriberCompareResponse.from_dict(snippet_snapshot_subscriber_compare_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


