# LogicalRoutersVrfInnerMulticastMsdp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enable** | **bool** |  | [optional] 
**global_authentication** | **str** |  | [optional] 
**global_timer** | **str** |  | [optional] 
**originator_id** | [**LogicalRoutersVrfInnerBgpPeerGroupInnerPeerInnerLocalAddress**](LogicalRoutersVrfInnerBgpPeerGroupInnerPeerInnerLocalAddress.md) |  | [optional] 
**peer** | [**List[LogicalRoutersVrfInnerMulticastMsdpPeerInner]**](LogicalRoutersVrfInnerMulticastMsdpPeerInner.md) |  | [optional] 

## Example

```python
from scm_network_services.models.logical_routers_vrf_inner_multicast_msdp import LogicalRoutersVrfInnerMulticastMsdp

# TODO update the JSON string below
json = "{}"
# create an instance of LogicalRoutersVrfInnerMulticastMsdp from a JSON string
logical_routers_vrf_inner_multicast_msdp_instance = LogicalRoutersVrfInnerMulticastMsdp.from_json(json)
# print the JSON string representation of the object
print(LogicalRoutersVrfInnerMulticastMsdp.to_json())

# convert the object into a dict
logical_routers_vrf_inner_multicast_msdp_dict = logical_routers_vrf_inner_multicast_msdp_instance.to_dict()
# create an instance of LogicalRoutersVrfInnerMulticastMsdp from a dict
logical_routers_vrf_inner_multicast_msdp_from_dict = LogicalRoutersVrfInnerMulticastMsdp.from_dict(logical_routers_vrf_inner_multicast_msdp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


