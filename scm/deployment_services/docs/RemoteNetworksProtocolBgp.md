# RemoteNetworksProtocolBgp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**do_not_export_routes** | **bool** | Do not export routes? | [optional] 
**enable** | **bool** | Enable BGP peering? | [optional] 
**local_ip_address** | **str** | Local peer IP address | [optional] 
**originate_default_route** | **bool** | Originate default route? | [optional] 
**peer_as** | **str** | BGP peer ASN | [optional] 
**peer_ip_address** | **str** | Remote peer IP address | [optional] 
**peering_type** | **str** | Route exchange types | [optional] 
**secret** | **str** | BGP peering secret | [optional] 
**summarize_mobile_user_routes** | **bool** | Summarize mobile user routes? | [optional] 

## Example

```python
from scm_deployment_services.models.remote_networks_protocol_bgp import RemoteNetworksProtocolBgp

# TODO update the JSON string below
json = "{}"
# create an instance of RemoteNetworksProtocolBgp from a JSON string
remote_networks_protocol_bgp_instance = RemoteNetworksProtocolBgp.from_json(json)
# print the JSON string representation of the object
print(RemoteNetworksProtocolBgp.to_json())

# convert the object into a dict
remote_networks_protocol_bgp_dict = remote_networks_protocol_bgp_instance.to_dict()
# create an instance of RemoteNetworksProtocolBgp from a dict
remote_networks_protocol_bgp_from_dict = RemoteNetworksProtocolBgp.from_dict(remote_networks_protocol_bgp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


