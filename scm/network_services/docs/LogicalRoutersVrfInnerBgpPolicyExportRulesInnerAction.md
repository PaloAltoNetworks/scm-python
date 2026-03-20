# LogicalRoutersVrfInnerBgpPolicyExportRulesInnerAction


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allow** | [**LogicalRoutersVrfInnerBgpPolicyExportRulesInnerActionAllow**](LogicalRoutersVrfInnerBgpPolicyExportRulesInnerActionAllow.md) |  | [optional] 
**deny** | **object** |  | [optional] 

## Example

```python
from scm.network_services.models.logical_routers_vrf_inner_bgp_policy_export_rules_inner_action import LogicalRoutersVrfInnerBgpPolicyExportRulesInnerAction

# TODO update the JSON string below
json = "{}"
# create an instance of LogicalRoutersVrfInnerBgpPolicyExportRulesInnerAction from a JSON string
logical_routers_vrf_inner_bgp_policy_export_rules_inner_action_instance = LogicalRoutersVrfInnerBgpPolicyExportRulesInnerAction.from_json(json)
# print the JSON string representation of the object
print(LogicalRoutersVrfInnerBgpPolicyExportRulesInnerAction.to_json())

# convert the object into a dict
logical_routers_vrf_inner_bgp_policy_export_rules_inner_action_dict = logical_routers_vrf_inner_bgp_policy_export_rules_inner_action_instance.to_dict()
# create an instance of LogicalRoutersVrfInnerBgpPolicyExportRulesInnerAction from a dict
logical_routers_vrf_inner_bgp_policy_export_rules_inner_action_from_dict = LogicalRoutersVrfInnerBgpPolicyExportRulesInnerAction.from_dict(logical_routers_vrf_inner_bgp_policy_export_rules_inner_action_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


