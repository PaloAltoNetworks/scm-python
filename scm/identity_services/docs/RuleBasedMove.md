# RuleBasedMove


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**destination** | **str** | The position of the rule relative to other rules in this rulebase. | 
**destination_rule** | **str** | A destination target rule UUID. This is only used if the &#x60;destination&#x60; value is &#x60;before&#x60; or &#x60;after&#x60;. | [optional] 
**rulebase** | **str** | The position of the rule relative to the local rulebase | 

## Example

```python
from scm_identity_services.models.rule_based_move import RuleBasedMove

# TODO update the JSON string below
json = "{}"
# create an instance of RuleBasedMove from a JSON string
rule_based_move_instance = RuleBasedMove.from_json(json)
# print the JSON string representation of the object
print(RuleBasedMove.to_json())

# convert the object into a dict
rule_based_move_dict = rule_based_move_instance.to_dict()
# create an instance of RuleBasedMove from a dict
rule_based_move_from_dict = RuleBasedMove.from_dict(rule_based_move_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


