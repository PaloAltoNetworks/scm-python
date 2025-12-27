# SnippetCategories


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_in** | **datetime** |  | [optional] [readonly] 
**description** | **str** |  | [optional] [readonly] 
**display_name** | **str** |  | [optional] [readonly] 
**donor_created** | **int** |  | [optional] [readonly] 
**donor_snippet_file_id** | **int** |  | [optional] [readonly] 
**donor_snippet_version** | **int** |  | [optional] [readonly] 
**donor_tenant_id** | **str** |  | [optional] [readonly] 
**donor_tenant_name** | **str** |  | [optional] [readonly] 
**donor_tsg** | **str** |  | [optional] [readonly] 
**enable_prefix** | **bool** |  | [optional] [readonly] 
**error** | **str** |  | [optional] [readonly] 
**folders** | [**List[UsedFolders]**](UsedFolders.md) |  | [optional] 
**id** | **str** |  | [readonly] 
**labels** | **List[str]** |  | [optional] 
**last_update** | **datetime** |  | [optional] [readonly] 
**msg_uuid** | **str** |  | [optional] [readonly] 
**name** | **str** |  | [readonly] 
**prefix** | **str** |  | [optional] [readonly] 
**recipient_paused_update** | **bool** |  | [optional] [readonly] 
**recipient_tenant_id** | **str** |  | [optional] [readonly] 
**recipient_tenant_name** | **str** |  | [optional] [readonly] 
**recipient_tsg** | **str** |  | [optional] [readonly] 
**recipient_validate_before_update** | **bool** |  | [optional] [readonly] 
**shared_in** | **str** |  | [optional] [readonly] 
**snippet_uuid** | **str** |  | [optional] [readonly] 
**status** | **str** |  | [optional] [readonly] 
**type** | **str** |  | [optional] [readonly] 
**version** | **int** |  | [optional] [readonly] 

## Example

```python
from scm.config_setup.models.snippet_categories import SnippetCategories

# TODO update the JSON string below
json = "{}"
# create an instance of SnippetCategories from a JSON string
snippet_categories_instance = SnippetCategories.from_json(json)
# print the JSON string representation of the object
print(SnippetCategories.to_json())

# convert the object into a dict
snippet_categories_dict = snippet_categories_instance.to_dict()
# create an instance of SnippetCategories from a dict
snippet_categories_from_dict = SnippetCategories.from_dict(snippet_categories_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


