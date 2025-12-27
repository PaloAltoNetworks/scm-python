# LogicalRoutersVrfInnerMulticastPimRpLocalRp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**candidate_rp** | [**LogicalRoutersVrfInnerMulticastPimRpLocalRpCandidateRp**](LogicalRoutersVrfInnerMulticastPimRpLocalRpCandidateRp.md) |  | [optional] 
**static_rp** | [**LogicalRoutersVrfInnerMulticastPimRpLocalRpStaticRp**](LogicalRoutersVrfInnerMulticastPimRpLocalRpStaticRp.md) |  | [optional] 

## Example

```python
from scm_network_services.models.logical_routers_vrf_inner_multicast_pim_rp_local_rp import LogicalRoutersVrfInnerMulticastPimRpLocalRp

# TODO update the JSON string below
json = "{}"
# create an instance of LogicalRoutersVrfInnerMulticastPimRpLocalRp from a JSON string
logical_routers_vrf_inner_multicast_pim_rp_local_rp_instance = LogicalRoutersVrfInnerMulticastPimRpLocalRp.from_json(json)
# print the JSON string representation of the object
print(LogicalRoutersVrfInnerMulticastPimRpLocalRp.to_json())

# convert the object into a dict
logical_routers_vrf_inner_multicast_pim_rp_local_rp_dict = logical_routers_vrf_inner_multicast_pim_rp_local_rp_instance.to_dict()
# create an instance of LogicalRoutersVrfInnerMulticastPimRpLocalRp from a dict
logical_routers_vrf_inner_multicast_pim_rp_local_rp_from_dict = LogicalRoutersVrfInnerMulticastPimRpLocalRp.from_dict(logical_routers_vrf_inner_multicast_pim_rp_local_rp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


