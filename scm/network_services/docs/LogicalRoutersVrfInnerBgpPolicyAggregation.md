# LogicalRoutersVrfInnerBgpPolicyAggregation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | [**List[LogicalRoutersVrfInnerBgpPolicyAggregationAddressInner]**](LogicalRoutersVrfInnerBgpPolicyAggregationAddressInner.md) |  | [optional] 

## Example

```python
from scm_network_services.models.logical_routers_vrf_inner_bgp_policy_aggregation import LogicalRoutersVrfInnerBgpPolicyAggregation

# TODO update the JSON string below
json = "{}"
# create an instance of LogicalRoutersVrfInnerBgpPolicyAggregation from a JSON string
logical_routers_vrf_inner_bgp_policy_aggregation_instance = LogicalRoutersVrfInnerBgpPolicyAggregation.from_json(json)
# print the JSON string representation of the object
print(LogicalRoutersVrfInnerBgpPolicyAggregation.to_json())

# convert the object into a dict
logical_routers_vrf_inner_bgp_policy_aggregation_dict = logical_routers_vrf_inner_bgp_policy_aggregation_instance.to_dict()
# create an instance of LogicalRoutersVrfInnerBgpPolicyAggregation from a dict
logical_routers_vrf_inner_bgp_policy_aggregation_from_dict = LogicalRoutersVrfInnerBgpPolicyAggregation.from_dict(logical_routers_vrf_inner_bgp_policy_aggregation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


