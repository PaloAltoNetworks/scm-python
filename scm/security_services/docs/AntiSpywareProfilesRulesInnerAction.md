# AntiSpywareProfilesRulesInnerAction

anti spyware profiles rules default action

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**alert** | **object** |  | [optional] 
**allow** | **object** |  | [optional] 
**block_ip** | [**AntiSpywareProfilesRulesInnerActionBlockIp**](AntiSpywareProfilesRulesInnerActionBlockIp.md) |  | [optional] 
**drop** | **object** |  | [optional] 
**reset_both** | **object** |  | [optional] 
**reset_client** | **object** |  | [optional] 
**reset_server** | **object** |  | [optional] 

## Example

```python
from scm.security_services.models.anti_spyware_profiles_rules_inner_action import AntiSpywareProfilesRulesInnerAction

# TODO update the JSON string below
json = "{}"
# create an instance of AntiSpywareProfilesRulesInnerAction from a JSON string
anti_spyware_profiles_rules_inner_action_instance = AntiSpywareProfilesRulesInnerAction.from_json(json)
# print the JSON string representation of the object
print(AntiSpywareProfilesRulesInnerAction.to_json())

# convert the object into a dict
anti_spyware_profiles_rules_inner_action_dict = anti_spyware_profiles_rules_inner_action_instance.to_dict()
# create an instance of AntiSpywareProfilesRulesInnerAction from a dict
anti_spyware_profiles_rules_inner_action_from_dict = AntiSpywareProfilesRulesInnerAction.from_dict(anti_spyware_profiles_rules_inner_action_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


