# DosProtectionRulesTo

Destination zones and interfaces

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**interface** | **List[str]** |  | [optional] 
**zone** | **List[str]** |  | [optional] 

## Example

```python
from scm.security_services.models.dos_protection_rules_to import DosProtectionRulesTo

# TODO update the JSON string below
json = "{}"
# create an instance of DosProtectionRulesTo from a JSON string
dos_protection_rules_to_instance = DosProtectionRulesTo.from_json(json)
# print the JSON string representation of the object
print(DosProtectionRulesTo.to_json())

# convert the object into a dict
dos_protection_rules_to_dict = dos_protection_rules_to_instance.to_dict()
# create an instance of DosProtectionRulesTo from a dict
dos_protection_rules_to_from_dict = DosProtectionRulesTo.from_dict(dos_protection_rules_to_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


