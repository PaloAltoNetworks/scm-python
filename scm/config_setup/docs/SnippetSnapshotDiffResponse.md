# SnippetSnapshotDiffResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**after** | [**SnippetSnapshotDiffResponseAfter**](SnippetSnapshotDiffResponseAfter.md) |  | [optional] 
**before** | [**SnippetSnapshotDiffResponseBefore**](SnippetSnapshotDiffResponseBefore.md) |  | [optional] 

## Example

```python
from scm.config_setup.models.snippet_snapshot_diff_response import SnippetSnapshotDiffResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SnippetSnapshotDiffResponse from a JSON string
snippet_snapshot_diff_response_instance = SnippetSnapshotDiffResponse.from_json(json)
# print the JSON string representation of the object
print(SnippetSnapshotDiffResponse.to_json())

# convert the object into a dict
snippet_snapshot_diff_response_dict = snippet_snapshot_diff_response_instance.to_dict()
# create an instance of SnippetSnapshotDiffResponse from a dict
snippet_snapshot_diff_response_from_dict = SnippetSnapshotDiffResponse.from_dict(snippet_snapshot_diff_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


