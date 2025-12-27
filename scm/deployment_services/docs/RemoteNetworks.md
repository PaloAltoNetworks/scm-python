# RemoteNetworks


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ecmp_load_balancing** | **str** |  | [optional] [default to 'disable']
**ecmp_tunnels** | [**List[RemoteNetworksEcmpTunnelsInner]**](RemoteNetworksEcmpTunnelsInner.md) | ecmp_tunnels is required when ecmp_load_balancing is enable | [optional] 
**folder** | **str** | The folder that contains the remote network | [default to 'Remote Networks']
**id** | **str** | The UUID of the remote network | [readonly] 
**ipsec_tunnel** | **str** | ipsec_tunnel is required when ecmp_load_balancing is disable | [optional] 
**license_type** | **str** | New customer will only be on aggregate bandwidth licensing | [default to 'FWAAS-AGGREGATE']
**name** | **str** | The name of the remote network | 
**protocol** | [**RemoteNetworksProtocol**](RemoteNetworksProtocol.md) |  | [optional] 
**region** | **str** |  | 
**secondary_ipsec_tunnel** | **str** | specify secondary ipsec_tunnel if needed | [optional] 
**spn_name** | **str** | spn-name is needed when license_type is FWAAS-AGGREGATE | [optional] 
**subnets** | **List[str]** |  | [optional] 

## Example

```python
from scm_deployment_services.models.remote_networks import RemoteNetworks

# TODO update the JSON string below
json = "{}"
# create an instance of RemoteNetworks from a JSON string
remote_networks_instance = RemoteNetworks.from_json(json)
# print the JSON string representation of the object
print(RemoteNetworks.to_json())

# convert the object into a dict
remote_networks_dict = remote_networks_instance.to_dict()
# create an instance of RemoteNetworks from a dict
remote_networks_from_dict = RemoteNetworks.from_dict(remote_networks_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


