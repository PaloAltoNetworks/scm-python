# TrafficSteeringRulesListResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[TrafficSteeringRules]**](TrafficSteeringRules.md) |  | 
**limit** | **int** | The maximum number of results per page | [default to 200]
**offset** | **int** | The offset into the list of results returned | [default to 0]
**total** | **int** | The total count of results | 

## Example

```python
from scm.deployment_services.models.traffic_steering_rules_list_response import TrafficSteeringRulesListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of TrafficSteeringRulesListResponse from a JSON string
traffic_steering_rules_list_response_instance = TrafficSteeringRulesListResponse.from_json(json)
# print the JSON string representation of the object
print(TrafficSteeringRulesListResponse.to_json())

# convert the object into a dict
traffic_steering_rules_list_response_dict = traffic_steering_rules_list_response_instance.to_dict()
# create an instance of TrafficSteeringRulesListResponse from a dict
traffic_steering_rules_list_response_from_dict = TrafficSteeringRulesListResponse.from_dict(traffic_steering_rules_list_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


