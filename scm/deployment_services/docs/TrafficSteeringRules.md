# TrafficSteeringRules


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | [**TrafficSteeringRulesAction**](TrafficSteeringRulesAction.md) |  | [optional] 
**category** | **List[str]** |  | [optional] 
**destination** | **List[str]** |  | [optional] [default to ["any"]]
**folder** | **str** | The folder containing the traffic steering rule | [default to 'Service Connections']
**id** | **str** | The UUID of the traffic steering rule | [readonly] 
**name** | **str** |  | 
**service** | **List[str]** |  | [default to ["any"]]
**source** | **List[str]** |  | [default to ["any"]]
**source_user** | **List[str]** |  | [optional] [default to ["any"]]

## Example

```python
from scm.deployment_services.models.traffic_steering_rules import TrafficSteeringRules

# TODO update the JSON string below
json = "{}"
# create an instance of TrafficSteeringRules from a JSON string
traffic_steering_rules_instance = TrafficSteeringRules.from_json(json)
# print the JSON string representation of the object
print(TrafficSteeringRules.to_json())

# convert the object into a dict
traffic_steering_rules_dict = traffic_steering_rules_instance.to_dict()
# create an instance of TrafficSteeringRules from a dict
traffic_steering_rules_from_dict = TrafficSteeringRules.from_dict(traffic_steering_rules_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


