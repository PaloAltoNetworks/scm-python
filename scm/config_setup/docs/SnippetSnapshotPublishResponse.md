# SnippetSnapshotPublishResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**file_id** | **int** |  | [optional] [readonly] 
**id** | **str** |  | [optional] [readonly] 
**job_id** | **int** |  | [optional] [readonly] 
**tsgs** | **List[str]** |  | [optional] [readonly] 
**version** | **int** |  | [optional] [readonly] 

## Example

```python
from scm.config_setup.models.snippet_snapshot_publish_response import SnippetSnapshotPublishResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SnippetSnapshotPublishResponse from a JSON string
snippet_snapshot_publish_response_instance = SnippetSnapshotPublishResponse.from_json(json)
# print the JSON string representation of the object
print(SnippetSnapshotPublishResponse.to_json())

# convert the object into a dict
snippet_snapshot_publish_response_dict = snippet_snapshot_publish_response_instance.to_dict()
# create an instance of SnippetSnapshotPublishResponse from a dict
snippet_snapshot_publish_response_from_dict = SnippetSnapshotPublishResponse.from_dict(snippet_snapshot_publish_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


