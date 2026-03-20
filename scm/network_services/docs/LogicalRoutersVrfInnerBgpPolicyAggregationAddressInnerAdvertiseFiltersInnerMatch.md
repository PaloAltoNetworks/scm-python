# LogicalRoutersVrfInnerBgpPolicyAggregationAddressInnerAdvertiseFiltersInnerMatch


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address_prefix** | [**List[LogicalRoutersVrfInnerBgpPolicyAggregationAddressInnerAdvertiseFiltersInnerMatchAddressPrefixInner]**](LogicalRoutersVrfInnerBgpPolicyAggregationAddressInnerAdvertiseFiltersInnerMatchAddressPrefixInner.md) |  | [optional] 
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
from scm.network_services.models.logical_routers_vrf_inner_bgp_policy_aggregation_address_inner_advertise_filters_inner_match import LogicalRoutersVrfInnerBgpPolicyAggregationAddressInnerAdvertiseFiltersInnerMatch

# TODO update the JSON string below
json = "{}"
# create an instance of LogicalRoutersVrfInnerBgpPolicyAggregationAddressInnerAdvertiseFiltersInnerMatch from a JSON string
logical_routers_vrf_inner_bgp_policy_aggregation_address_inner_advertise_filters_inner_match_instance = LogicalRoutersVrfInnerBgpPolicyAggregationAddressInnerAdvertiseFiltersInnerMatch.from_json(json)
# print the JSON string representation of the object
print(LogicalRoutersVrfInnerBgpPolicyAggregationAddressInnerAdvertiseFiltersInnerMatch.to_json())

# convert the object into a dict
logical_routers_vrf_inner_bgp_policy_aggregation_address_inner_advertise_filters_inner_match_dict = logical_routers_vrf_inner_bgp_policy_aggregation_address_inner_advertise_filters_inner_match_instance.to_dict()
# create an instance of LogicalRoutersVrfInnerBgpPolicyAggregationAddressInnerAdvertiseFiltersInnerMatch from a dict
logical_routers_vrf_inner_bgp_policy_aggregation_address_inner_advertise_filters_inner_match_from_dict = LogicalRoutersVrfInnerBgpPolicyAggregationAddressInnerAdvertiseFiltersInnerMatch.from_dict(logical_routers_vrf_inner_bgp_policy_aggregation_address_inner_advertise_filters_inner_match_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


