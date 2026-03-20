# LogicalRoutersVrfInnerBgpPeerGroupInnerPeerInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bfd** | [**LogicalRoutersVrfInnerBgpPeerGroupInnerPeerInnerBfd**](LogicalRoutersVrfInnerBgpPeerGroupInnerPeerInnerBfd.md) |  | [optional] 
**connection_options** | [**LogicalRoutersVrfInnerBgpPeerGroupInnerPeerInnerConnectionOptions**](LogicalRoutersVrfInnerBgpPeerGroupInnerPeerInnerConnectionOptions.md) |  | [optional] 
**enable** | **bool** |  | [optional] 
**enable_mp_bgp** | **bool** |  | [optional] 
**enable_sender_side_loop_detection** | **bool** |  | [optional] 
**inherit** | [**LogicalRoutersVrfInnerBgpPeerGroupInnerPeerInnerInherit**](LogicalRoutersVrfInnerBgpPeerGroupInnerPeerInnerInherit.md) |  | [optional] 
**local_address** | [**LogicalRoutersVrfInnerBgpPeerGroupInnerPeerInnerLocalAddress**](LogicalRoutersVrfInnerBgpPeerGroupInnerPeerInnerLocalAddress.md) |  | [optional] 
**name** | **str** |  | 
**passive** | **bool** |  | [optional] 
**peer_address** | [**LogicalRoutersVrfInnerBgpPeerGroupInnerPeerInnerPeerAddress**](LogicalRoutersVrfInnerBgpPeerGroupInnerPeerInnerPeerAddress.md) |  | [optional] 
**peer_as** | **str** |  | [optional] 
**peering_type** | **str** |  | [optional] 
**reflector_client** | **str** |  | [optional] 
**subsequent_address_family_identifier** | [**LogicalRoutersVrfInnerBgpPeerGroupInnerPeerInnerSubsequentAddressFamilyIdentifier**](LogicalRoutersVrfInnerBgpPeerGroupInnerPeerInnerSubsequentAddressFamilyIdentifier.md) |  | [optional] 

## Example

```python
from scm.network_services.models.logical_routers_vrf_inner_bgp_peer_group_inner_peer_inner import LogicalRoutersVrfInnerBgpPeerGroupInnerPeerInner

# TODO update the JSON string below
json = "{}"
# create an instance of LogicalRoutersVrfInnerBgpPeerGroupInnerPeerInner from a JSON string
logical_routers_vrf_inner_bgp_peer_group_inner_peer_inner_instance = LogicalRoutersVrfInnerBgpPeerGroupInnerPeerInner.from_json(json)
# print the JSON string representation of the object
print(LogicalRoutersVrfInnerBgpPeerGroupInnerPeerInner.to_json())

# convert the object into a dict
logical_routers_vrf_inner_bgp_peer_group_inner_peer_inner_dict = logical_routers_vrf_inner_bgp_peer_group_inner_peer_inner_instance.to_dict()
# create an instance of LogicalRoutersVrfInnerBgpPeerGroupInnerPeerInner from a dict
logical_routers_vrf_inner_bgp_peer_group_inner_peer_inner_from_dict = LogicalRoutersVrfInnerBgpPeerGroupInnerPeerInner.from_dict(logical_routers_vrf_inner_bgp_peer_group_inner_peer_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


