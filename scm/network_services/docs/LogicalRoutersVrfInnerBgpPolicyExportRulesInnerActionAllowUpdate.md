# LogicalRoutersVrfInnerBgpPolicyExportRulesInnerActionAllowUpdate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**as_path** | [**LogicalRoutersVrfInnerBgpPolicyAggregationAddressInnerAggregateRouteAttributesAsPath**](LogicalRoutersVrfInnerBgpPolicyAggregationAddressInnerAggregateRouteAttributesAsPath.md) |  | [optional] 
**as_path_limit** | **int** |  | [optional] 
**community** | [**LogicalRoutersVrfInnerBgpPolicyAggregationAddressInnerAggregateRouteAttributesCommunity**](LogicalRoutersVrfInnerBgpPolicyAggregationAddressInnerAggregateRouteAttributesCommunity.md) |  | [optional] 
**extended_community** | [**LogicalRoutersVrfInnerBgpPolicyAggregationAddressInnerAggregateRouteAttributesCommunity**](LogicalRoutersVrfInnerBgpPolicyAggregationAddressInnerAggregateRouteAttributesCommunity.md) |  | [optional] 
**local_preference** | **int** |  | [optional] 
**med** | **int** |  | [optional] 
**nexthop** | **str** |  | [optional] 
**origin** | **str** |  | [optional] 

## Example

```python
from scm.network_services.models.logical_routers_vrf_inner_bgp_policy_export_rules_inner_action_allow_update import LogicalRoutersVrfInnerBgpPolicyExportRulesInnerActionAllowUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of LogicalRoutersVrfInnerBgpPolicyExportRulesInnerActionAllowUpdate from a JSON string
logical_routers_vrf_inner_bgp_policy_export_rules_inner_action_allow_update_instance = LogicalRoutersVrfInnerBgpPolicyExportRulesInnerActionAllowUpdate.from_json(json)
# print the JSON string representation of the object
print(LogicalRoutersVrfInnerBgpPolicyExportRulesInnerActionAllowUpdate.to_json())

# convert the object into a dict
logical_routers_vrf_inner_bgp_policy_export_rules_inner_action_allow_update_dict = logical_routers_vrf_inner_bgp_policy_export_rules_inner_action_allow_update_instance.to_dict()
# create an instance of LogicalRoutersVrfInnerBgpPolicyExportRulesInnerActionAllowUpdate from a dict
logical_routers_vrf_inner_bgp_policy_export_rules_inner_action_allow_update_from_dict = LogicalRoutersVrfInnerBgpPolicyExportRulesInnerActionAllowUpdate.from_dict(logical_routers_vrf_inner_bgp_policy_export_rules_inner_action_allow_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


