# SnippetSnapshotLoadSnippetPayload


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**version** | **str** |  | 

## Example

```python
from scm.config_setup.models.snippet_snapshot_load_snippet_payload import SnippetSnapshotLoadSnippetPayload

# TODO update the JSON string below
json = "{}"
# create an instance of SnippetSnapshotLoadSnippetPayload from a JSON string
snippet_snapshot_load_snippet_payload_instance = SnippetSnapshotLoadSnippetPayload.from_json(json)
# print the JSON string representation of the object
print(SnippetSnapshotLoadSnippetPayload.to_json())

# convert the object into a dict
snippet_snapshot_load_snippet_payload_dict = snippet_snapshot_load_snippet_payload_instance.to_dict()
# create an instance of SnippetSnapshotLoadSnippetPayload from a dict
snippet_snapshot_load_snippet_payload_from_dict = SnippetSnapshotLoadSnippetPayload.from_dict(snippet_snapshot_load_snippet_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


