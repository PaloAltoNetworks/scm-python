# SnippetShareInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created** | **datetime** |  | [optional] [readonly] 
**donor_created** | **int** |  | [optional] [readonly] 
**donor_snippet_file_id** | **int** |  | [optional] [readonly] 
**donor_snippet_version** | **int** |  | [optional] [readonly] 
**donor_tenant_id** | **str** |  | [optional] [readonly] 
**donor_tenant_name** | **str** |  | [optional] [readonly] 
**donor_tsg** | **str** |  | [optional] [readonly] 
**error** | **str** |  | [optional] [readonly] 
**id** | **int** |  | [optional] [readonly] 
**last_updated** | **datetime** |  | [optional] [readonly] 
**msg_uuid** | **str** |  | [optional] [readonly] 
**properties** | [**List[SnippetShareProperty]**](SnippetShareProperty.md) |  | [optional] 
**recipient_paused_update** | **bool** |  | [optional] [readonly] 
**recipient_snippet_file_id** | **int** |  | [optional] [readonly] 
**recipient_snippet_version** | **int** |  | [optional] [readonly] 
**recipient_tenant_id** | **str** |  | [optional] [readonly] 
**recipient_tenant_name** | **str** |  | [optional] [readonly] 
**recipient_tsg** | **str** |  | [optional] [readonly] 
**recipient_validate_before_update** | **bool** |  | [optional] [readonly] 
**snippet_name** | **str** |  | [optional] [readonly] 
**snippet_uuid** | **str** |  | [optional] [readonly] 
**status** | **str** |  | [optional] [readonly] 

## Example

```python
from scm_config_setup.models.snippet_share_info import SnippetShareInfo

# TODO update the JSON string below
json = "{}"
# create an instance of SnippetShareInfo from a JSON string
snippet_share_info_instance = SnippetShareInfo.from_json(json)
# print the JSON string representation of the object
print(SnippetShareInfo.to_json())

# convert the object into a dict
snippet_share_info_dict = snippet_share_info_instance.to_dict()
# create an instance of SnippetShareInfo from a dict
snippet_share_info_from_dict = SnippetShareInfo.from_dict(snippet_share_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


