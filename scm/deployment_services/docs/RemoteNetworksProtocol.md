# RemoteNetworksProtocol

setup the protocol when ecmp_load_balancing is disable

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bgp** | [**RemoteNetworksProtocolBgp**](RemoteNetworksProtocolBgp.md) |  | [optional] 
**bgp_peer** | [**RemoteNetworksProtocolBgpPeer**](RemoteNetworksProtocolBgpPeer.md) |  | [optional] 

## Example

```python
from scm.deployment_services.models.remote_networks_protocol import RemoteNetworksProtocol

# TODO update the JSON string below
json = "{}"
# create an instance of RemoteNetworksProtocol from a JSON string
remote_networks_protocol_instance = RemoteNetworksProtocol.from_json(json)
# print the JSON string representation of the object
print(RemoteNetworksProtocol.to_json())

# convert the object into a dict
remote_networks_protocol_dict = remote_networks_protocol_instance.to_dict()
# create an instance of RemoteNetworksProtocol from a dict
remote_networks_protocol_from_dict = RemoteNetworksProtocol.from_dict(remote_networks_protocol_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


