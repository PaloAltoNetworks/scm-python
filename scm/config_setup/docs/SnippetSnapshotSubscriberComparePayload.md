# SnippetSnapshotSubscriberComparePayload


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**tenant_id** | **str** | Publisher Tenant ID | 

## Example

```python
from scm.config_setup.models.snippet_snapshot_subscriber_compare_payload import SnippetSnapshotSubscriberComparePayload

# TODO update the JSON string below
json = "{}"
# create an instance of SnippetSnapshotSubscriberComparePayload from a JSON string
snippet_snapshot_subscriber_compare_payload_instance = SnippetSnapshotSubscriberComparePayload.from_json(json)
# print the JSON string representation of the object
print(SnippetSnapshotSubscriberComparePayload.to_json())

# convert the object into a dict
snippet_snapshot_subscriber_compare_payload_dict = snippet_snapshot_subscriber_compare_payload_instance.to_dict()
# create an instance of SnippetSnapshotSubscriberComparePayload from a dict
snippet_snapshot_subscriber_compare_payload_from_dict = SnippetSnapshotSubscriberComparePayload.from_dict(snippet_snapshot_subscriber_compare_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


