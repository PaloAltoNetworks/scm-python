# LogicalRoutersVrfInnerBgpPolicyExportRulesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | [**LogicalRoutersVrfInnerBgpPolicyExportRulesInnerAction**](LogicalRoutersVrfInnerBgpPolicyExportRulesInnerAction.md) |  | [optional] 
**enable** | **bool** |  | [optional] 
**match** | [**LogicalRoutersVrfInnerBgpPolicyExportRulesInnerMatch**](LogicalRoutersVrfInnerBgpPolicyExportRulesInnerMatch.md) |  | [optional] 
**name** | **str** |  | 
**used_by** | **List[str]** |  | [optional] 

## Example

```python
from scm.network_services.models.logical_routers_vrf_inner_bgp_policy_export_rules_inner import LogicalRoutersVrfInnerBgpPolicyExportRulesInner

# TODO update the JSON string below
json = "{}"
# create an instance of LogicalRoutersVrfInnerBgpPolicyExportRulesInner from a JSON string
logical_routers_vrf_inner_bgp_policy_export_rules_inner_instance = LogicalRoutersVrfInnerBgpPolicyExportRulesInner.from_json(json)
# print the JSON string representation of the object
print(LogicalRoutersVrfInnerBgpPolicyExportRulesInner.to_json())

# convert the object into a dict
logical_routers_vrf_inner_bgp_policy_export_rules_inner_dict = logical_routers_vrf_inner_bgp_policy_export_rules_inner_instance.to_dict()
# create an instance of LogicalRoutersVrfInnerBgpPolicyExportRulesInner from a dict
logical_routers_vrf_inner_bgp_policy_export_rules_inner_from_dict = LogicalRoutersVrfInnerBgpPolicyExportRulesInner.from_dict(logical_routers_vrf_inner_bgp_policy_export_rules_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


