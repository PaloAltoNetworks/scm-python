# SnippetShareProperty


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created** | **datetime** |  | [optional] [readonly] 
**created_by** | **str** |  | [optional] [readonly] 
**donor_tenant** | **str** |  | [optional] [readonly] 
**donor_tsg** | **str** |  | [optional] [readonly] 
**error** | **str** |  | [optional] [readonly] 
**id** | **int** |  | [optional] [readonly] 
**msg_uuid** | **str** |  | [optional] [readonly] 
**property_name** | **str** |  | [optional] [readonly] 
**property_value** | **str** |  | [optional] [readonly] 
**recipient_tenant** | **str** |  | [optional] [readonly] 
**recipient_tsg** | **str** |  | [optional] [readonly] 
**snippet_name** | **str** |  | [optional] [readonly] 
**snippet_uuid** | **str** |  | [optional] [readonly] 
**status** | **str** |  | [optional] [readonly] 
**updated** | **datetime** |  | [optional] [readonly] 
**updated_by** | **str** |  | [optional] [readonly] 

## Example

```python
from scm.config_setup.models.snippet_share_property import SnippetShareProperty

# TODO update the JSON string below
json = "{}"
# create an instance of SnippetShareProperty from a JSON string
snippet_share_property_instance = SnippetShareProperty.from_json(json)
# print the JSON string representation of the object
print(SnippetShareProperty.to_json())

# convert the object into a dict
snippet_share_property_dict = snippet_share_property_instance.to_dict()
# create an instance of SnippetShareProperty from a dict
snippet_share_property_from_dict = SnippetShareProperty.from_dict(snippet_share_property_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


