# CompareSnippetSnapshotConfigPayload


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**comparing_version** | **int** |  | 
**id** | **str** |  | 
**version** | **int** |  | 

## Example

```python
from scm_config_setup.models.compare_snippet_snapshot_config_payload import CompareSnippetSnapshotConfigPayload

# TODO update the JSON string below
json = "{}"
# create an instance of CompareSnippetSnapshotConfigPayload from a JSON string
compare_snippet_snapshot_config_payload_instance = CompareSnippetSnapshotConfigPayload.from_json(json)
# print the JSON string representation of the object
print(CompareSnippetSnapshotConfigPayload.to_json())

# convert the object into a dict
compare_snippet_snapshot_config_payload_dict = compare_snippet_snapshot_config_payload_instance.to_dict()
# create an instance of CompareSnippetSnapshotConfigPayload from a dict
compare_snippet_snapshot_config_payload_from_dict = CompareSnippetSnapshotConfigPayload.from_dict(compare_snippet_snapshot_config_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


