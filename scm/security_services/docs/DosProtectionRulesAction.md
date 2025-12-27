# DosProtectionRulesAction

The action to take on rule match

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allow** | **object** |  | [optional] 
**deny** | **object** |  | [optional] 
**protect** | **object** |  | [optional] 

## Example

```python
from scm.security_services.models.dos_protection_rules_action import DosProtectionRulesAction

# TODO update the JSON string below
json = "{}"
# create an instance of DosProtectionRulesAction from a JSON string
dos_protection_rules_action_instance = DosProtectionRulesAction.from_json(json)
# print the JSON string representation of the object
print(DosProtectionRulesAction.to_json())

# convert the object into a dict
dos_protection_rules_action_dict = dos_protection_rules_action_instance.to_dict()
# create an instance of DosProtectionRulesAction from a dict
dos_protection_rules_action_from_dict = DosProtectionRulesAction.from_dict(dos_protection_rules_action_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


