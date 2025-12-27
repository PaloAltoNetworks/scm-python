# LogicalRoutersVrfInnerBgpPolicyConditionalAdvertisementPolicyInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**advertise_filters** | [**List[LogicalRoutersVrfInnerBgpPolicyAggregationAddressInnerAdvertiseFiltersInner]**](LogicalRoutersVrfInnerBgpPolicyAggregationAddressInnerAdvertiseFiltersInner.md) |  | [optional] 
**enable** | **bool** |  | [optional] 
**name** | **str** |  | 
**non_exist_filters** | [**List[LogicalRoutersVrfInnerBgpPolicyAggregationAddressInnerAdvertiseFiltersInner]**](LogicalRoutersVrfInnerBgpPolicyAggregationAddressInnerAdvertiseFiltersInner.md) |  | [optional] 
**used_by** | **List[str]** |  | [optional] 

## Example

```python
from scm_network_services.models.logical_routers_vrf_inner_bgp_policy_conditional_advertisement_policy_inner import LogicalRoutersVrfInnerBgpPolicyConditionalAdvertisementPolicyInner

# TODO update the JSON string below
json = "{}"
# create an instance of LogicalRoutersVrfInnerBgpPolicyConditionalAdvertisementPolicyInner from a JSON string
logical_routers_vrf_inner_bgp_policy_conditional_advertisement_policy_inner_instance = LogicalRoutersVrfInnerBgpPolicyConditionalAdvertisementPolicyInner.from_json(json)
# print the JSON string representation of the object
print(LogicalRoutersVrfInnerBgpPolicyConditionalAdvertisementPolicyInner.to_json())

# convert the object into a dict
logical_routers_vrf_inner_bgp_policy_conditional_advertisement_policy_inner_dict = logical_routers_vrf_inner_bgp_policy_conditional_advertisement_policy_inner_instance.to_dict()
# create an instance of LogicalRoutersVrfInnerBgpPolicyConditionalAdvertisementPolicyInner from a dict
logical_routers_vrf_inner_bgp_policy_conditional_advertisement_policy_inner_from_dict = LogicalRoutersVrfInnerBgpPolicyConditionalAdvertisementPolicyInner.from_dict(logical_routers_vrf_inner_bgp_policy_conditional_advertisement_policy_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


