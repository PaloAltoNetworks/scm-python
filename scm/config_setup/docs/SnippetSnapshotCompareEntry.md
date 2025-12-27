# SnippetSnapshotCompareEntry


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**admin** | **str** |  | [optional] [readonly] 
**id** | **str** |  | [optional] [readonly] 
**loc** | **str** |  | [optional] 
**loctype** | **str** |  | [optional] 
**objectname** | **str** |  | [optional] 
**objecttype** | **str** |  | [optional] 
**operations** | **str** |  | [optional] 
**timestamp** | **datetime** |  | [optional] 

## Example

```python
from scm_config_setup.models.snippet_snapshot_compare_entry import SnippetSnapshotCompareEntry

# TODO update the JSON string below
json = "{}"
# create an instance of SnippetSnapshotCompareEntry from a JSON string
snippet_snapshot_compare_entry_instance = SnippetSnapshotCompareEntry.from_json(json)
# print the JSON string representation of the object
print(SnippetSnapshotCompareEntry.to_json())

# convert the object into a dict
snippet_snapshot_compare_entry_dict = snippet_snapshot_compare_entry_instance.to_dict()
# create an instance of SnippetSnapshotCompareEntry from a dict
snippet_snapshot_compare_entry_from_dict = SnippetSnapshotCompareEntry.from_dict(snippet_snapshot_compare_entry_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


