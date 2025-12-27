# TrustInfoWithSharedSnippets


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created** | **datetime** |  | [optional] [readonly] 
**donor_created** | **int** |  | [optional] [readonly] 
**donor_snippet_file_id** | **int** |  | [optional] [readonly] 
**donor_snippet_version** | **int** |  | [optional] [readonly] 
**donor_tsg** | **str** |  | [optional] [readonly] 
**error** | **str** |  | [optional] [readonly] 
**id** | **int** |  | [optional] [readonly] 
**last_updated** | **datetime** |  | [optional] [readonly] 
**msg_uuid** | **str** |  | [optional] [readonly] 
**recipient_paused_update** | **int** |  | [optional] [readonly] 
**recipient_snippet_file_id** | **int** |  | [optional] [readonly] 
**recipient_snippet_version** | **int** |  | [optional] [readonly] 
**recipient_tsg** | **str** |  | [optional] [readonly] 
**recipient_validate_before_update** | **int** |  | [optional] [readonly] 
**shared_snippets** | [**List[SnippetShareInfo]**](SnippetShareInfo.md) |  | [optional] 
**snippet_name** | **str** |  | [optional] [readonly] 
**snippet_uuid** | **str** |  | [optional] [readonly] 
**status** | **str** |  | [optional] [readonly] 
**updated_by** | **str** |  | [optional] [readonly] 

## Example

```python
from scm_config_setup.models.trust_info_with_shared_snippets import TrustInfoWithSharedSnippets

# TODO update the JSON string below
json = "{}"
# create an instance of TrustInfoWithSharedSnippets from a JSON string
trust_info_with_shared_snippets_instance = TrustInfoWithSharedSnippets.from_json(json)
# print the JSON string representation of the object
print(TrustInfoWithSharedSnippets.to_json())

# convert the object into a dict
trust_info_with_shared_snippets_dict = trust_info_with_shared_snippets_instance.to_dict()
# create an instance of TrustInfoWithSharedSnippets from a dict
trust_info_with_shared_snippets_from_dict = TrustInfoWithSharedSnippets.from_dict(trust_info_with_shared_snippets_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


