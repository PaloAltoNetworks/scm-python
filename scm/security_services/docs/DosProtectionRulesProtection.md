# DosProtectionRulesProtection


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**aggregate** | [**DosProtectionRulesProtectionAggregate**](DosProtectionRulesProtectionAggregate.md) |  | [optional] 
**classified** | [**DosProtectionRulesProtectionClassified**](DosProtectionRulesProtectionClassified.md) |  | [optional] 

## Example

```python
from scm_security_services.models.dos_protection_rules_protection import DosProtectionRulesProtection

# TODO update the JSON string below
json = "{}"
# create an instance of DosProtectionRulesProtection from a JSON string
dos_protection_rules_protection_instance = DosProtectionRulesProtection.from_json(json)
# print the JSON string representation of the object
print(DosProtectionRulesProtection.to_json())

# convert the object into a dict
dos_protection_rules_protection_dict = dos_protection_rules_protection_instance.to_dict()
# create an instance of DosProtectionRulesProtection from a dict
dos_protection_rules_protection_from_dict = DosProtectionRulesProtection.from_dict(dos_protection_rules_protection_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


