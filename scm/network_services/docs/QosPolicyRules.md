# QosPolicyRules


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | [**QosPolicyRulesAction**](QosPolicyRulesAction.md) |  | 
**description** | **str** |  | [optional] 
**device** | **str** | The device in which the resource is defined | [optional] 
**dscp_tos** | [**QosPolicyRulesDscpTos**](QosPolicyRulesDscpTos.md) |  | [optional] 
**folder** | **str** | The folder in which the resource is defined | [optional] 
**id** | **str** | UUID of the resource | [optional] [readonly] 
**name** | **str** |  | 
**schedule** | **str** |  | [optional] 
**snippet** | **str** | The snippet in which the resource is defined | [optional] 

## Example

```python
from scm_network_services.models.qos_policy_rules import QosPolicyRules

# TODO update the JSON string below
json = "{}"
# create an instance of QosPolicyRules from a JSON string
qos_policy_rules_instance = QosPolicyRules.from_json(json)
# print the JSON string representation of the object
print(QosPolicyRules.to_json())

# convert the object into a dict
qos_policy_rules_dict = qos_policy_rules_instance.to_dict()
# create an instance of QosPolicyRules from a dict
qos_policy_rules_from_dict = QosPolicyRules.from_dict(qos_policy_rules_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


