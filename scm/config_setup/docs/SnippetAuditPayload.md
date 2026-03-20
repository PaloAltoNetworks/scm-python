# SnippetAuditPayload


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **str** |  | [optional] 
**details** | **str** |  | [optional] 
**donor_created** | **int** |  | [optional] 
**donor_tenant_name** | **str** |  | [optional] 
**donor_tsg** | **str** |  | [optional] 
**recipient_tenant_name** | **str** |  | [optional] 
**recipient_tsg** | **str** |  | [optional] 
**snippet_uuid** | **str** |  | [optional] 
**version** | **str** |  | [optional] 

## Example

```python
from scm.config_setup.models.snippet_audit_payload import SnippetAuditPayload

# TODO update the JSON string below
json = "{}"
# create an instance of SnippetAuditPayload from a JSON string
snippet_audit_payload_instance = SnippetAuditPayload.from_json(json)
# print the JSON string representation of the object
print(SnippetAuditPayload.to_json())

# convert the object into a dict
snippet_audit_payload_dict = snippet_audit_payload_instance.to_dict()
# create an instance of SnippetAuditPayload from a dict
snippet_audit_payload_from_dict = SnippetAuditPayload.from_dict(snippet_audit_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


