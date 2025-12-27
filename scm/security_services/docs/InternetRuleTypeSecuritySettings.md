# InternetRuleTypeSecuritySettings


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**anti_spyware** | **str** |  | [optional] [default to 'yes']
**virus_and_wildfire_analysis** | **str** |  | [optional] [default to 'yes']
**vulnerability** | **str** |  | [optional] [default to 'yes']

## Example

```python
from scm_security_services.models.internet_rule_type_security_settings import InternetRuleTypeSecuritySettings

# TODO update the JSON string below
json = "{}"
# create an instance of InternetRuleTypeSecuritySettings from a JSON string
internet_rule_type_security_settings_instance = InternetRuleTypeSecuritySettings.from_json(json)
# print the JSON string representation of the object
print(InternetRuleTypeSecuritySettings.to_json())

# convert the object into a dict
internet_rule_type_security_settings_dict = internet_rule_type_security_settings_instance.to_dict()
# create an instance of InternetRuleTypeSecuritySettings from a dict
internet_rule_type_security_settings_from_dict = InternetRuleTypeSecuritySettings.from_dict(internet_rule_type_security_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


