# SecurityRuleTypeProfileSetting

The security profile object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**group** | **List[str]** | The security profile group | [optional] 

## Example

```python
from scm_security_services.models.security_rule_type_profile_setting import SecurityRuleTypeProfileSetting

# TODO update the JSON string below
json = "{}"
# create an instance of SecurityRuleTypeProfileSetting from a JSON string
security_rule_type_profile_setting_instance = SecurityRuleTypeProfileSetting.from_json(json)
# print the JSON string representation of the object
print(SecurityRuleTypeProfileSetting.to_json())

# convert the object into a dict
security_rule_type_profile_setting_dict = security_rule_type_profile_setting_instance.to_dict()
# create an instance of SecurityRuleTypeProfileSetting from a dict
security_rule_type_profile_setting_from_dict = SecurityRuleTypeProfileSetting.from_dict(security_rule_type_profile_setting_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


