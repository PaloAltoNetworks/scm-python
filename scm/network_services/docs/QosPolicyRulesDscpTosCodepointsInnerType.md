# QosPolicyRulesDscpTosCodepointsInnerType


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**af** | [**QosPolicyRulesDscpTosCodepointsInnerTypeAf**](QosPolicyRulesDscpTosCodepointsInnerTypeAf.md) |  | [optional] 
**cs** | [**QosPolicyRulesDscpTosCodepointsInnerTypeAf**](QosPolicyRulesDscpTosCodepointsInnerTypeAf.md) |  | [optional] 
**custom** | [**QosPolicyRulesDscpTosCodepointsInnerTypeCustom**](QosPolicyRulesDscpTosCodepointsInnerTypeCustom.md) |  | [optional] 
**ef** | **object** |  | [optional] 
**tos** | [**QosPolicyRulesDscpTosCodepointsInnerTypeAf**](QosPolicyRulesDscpTosCodepointsInnerTypeAf.md) |  | [optional] 

## Example

```python
from scm.network_services.models.qos_policy_rules_dscp_tos_codepoints_inner_type import QosPolicyRulesDscpTosCodepointsInnerType

# TODO update the JSON string below
json = "{}"
# create an instance of QosPolicyRulesDscpTosCodepointsInnerType from a JSON string
qos_policy_rules_dscp_tos_codepoints_inner_type_instance = QosPolicyRulesDscpTosCodepointsInnerType.from_json(json)
# print the JSON string representation of the object
print(QosPolicyRulesDscpTosCodepointsInnerType.to_json())

# convert the object into a dict
qos_policy_rules_dscp_tos_codepoints_inner_type_dict = qos_policy_rules_dscp_tos_codepoints_inner_type_instance.to_dict()
# create an instance of QosPolicyRulesDscpTosCodepointsInnerType from a dict
qos_policy_rules_dscp_tos_codepoints_inner_type_from_dict = QosPolicyRulesDscpTosCodepointsInnerType.from_dict(qos_policy_rules_dscp_tos_codepoints_inner_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


