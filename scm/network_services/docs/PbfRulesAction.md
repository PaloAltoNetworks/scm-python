# PbfRulesAction


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**discard** | **object** |  | [optional] 
**forward** | [**PbfRulesActionForward**](PbfRulesActionForward.md) |  | [optional] 
**no_pbf** | **object** |  | [optional] 

## Example

```python
from scm.network_services.models.pbf_rules_action import PbfRulesAction

# TODO update the JSON string below
json = "{}"
# create an instance of PbfRulesAction from a JSON string
pbf_rules_action_instance = PbfRulesAction.from_json(json)
# print the JSON string representation of the object
print(PbfRulesAction.to_json())

# convert the object into a dict
pbf_rules_action_dict = pbf_rules_action_instance.to_dict()
# create an instance of PbfRulesAction from a dict
pbf_rules_action_from_dict = PbfRulesAction.from_dict(pbf_rules_action_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


