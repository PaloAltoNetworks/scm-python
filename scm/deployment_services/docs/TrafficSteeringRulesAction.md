# TrafficSteeringRulesAction


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**forward** | [**TrafficSteeringRulesActionForward**](TrafficSteeringRulesActionForward.md) |  | [optional] 

## Example

```python
from scm_deployment_services.models.traffic_steering_rules_action import TrafficSteeringRulesAction

# TODO update the JSON string below
json = "{}"
# create an instance of TrafficSteeringRulesAction from a JSON string
traffic_steering_rules_action_instance = TrafficSteeringRulesAction.from_json(json)
# print the JSON string representation of the object
print(TrafficSteeringRulesAction.to_json())

# convert the object into a dict
traffic_steering_rules_action_dict = traffic_steering_rules_action_instance.to_dict()
# create an instance of TrafficSteeringRulesAction from a dict
traffic_steering_rules_action_from_dict = TrafficSteeringRulesAction.from_dict(traffic_steering_rules_action_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


