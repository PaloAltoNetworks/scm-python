# LogicalRoutersVrfInnerMulticastRpLocalRp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**candidate_rp** | [**LogicalRoutersVrfInnerMulticastRpLocalRpCandidateRp**](LogicalRoutersVrfInnerMulticastRpLocalRpCandidateRp.md) |  | [optional] 
**static_rp** | [**LogicalRoutersVrfInnerMulticastRpLocalRpStaticRp**](LogicalRoutersVrfInnerMulticastRpLocalRpStaticRp.md) |  | [optional] 

## Example

```python
from scm.network_services.models.logical_routers_vrf_inner_multicast_rp_local_rp import LogicalRoutersVrfInnerMulticastRpLocalRp

# TODO update the JSON string below
json = "{}"
# create an instance of LogicalRoutersVrfInnerMulticastRpLocalRp from a JSON string
logical_routers_vrf_inner_multicast_rp_local_rp_instance = LogicalRoutersVrfInnerMulticastRpLocalRp.from_json(json)
# print the JSON string representation of the object
print(LogicalRoutersVrfInnerMulticastRpLocalRp.to_json())

# convert the object into a dict
logical_routers_vrf_inner_multicast_rp_local_rp_dict = logical_routers_vrf_inner_multicast_rp_local_rp_instance.to_dict()
# create an instance of LogicalRoutersVrfInnerMulticastRpLocalRp from a dict
logical_routers_vrf_inner_multicast_rp_local_rp_from_dict = LogicalRoutersVrfInnerMulticastRpLocalRp.from_dict(logical_routers_vrf_inner_multicast_rp_local_rp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


