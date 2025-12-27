# DosProtectionRulesProtectionClassified


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**classification_criteria** | [**DosProtectionRulesProtectionClassifiedClassificationCriteria**](DosProtectionRulesProtectionClassifiedClassificationCriteria.md) |  | 
**profile** | **str** | Classified DoS protection profile | 

## Example

```python
from scm_security_services.models.dos_protection_rules_protection_classified import DosProtectionRulesProtectionClassified

# TODO update the JSON string below
json = "{}"
# create an instance of DosProtectionRulesProtectionClassified from a JSON string
dos_protection_rules_protection_classified_instance = DosProtectionRulesProtectionClassified.from_json(json)
# print the JSON string representation of the object
print(DosProtectionRulesProtectionClassified.to_json())

# convert the object into a dict
dos_protection_rules_protection_classified_dict = dos_protection_rules_protection_classified_instance.to_dict()
# create an instance of DosProtectionRulesProtectionClassified from a dict
dos_protection_rules_protection_classified_from_dict = DosProtectionRulesProtectionClassified.from_dict(dos_protection_rules_protection_classified_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


