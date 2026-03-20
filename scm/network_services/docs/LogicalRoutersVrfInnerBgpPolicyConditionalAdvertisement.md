# LogicalRoutersVrfInnerBgpPolicyConditionalAdvertisement


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**policy** | [**List[LogicalRoutersVrfInnerBgpPolicyConditionalAdvertisementPolicyInner]**](LogicalRoutersVrfInnerBgpPolicyConditionalAdvertisementPolicyInner.md) |  | [optional] 

## Example

```python
from scm.network_services.models.logical_routers_vrf_inner_bgp_policy_conditional_advertisement import LogicalRoutersVrfInnerBgpPolicyConditionalAdvertisement

# TODO update the JSON string below
json = "{}"
# create an instance of LogicalRoutersVrfInnerBgpPolicyConditionalAdvertisement from a JSON string
logical_routers_vrf_inner_bgp_policy_conditional_advertisement_instance = LogicalRoutersVrfInnerBgpPolicyConditionalAdvertisement.from_json(json)
# print the JSON string representation of the object
print(LogicalRoutersVrfInnerBgpPolicyConditionalAdvertisement.to_json())

# convert the object into a dict
logical_routers_vrf_inner_bgp_policy_conditional_advertisement_dict = logical_routers_vrf_inner_bgp_policy_conditional_advertisement_instance.to_dict()
# create an instance of LogicalRoutersVrfInnerBgpPolicyConditionalAdvertisement from a dict
logical_routers_vrf_inner_bgp_policy_conditional_advertisement_from_dict = LogicalRoutersVrfInnerBgpPolicyConditionalAdvertisement.from_dict(logical_routers_vrf_inner_bgp_policy_conditional_advertisement_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


