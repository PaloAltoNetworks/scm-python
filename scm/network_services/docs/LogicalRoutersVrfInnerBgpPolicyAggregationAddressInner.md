# LogicalRoutersVrfInnerBgpPolicyAggregationAddressInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**advertise_filters** | [**List[LogicalRoutersVrfInnerBgpPolicyAggregationAddressInnerAdvertiseFiltersInner]**](LogicalRoutersVrfInnerBgpPolicyAggregationAddressInnerAdvertiseFiltersInner.md) |  | [optional] 
**aggregate_route_attributes** | [**LogicalRoutersVrfInnerBgpPolicyAggregationAddressInnerAggregateRouteAttributes**](LogicalRoutersVrfInnerBgpPolicyAggregationAddressInnerAggregateRouteAttributes.md) |  | [optional] 
**as_set** | **bool** |  | [optional] 
**enable** | **bool** |  | [optional] 
**name** | **str** |  | 
**prefix** | **str** |  | [optional] 
**summary** | **bool** |  | [optional] 
**suppress_filters** | [**List[LogicalRoutersVrfInnerBgpPolicyAggregationAddressInnerAdvertiseFiltersInner]**](LogicalRoutersVrfInnerBgpPolicyAggregationAddressInnerAdvertiseFiltersInner.md) |  | [optional] 

## Example

```python
from scm_network_services.models.logical_routers_vrf_inner_bgp_policy_aggregation_address_inner import LogicalRoutersVrfInnerBgpPolicyAggregationAddressInner

# TODO update the JSON string below
json = "{}"
# create an instance of LogicalRoutersVrfInnerBgpPolicyAggregationAddressInner from a JSON string
logical_routers_vrf_inner_bgp_policy_aggregation_address_inner_instance = LogicalRoutersVrfInnerBgpPolicyAggregationAddressInner.from_json(json)
# print the JSON string representation of the object
print(LogicalRoutersVrfInnerBgpPolicyAggregationAddressInner.to_json())

# convert the object into a dict
logical_routers_vrf_inner_bgp_policy_aggregation_address_inner_dict = logical_routers_vrf_inner_bgp_policy_aggregation_address_inner_instance.to_dict()
# create an instance of LogicalRoutersVrfInnerBgpPolicyAggregationAddressInner from a dict
logical_routers_vrf_inner_bgp_policy_aggregation_address_inner_from_dict = LogicalRoutersVrfInnerBgpPolicyAggregationAddressInner.from_dict(logical_routers_vrf_inner_bgp_policy_aggregation_address_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


