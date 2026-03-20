# RuleBasedMove


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**destination** | **str** | A destination of the rule. Valid destination values are top, bottom, before and after. | 
**destination_rule** | **str** | A destination_rule attribute is required only if the destination value is before or after. Valid destination_rule values are existing rule UUIDs within the same container. | [optional] 
**rulebase** | **str** | A base of a rule. Valid rulebase values are pre and post. | 

## Example

```python
from scm.security_services.models.rule_based_move import RuleBasedMove

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


