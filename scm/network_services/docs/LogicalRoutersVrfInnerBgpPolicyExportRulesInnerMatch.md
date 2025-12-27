# LogicalRoutersVrfInnerBgpPolicyExportRulesInnerMatch


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address_prefix** | [**List[LogicalRoutersVrfInnerBgpPolicyExportRulesInnerMatchAddressPrefixInner]**](LogicalRoutersVrfInnerBgpPolicyExportRulesInnerMatchAddressPrefixInner.md) |  | [optional] 
**afi** | **str** |  | [optional] 
**as_path** | [**LogicalRoutersVrfInnerBgpPolicyAggregationAddressInnerAdvertiseFiltersInnerMatchAsPath**](LogicalRoutersVrfInnerBgpPolicyAggregationAddressInnerAdvertiseFiltersInnerMatchAsPath.md) |  | [optional] 
**community** | [**LogicalRoutersVrfInnerBgpPolicyAggregationAddressInnerAdvertiseFiltersInnerMatchAsPath**](LogicalRoutersVrfInnerBgpPolicyAggregationAddressInnerAdvertiseFiltersInnerMatchAsPath.md) |  | [optional] 
**extended_community** | [**LogicalRoutersVrfInnerBgpPolicyAggregationAddressInnerAdvertiseFiltersInnerMatchAsPath**](LogicalRoutersVrfInnerBgpPolicyAggregationAddressInnerAdvertiseFiltersInnerMatchAsPath.md) |  | [optional] 
**from_peer** | **List[str]** |  | [optional] 
**med** | **int** |  | [optional] 
**nexthop** | **List[str]** |  | [optional] 
**route_table** | **str** |  | [optional] 
**safi** | **str** |  | [optional] 

## Example

```python
from scm_network_services.models.logical_routers_vrf_inner_bgp_policy_export_rules_inner_match import LogicalRoutersVrfInnerBgpPolicyExportRulesInnerMatch

# TODO update the JSON string below
json = "{}"
# create an instance of LogicalRoutersVrfInnerBgpPolicyExportRulesInnerMatch from a JSON string
logical_routers_vrf_inner_bgp_policy_export_rules_inner_match_instance = LogicalRoutersVrfInnerBgpPolicyExportRulesInnerMatch.from_json(json)
# print the JSON string representation of the object
print(LogicalRoutersVrfInnerBgpPolicyExportRulesInnerMatch.to_json())

# convert the object into a dict
logical_routers_vrf_inner_bgp_policy_export_rules_inner_match_dict = logical_routers_vrf_inner_bgp_policy_export_rules_inner_match_instance.to_dict()
# create an instance of LogicalRoutersVrfInnerBgpPolicyExportRulesInnerMatch from a dict
logical_routers_vrf_inner_bgp_policy_export_rules_inner_match_from_dict = LogicalRoutersVrfInnerBgpPolicyExportRulesInnerMatch.from_dict(logical_routers_vrf_inner_bgp_policy_export_rules_inner_match_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


