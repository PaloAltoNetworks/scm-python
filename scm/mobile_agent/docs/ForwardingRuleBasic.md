# ForwardingRuleBasic

Basic forwarding rule configuration for PAC file and GlobalProtect proxy profiles

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**connectivity** | **str** | Connectivity method for this forwarding rule (e.g. direct) | [optional] [default to 'direct']
**destinations** | **str** | Destination scope this forwarding rule applies to | [optional] [default to 'Any']
**enabled** | **bool** | Enable a basic forwarding rule | [optional] [default to True]
**name** | **str** | Basic forwarding rule name as an alphanumeric string [ 0-9a-zA-Z._ -] | 
**user_locations** | **str** | User location scope this rule applies to | [optional] [default to 'Any']

## Example

```python
from scm.mobile_agent.models.forwarding_rule_basic import ForwardingRuleBasic

# TODO update the JSON string below
json = "{}"
# create an instance of ForwardingRuleBasic from a JSON string
forwarding_rule_basic_instance = ForwardingRuleBasic.from_json(json)
# print the JSON string representation of the object
print(ForwardingRuleBasic.to_json())

# convert the object into a dict
forwarding_rule_basic_dict = forwarding_rule_basic_instance.to_dict()
# create an instance of ForwardingRuleBasic from a dict
forwarding_rule_basic_from_dict = ForwardingRuleBasic.from_dict(forwarding_rule_basic_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


