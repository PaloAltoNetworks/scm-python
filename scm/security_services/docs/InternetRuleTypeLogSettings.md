# InternetRuleTypeLogSettings


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**log_sessions** | **bool** |  | [optional] [default to True]

## Example

```python
from scm.security_services.models.internet_rule_type_log_settings import InternetRuleTypeLogSettings

# TODO update the JSON string below
json = "{}"
# create an instance of InternetRuleTypeLogSettings from a JSON string
internet_rule_type_log_settings_instance = InternetRuleTypeLogSettings.from_json(json)
# print the JSON string representation of the object
print(InternetRuleTypeLogSettings.to_json())

# convert the object into a dict
internet_rule_type_log_settings_dict = internet_rule_type_log_settings_instance.to_dict()
# create an instance of InternetRuleTypeLogSettings from a dict
internet_rule_type_log_settings_from_dict = InternetRuleTypeLogSettings.from_dict(internet_rule_type_log_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


