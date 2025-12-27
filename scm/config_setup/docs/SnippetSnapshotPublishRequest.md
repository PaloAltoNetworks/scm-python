# SnippetSnapshotPublishRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**tsgs** | **List[str]** |  | [optional] 
**validation** | **bool** |  | [optional] 
**version** | **int** |  | [optional] 

## Example

```python
from scm.config_setup.models.snippet_snapshot_publish_request import SnippetSnapshotPublishRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SnippetSnapshotPublishRequest from a JSON string
snippet_snapshot_publish_request_instance = SnippetSnapshotPublishRequest.from_json(json)
# print the JSON string representation of the object
print(SnippetSnapshotPublishRequest.to_json())

# convert the object into a dict
snippet_snapshot_publish_request_dict = snippet_snapshot_publish_request_instance.to_dict()
# create an instance of SnippetSnapshotPublishRequest from a dict
snippet_snapshot_publish_request_from_dict = SnippetSnapshotPublishRequest.from_dict(snippet_snapshot_publish_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


