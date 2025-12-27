# LogicalRoutersVrfInnerMulticastMsdpPeerInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**authentication** | **str** |  | [optional] 
**enable** | **bool** |  | [optional] 
**inbound_sa_filter** | **str** |  | [optional] 
**local_address** | [**LogicalRoutersVrfInnerBgpPeerGroupInnerPeerInnerLocalAddress**](LogicalRoutersVrfInnerBgpPeerGroupInnerPeerInnerLocalAddress.md) |  | [optional] 
**max_sa** | **int** |  | [optional] 
**name** | **str** |  | 
**outbound_sa_filter** | **str** |  | [optional] 
**peer_address** | [**LogicalRoutersVrfInnerBgpPeerGroupInnerPeerInnerPeerAddress**](LogicalRoutersVrfInnerBgpPeerGroupInnerPeerInnerPeerAddress.md) |  | [optional] 
**peer_as** | **str** |  | [optional] 

## Example

```python
from scm.network_services.models.logical_routers_vrf_inner_multicast_msdp_peer_inner import LogicalRoutersVrfInnerMulticastMsdpPeerInner

# TODO update the JSON string below
json = "{}"
# create an instance of LogicalRoutersVrfInnerMulticastMsdpPeerInner from a JSON string
logical_routers_vrf_inner_multicast_msdp_peer_inner_instance = LogicalRoutersVrfInnerMulticastMsdpPeerInner.from_json(json)
# print the JSON string representation of the object
print(LogicalRoutersVrfInnerMulticastMsdpPeerInner.to_json())

# convert the object into a dict
logical_routers_vrf_inner_multicast_msdp_peer_inner_dict = logical_routers_vrf_inner_multicast_msdp_peer_inner_instance.to_dict()
# create an instance of LogicalRoutersVrfInnerMulticastMsdpPeerInner from a dict
logical_routers_vrf_inner_multicast_msdp_peer_inner_from_dict = LogicalRoutersVrfInnerMulticastMsdpPeerInner.from_dict(logical_routers_vrf_inner_multicast_msdp_peer_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


