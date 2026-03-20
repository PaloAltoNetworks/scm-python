# PbfRulesActionForwardMonitor


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**disable_if_unreachable** | **bool** | Disable this rule if nexthop/monitor ip is unreachable? | [optional] 
**ip_address** | **str** | Monitor IP address | [optional] 
**profile** | **str** | Monitoring profile | [optional] 

## Example

```python
from scm.network_services.models.pbf_rules_action_forward_monitor import PbfRulesActionForwardMonitor

# TODO update the JSON string below
json = "{}"
# create an instance of PbfRulesActionForwardMonitor from a JSON string
pbf_rules_action_forward_monitor_instance = PbfRulesActionForwardMonitor.from_json(json)
# print the JSON string representation of the object
print(PbfRulesActionForwardMonitor.to_json())

# convert the object into a dict
pbf_rules_action_forward_monitor_dict = pbf_rules_action_forward_monitor_instance.to_dict()
# create an instance of PbfRulesActionForwardMonitor from a dict
pbf_rules_action_forward_monitor_from_dict = PbfRulesActionForwardMonitor.from_dict(pbf_rules_action_forward_monitor_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


