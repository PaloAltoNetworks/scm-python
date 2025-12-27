# LogicalRoutersVrfInnerBgpPeerGroupInnerPeerInnerConnectionOptions


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**authentication** | **str** |  | [optional] 
**dampening** | **str** |  | [optional] 
**hold_time** | **str** |  | [optional] 
**idle_hold_time** | **int** |  | [optional] 
**incoming_bgp_connection** | [**LogicalRoutersVrfInnerBgpPeerGroupInnerPeerInnerConnectionOptionsIncomingBgpConnection**](LogicalRoutersVrfInnerBgpPeerGroupInnerPeerInnerConnectionOptionsIncomingBgpConnection.md) |  | [optional] 
**keep_alive_interval** | **str** |  | [optional] 
**max_prefixes** | **str** |  | [optional] 
**min_route_adv_interval** | **int** |  | [optional] 
**multihop** | **str** |  | [optional] 
**open_delay_time** | **int** |  | [optional] 
**outgoing_bgp_connection** | [**LogicalRoutersVrfInnerBgpPeerGroupInnerPeerInnerConnectionOptionsOutgoingBgpConnection**](LogicalRoutersVrfInnerBgpPeerGroupInnerPeerInnerConnectionOptionsOutgoingBgpConnection.md) |  | [optional] 
**timers** | **str** |  | [optional] 

## Example

```python
from scm_network_services.models.logical_routers_vrf_inner_bgp_peer_group_inner_peer_inner_connection_options import LogicalRoutersVrfInnerBgpPeerGroupInnerPeerInnerConnectionOptions

# TODO update the JSON string below
json = "{}"
# create an instance of LogicalRoutersVrfInnerBgpPeerGroupInnerPeerInnerConnectionOptions from a JSON string
logical_routers_vrf_inner_bgp_peer_group_inner_peer_inner_connection_options_instance = LogicalRoutersVrfInnerBgpPeerGroupInnerPeerInnerConnectionOptions.from_json(json)
# print the JSON string representation of the object
print(LogicalRoutersVrfInnerBgpPeerGroupInnerPeerInnerConnectionOptions.to_json())

# convert the object into a dict
logical_routers_vrf_inner_bgp_peer_group_inner_peer_inner_connection_options_dict = logical_routers_vrf_inner_bgp_peer_group_inner_peer_inner_connection_options_instance.to_dict()
# create an instance of LogicalRoutersVrfInnerBgpPeerGroupInnerPeerInnerConnectionOptions from a dict
logical_routers_vrf_inner_bgp_peer_group_inner_peer_inner_connection_options_from_dict = LogicalRoutersVrfInnerBgpPeerGroupInnerPeerInnerConnectionOptions.from_dict(logical_routers_vrf_inner_bgp_peer_group_inner_peer_inner_connection_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


