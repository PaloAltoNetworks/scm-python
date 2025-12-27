# WildfireAntiVirusProfilesRulesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**analysis** | **str** |  | [optional] 
**application** | **List[str]** |  | [optional] 
**direction** | **str** |  | [optional] 
**file_type** | **List[str]** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from scm_security_services.models.wildfire_anti_virus_profiles_rules_inner import WildfireAntiVirusProfilesRulesInner

# TODO update the JSON string below
json = "{}"
# create an instance of WildfireAntiVirusProfilesRulesInner from a JSON string
wildfire_anti_virus_profiles_rules_inner_instance = WildfireAntiVirusProfilesRulesInner.from_json(json)
# print the JSON string representation of the object
print(WildfireAntiVirusProfilesRulesInner.to_json())

# convert the object into a dict
wildfire_anti_virus_profiles_rules_inner_dict = wildfire_anti_virus_profiles_rules_inner_instance.to_dict()
# create an instance of WildfireAntiVirusProfilesRulesInner from a dict
wildfire_anti_virus_profiles_rules_inner_from_dict = WildfireAntiVirusProfilesRulesInner.from_dict(wildfire_anti_virus_profiles_rules_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


