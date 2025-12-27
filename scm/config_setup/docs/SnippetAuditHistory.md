# SnippetAuditHistory


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **str** |  | [optional] [readonly] 
**created** | **datetime** |  | [optional] [readonly] 
**deleted** | **int** |  | [optional] [readonly] 
**details** | **str** |  | [optional] [readonly] 
**display** | **int** |  | [optional] [readonly] 
**donor_created** | **int** |  | [optional] [readonly] 
**donor_tenant_name** | **str** |  | [optional] [readonly] 
**donor_tsg** | **str** |  | [optional] [readonly] 
**id** | **int** |  | [optional] [readonly] 
**recipient_tenant_name** | **str** |  | [optional] [readonly] 
**recipient_tsg** | **str** |  | [optional] [readonly] 
**snippet_uuid** | **str** |  | [optional] [readonly] 
**user** | **str** |  | [optional] [readonly] 
**version** | **str** |  | [optional] [readonly] 

## Example

```python
from scm.config_setup.models.snippet_audit_history import SnippetAuditHistory

# TODO update the JSON string below
json = "{}"
# create an instance of SnippetAuditHistory from a JSON string
snippet_audit_history_instance = SnippetAuditHistory.from_json(json)
# print the JSON string representation of the object
print(SnippetAuditHistory.to_json())

# convert the object into a dict
snippet_audit_history_dict = snippet_audit_history_instance.to_dict()
# create an instance of SnippetAuditHistory from a dict
snippet_audit_history_from_dict = SnippetAuditHistory.from_dict(snippet_audit_history_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


