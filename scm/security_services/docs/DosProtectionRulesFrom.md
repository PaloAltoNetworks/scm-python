# DosProtectionRulesFrom

Source zones and interfaces

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**interface** | **List[str]** |  | [optional] 
**zone** | **List[str]** |  | [optional] 

## Example

```python
from scm.security_services.models.dos_protection_rules_from import DosProtectionRulesFrom

# TODO update the JSON string below
json = "{}"
# create an instance of DosProtectionRulesFrom from a JSON string
dos_protection_rules_from_instance = DosProtectionRulesFrom.from_json(json)
# print the JSON string representation of the object
print(DosProtectionRulesFrom.to_json())

# convert the object into a dict
dos_protection_rules_from_dict = dos_protection_rules_from_instance.to_dict()
# create an instance of DosProtectionRulesFrom from a dict
dos_protection_rules_from_from_dict = DosProtectionRulesFrom.from_dict(dos_protection_rules_from_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


