# ForwardingRuleZtna

ZTNA forwarding rule configuration

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**connectivity** | **str** | Connectivity method for this ZTNA forwarding rule (e.g. direct) | [optional] [default to 'direct']
**destinations** | **str** | Destination scope this ZTNA forwarding rule applies to | [optional] [default to 'Any']
**enabled** | **bool** | Enable a forwarding rule ztna | [optional] [default to True]
**name** | **str** | Forwarding rule ZTNA name as an alphanumeric string [ 0-9a-zA-Z._ -] | 
**source_applications** | **str** | Source applications this ZTNA rule applies to | [optional] [default to 'Any']
**traffic_type** | **str** | Type of traffic this ZTNA rule applies to (dns, network, or both) | [optional] [default to 'dns']
**user_locations** | **str** | User location scope this ZTNA rule applies to | [optional] [default to 'Any']

## Example

```python
from scm.mobile_agent.models.forwarding_rule_ztna import ForwardingRuleZtna

# TODO update the JSON string below
json = "{}"
# create an instance of ForwardingRuleZtna from a JSON string
forwarding_rule_ztna_instance = ForwardingRuleZtna.from_json(json)
# print the JSON string representation of the object
print(ForwardingRuleZtna.to_json())

# convert the object into a dict
forwarding_rule_ztna_dict = forwarding_rule_ztna_instance.to_dict()
# create an instance of ForwardingRuleZtna from a dict
forwarding_rule_ztna_from_dict = ForwardingRuleZtna.from_dict(forwarding_rule_ztna_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


