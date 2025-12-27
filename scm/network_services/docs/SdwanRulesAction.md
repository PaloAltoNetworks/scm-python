# SdwanRulesAction


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**traffic_distribution_profile** | **str** | Traffic dstribution profile | 

## Example

```python
from scm_network_services.models.sdwan_rules_action import SdwanRulesAction

# TODO update the JSON string below
json = "{}"
# create an instance of SdwanRulesAction from a JSON string
sdwan_rules_action_instance = SdwanRulesAction.from_json(json)
# print the JSON string representation of the object
print(SdwanRulesAction.to_json())

# convert the object into a dict
sdwan_rules_action_dict = sdwan_rules_action_instance.to_dict()
# create an instance of SdwanRulesAction from a dict
sdwan_rules_action_from_dict = SdwanRulesAction.from_dict(sdwan_rules_action_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


