# CommonSnippetSnapshotPayload


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**keep_local** | **bool** |  | [optional] 

## Example

```python
from scm_config_setup.models.common_snippet_snapshot_payload import CommonSnippetSnapshotPayload

# TODO update the JSON string below
json = "{}"
# create an instance of CommonSnippetSnapshotPayload from a JSON string
common_snippet_snapshot_payload_instance = CommonSnippetSnapshotPayload.from_json(json)
# print the JSON string representation of the object
print(CommonSnippetSnapshotPayload.to_json())

# convert the object into a dict
common_snippet_snapshot_payload_dict = common_snippet_snapshot_payload_instance.to_dict()
# create an instance of CommonSnippetSnapshotPayload from a dict
common_snippet_snapshot_payload_from_dict = CommonSnippetSnapshotPayload.from_dict(common_snippet_snapshot_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


