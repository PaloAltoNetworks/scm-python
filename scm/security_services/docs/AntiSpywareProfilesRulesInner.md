# AntiSpywareProfilesRulesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | [**AntiSpywareProfilesRulesInnerAction**](AntiSpywareProfilesRulesInnerAction.md) |  | [optional] 
**category** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**packet_capture** | **str** |  | [optional] 
**severity** | **List[str]** |  | [optional] 
**threat_name** | **str** |  | [optional] [default to 'any']

## Example

```python
from scm_security_services.models.anti_spyware_profiles_rules_inner import AntiSpywareProfilesRulesInner

# TODO update the JSON string below
json = "{}"
# create an instance of AntiSpywareProfilesRulesInner from a JSON string
anti_spyware_profiles_rules_inner_instance = AntiSpywareProfilesRulesInner.from_json(json)
# print the JSON string representation of the object
print(AntiSpywareProfilesRulesInner.to_json())

# convert the object into a dict
anti_spyware_profiles_rules_inner_dict = anti_spyware_profiles_rules_inner_instance.to_dict()
# create an instance of AntiSpywareProfilesRulesInner from a dict
anti_spyware_profiles_rules_inner_from_dict = AntiSpywareProfilesRulesInner.from_dict(anti_spyware_profiles_rules_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


