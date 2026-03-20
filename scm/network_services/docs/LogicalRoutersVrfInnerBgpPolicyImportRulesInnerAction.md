# LogicalRoutersVrfInnerBgpPolicyImportRulesInnerAction


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allow** | [**LogicalRoutersVrfInnerBgpPolicyImportRulesInnerActionAllow**](LogicalRoutersVrfInnerBgpPolicyImportRulesInnerActionAllow.md) |  | [optional] 
**deny** | **object** |  | [optional] 

## Example

```python
from scm.network_services.models.logical_routers_vrf_inner_bgp_policy_import_rules_inner_action import LogicalRoutersVrfInnerBgpPolicyImportRulesInnerAction

# TODO update the JSON string below
json = "{}"
# create an instance of LogicalRoutersVrfInnerBgpPolicyImportRulesInnerAction from a JSON string
logical_routers_vrf_inner_bgp_policy_import_rules_inner_action_instance = LogicalRoutersVrfInnerBgpPolicyImportRulesInnerAction.from_json(json)
# print the JSON string representation of the object
print(LogicalRoutersVrfInnerBgpPolicyImportRulesInnerAction.to_json())

# convert the object into a dict
logical_routers_vrf_inner_bgp_policy_import_rules_inner_action_dict = logical_routers_vrf_inner_bgp_policy_import_rules_inner_action_instance.to_dict()
# create an instance of LogicalRoutersVrfInnerBgpPolicyImportRulesInnerAction from a dict
logical_routers_vrf_inner_bgp_policy_import_rules_inner_action_from_dict = LogicalRoutersVrfInnerBgpPolicyImportRulesInnerAction.from_dict(logical_routers_vrf_inner_bgp_policy_import_rules_inner_action_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


