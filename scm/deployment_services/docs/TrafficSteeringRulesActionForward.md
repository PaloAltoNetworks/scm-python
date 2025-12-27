# TrafficSteeringRulesActionForward


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**forward** | [**TrafficSteeringRulesActionForwardForward**](TrafficSteeringRulesActionForwardForward.md) |  | [optional] 
**no_pbf** | **object** |  | [optional] 

## Example

```python
from scm_deployment_services.models.traffic_steering_rules_action_forward import TrafficSteeringRulesActionForward

# TODO update the JSON string below
json = "{}"
# create an instance of TrafficSteeringRulesActionForward from a JSON string
traffic_steering_rules_action_forward_instance = TrafficSteeringRulesActionForward.from_json(json)
# print the JSON string representation of the object
print(TrafficSteeringRulesActionForward.to_json())

# convert the object into a dict
traffic_steering_rules_action_forward_dict = traffic_steering_rules_action_forward_instance.to_dict()
# create an instance of TrafficSteeringRulesActionForward from a dict
traffic_steering_rules_action_forward_from_dict = TrafficSteeringRulesActionForward.from_dict(traffic_steering_rules_action_forward_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


