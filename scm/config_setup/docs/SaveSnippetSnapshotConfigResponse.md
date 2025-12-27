# SaveSnippetSnapshotConfigResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**result** | [**SaveSnippetSnapshotConfigResponseResult**](SaveSnippetSnapshotConfigResponseResult.md) |  | [optional] 
**status** | **str** |  | [optional] [readonly] 

## Example

```python
from scm_config_setup.models.save_snippet_snapshot_config_response import SaveSnippetSnapshotConfigResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SaveSnippetSnapshotConfigResponse from a JSON string
save_snippet_snapshot_config_response_instance = SaveSnippetSnapshotConfigResponse.from_json(json)
# print the JSON string representation of the object
print(SaveSnippetSnapshotConfigResponse.to_json())

# convert the object into a dict
save_snippet_snapshot_config_response_dict = save_snippet_snapshot_config_response_instance.to_dict()
# create an instance of SaveSnippetSnapshotConfigResponse from a dict
save_snippet_snapshot_config_response_from_dict = SaveSnippetSnapshotConfigResponse.from_dict(save_snippet_snapshot_config_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


