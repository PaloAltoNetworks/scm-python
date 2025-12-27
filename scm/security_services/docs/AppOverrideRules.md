# AppOverrideRules


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**application** | **str** |  | 
**description** | **str** |  | [optional] 
**destination** | **List[str]** |  | [default to ["any"]]
**device** | **str** | The device in which the resource is defined | [optional] 
**disabled** | **bool** |  | [optional] [default to False]
**folder** | **str** | The folder in which the resource is defined | [optional] 
**var_from** | **List[str]** |  | [default to ["any"]]
**group_tag** | **str** |  | [optional] 
**id** | **str** | UUID of the resource | [optional] [readonly] 
**name** | **str** |  | 
**negate_destination** | **bool** |  | [optional] [default to False]
**negate_source** | **bool** |  | [optional] [default to False]
**port** | **str** |  | 
**protocol** | **str** |  | 
**snippet** | **str** | The snippet in which the resource is defined | [optional] 
**source** | **List[str]** |  | [default to ["any"]]
**tag** | **List[str]** |  | [optional] 
**to** | **List[str]** |  | [default to ["any"]]

## Example

```python
from scm.security_services.models.app_override_rules import AppOverrideRules

# TODO update the JSON string below
json = "{}"
# create an instance of AppOverrideRules from a JSON string
app_override_rules_instance = AppOverrideRules.from_json(json)
# print the JSON string representation of the object
print(AppOverrideRules.to_json())

# convert the object into a dict
app_override_rules_dict = app_override_rules_instance.to_dict()
# create an instance of AppOverrideRules from a dict
app_override_rules_from_dict = AppOverrideRules.from_dict(app_override_rules_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


