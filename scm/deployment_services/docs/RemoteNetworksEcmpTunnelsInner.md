# RemoteNetworksEcmpTunnelsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ipsec_tunnel** | **str** |  | 
**name** | **str** |  | 
**protocol** | [**RemoteNetworksEcmpTunnelsInnerProtocol**](RemoteNetworksEcmpTunnelsInnerProtocol.md) |  | 

## Example

```python
from scm.deployment_services.models.remote_networks_ecmp_tunnels_inner import RemoteNetworksEcmpTunnelsInner

# TODO update the JSON string below
json = "{}"
# create an instance of RemoteNetworksEcmpTunnelsInner from a JSON string
remote_networks_ecmp_tunnels_inner_instance = RemoteNetworksEcmpTunnelsInner.from_json(json)
# print the JSON string representation of the object
print(RemoteNetworksEcmpTunnelsInner.to_json())

# convert the object into a dict
remote_networks_ecmp_tunnels_inner_dict = remote_networks_ecmp_tunnels_inner_instance.to_dict()
# create an instance of RemoteNetworksEcmpTunnelsInner from a dict
remote_networks_ecmp_tunnels_inner_from_dict = RemoteNetworksEcmpTunnelsInner.from_dict(remote_networks_ecmp_tunnels_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


