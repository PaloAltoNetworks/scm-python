# RemoteNetworksProtocolBgpPeer

secondary bgp routing as bgp_peer

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**local_ip_address** | **str** | Local peer IP address (secondary WAN) | [optional] 
**peer_ip_address** | **str** | Remote peer IP address (secondary WAN) | [optional] 
**same_as_primary** | **bool** | Same peer IP address as primary WAN | [optional] 
**secret** | **str** | BGP peering secret (secondary WAN) | [optional] 

## Example

```python
from scm.deployment_services.models.remote_networks_protocol_bgp_peer import RemoteNetworksProtocolBgpPeer

# TODO update the JSON string below
json = "{}"
# create an instance of RemoteNetworksProtocolBgpPeer from a JSON string
remote_networks_protocol_bgp_peer_instance = RemoteNetworksProtocolBgpPeer.from_json(json)
# print the JSON string representation of the object
print(RemoteNetworksProtocolBgpPeer.to_json())

# convert the object into a dict
remote_networks_protocol_bgp_peer_dict = remote_networks_protocol_bgp_peer_instance.to_dict()
# create an instance of RemoteNetworksProtocolBgpPeer from a dict
remote_networks_protocol_bgp_peer_from_dict = RemoteNetworksProtocolBgpPeer.from_dict(remote_networks_protocol_bgp_peer_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


