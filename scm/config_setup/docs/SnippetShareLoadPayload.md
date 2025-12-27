# SnippetShareLoadPayload


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**validation** | **bool** |  | [optional] 

## Example

```python
from scm_config_setup.models.snippet_share_load_payload import SnippetShareLoadPayload

# TODO update the JSON string below
json = "{}"
# create an instance of SnippetShareLoadPayload from a JSON string
snippet_share_load_payload_instance = SnippetShareLoadPayload.from_json(json)
# print the JSON string representation of the object
print(SnippetShareLoadPayload.to_json())

# convert the object into a dict
snippet_share_load_payload_dict = snippet_share_load_payload_instance.to_dict()
# create an instance of SnippetShareLoadPayload from a dict
snippet_share_load_payload_from_dict = SnippetShareLoadPayload.from_dict(snippet_share_load_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


