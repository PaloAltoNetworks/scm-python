# LogicalRoutersVrfInnerBgpPolicyAggregationAddressInnerAggregateRouteAttributes


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
**weight** | **int** |  | [optional] 

## Example

```python
from scm_network_services.models.logical_routers_vrf_inner_bgp_policy_aggregation_address_inner_aggregate_route_attributes import LogicalRoutersVrfInnerBgpPolicyAggregationAddressInnerAggregateRouteAttributes

# TODO update the JSON string below
json = "{}"
# create an instance of LogicalRoutersVrfInnerBgpPolicyAggregationAddressInnerAggregateRouteAttributes from a JSON string
logical_routers_vrf_inner_bgp_policy_aggregation_address_inner_aggregate_route_attributes_instance = LogicalRoutersVrfInnerBgpPolicyAggregationAddressInnerAggregateRouteAttributes.from_json(json)
# print the JSON string representation of the object
print(LogicalRoutersVrfInnerBgpPolicyAggregationAddressInnerAggregateRouteAttributes.to_json())

# convert the object into a dict
logical_routers_vrf_inner_bgp_policy_aggregation_address_inner_aggregate_route_attributes_dict = logical_routers_vrf_inner_bgp_policy_aggregation_address_inner_aggregate_route_attributes_instance.to_dict()
# create an instance of LogicalRoutersVrfInnerBgpPolicyAggregationAddressInnerAggregateRouteAttributes from a dict
logical_routers_vrf_inner_bgp_policy_aggregation_address_inner_aggregate_route_attributes_from_dict = LogicalRoutersVrfInnerBgpPolicyAggregationAddressInnerAggregateRouteAttributes.from_dict(logical_routers_vrf_inner_bgp_policy_aggregation_address_inner_aggregate_route_attributes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


