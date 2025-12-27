# InternetRuleTypeDefaultProfileSettings


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dlp** | **str** |  | [optional] 
**file_control** | [**InternetRuleTypeAllowUrlCategoryInnerFileControl**](InternetRuleTypeAllowUrlCategoryInnerFileControl.md) |  | [optional] 

## Example

```python
from scm_security_services.models.internet_rule_type_default_profile_settings import InternetRuleTypeDefaultProfileSettings

# TODO update the JSON string below
json = "{}"
# create an instance of InternetRuleTypeDefaultProfileSettings from a JSON string
internet_rule_type_default_profile_settings_instance = InternetRuleTypeDefaultProfileSettings.from_json(json)
# print the JSON string representation of the object
print(InternetRuleTypeDefaultProfileSettings.to_json())

# convert the object into a dict
internet_rule_type_default_profile_settings_dict = internet_rule_type_default_profile_settings_instance.to_dict()
# create an instance of InternetRuleTypeDefaultProfileSettings from a dict
internet_rule_type_default_profile_settings_from_dict = InternetRuleTypeDefaultProfileSettings.from_dict(internet_rule_type_default_profile_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


