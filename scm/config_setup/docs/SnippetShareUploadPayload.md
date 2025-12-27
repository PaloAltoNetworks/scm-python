# SnippetShareUploadPayload


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**pause_update** | **bool** |  | [optional] 
**validate_before_update** | **bool** |  | [optional] 

## Example

```python
from scm_config_setup.models.snippet_share_upload_payload import SnippetShareUploadPayload

# TODO update the JSON string below
json = "{}"
# create an instance of SnippetShareUploadPayload from a JSON string
snippet_share_upload_payload_instance = SnippetShareUploadPayload.from_json(json)
# print the JSON string representation of the object
print(SnippetShareUploadPayload.to_json())

# convert the object into a dict
snippet_share_upload_payload_dict = snippet_share_upload_payload_instance.to_dict()
# create an instance of SnippetShareUploadPayload from a dict
snippet_share_upload_payload_from_dict = SnippetShareUploadPayload.from_dict(snippet_share_upload_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


