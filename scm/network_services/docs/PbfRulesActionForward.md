# PbfRulesActionForward


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**egress_interface** | **str** | Egress interface | [optional] 
**monitor** | [**PbfRulesActionForwardMonitor**](PbfRulesActionForwardMonitor.md) |  | [optional] 
**nexthop** | [**PbfRulesActionForwardNexthop**](PbfRulesActionForwardNexthop.md) |  | [optional] 

## Example

```python
from scm_network_services.models.pbf_rules_action_forward import PbfRulesActionForward

# TODO update the JSON string below
json = "{}"
# create an instance of PbfRulesActionForward from a JSON string
pbf_rules_action_forward_instance = PbfRulesActionForward.from_json(json)
# print the JSON string representation of the object
print(PbfRulesActionForward.to_json())

# convert the object into a dict
pbf_rules_action_forward_dict = pbf_rules_action_forward_instance.to_dict()
# create an instance of PbfRulesActionForward from a dict
pbf_rules_action_forward_from_dict = PbfRulesActionForward.from_dict(pbf_rules_action_forward_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


