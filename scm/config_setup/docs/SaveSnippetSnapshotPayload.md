# SaveSnippetSnapshotPayload


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** |  | 
**id** | **str** |  | 

## Example

```python
from scm.config_setup.models.save_snippet_snapshot_payload import SaveSnippetSnapshotPayload

# TODO update the JSON string below
json = "{}"
# create an instance of SaveSnippetSnapshotPayload from a JSON string
save_snippet_snapshot_payload_instance = SaveSnippetSnapshotPayload.from_json(json)
# print the JSON string representation of the object
print(SaveSnippetSnapshotPayload.to_json())

# convert the object into a dict
save_snippet_snapshot_payload_dict = save_snippet_snapshot_payload_instance.to_dict()
# create an instance of SaveSnippetSnapshotPayload from a dict
save_snippet_snapshot_payload_from_dict = SaveSnippetSnapshotPayload.from_dict(save_snippet_snapshot_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


