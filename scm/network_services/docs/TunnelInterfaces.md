# TunnelInterfaces


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**comment** | **str** | Description for tunnel interface | [optional] 
**default_value** | **str** | Default interface assignment for tunnel interface | [optional] 
**device** | **str** | The device in which the resource is defined | [optional] 
**folder** | **str** | The folder in which the resource is defined | [optional] 
**id** | **str** | UUID of the resource for tunnel interface | [optional] [readonly] 
**interface_management_profile** | **str** | Interface management profile for tunnel interface | [optional] 
**ip** | [**List[TunnelInterfacesIpInner]**](TunnelInterfacesIpInner.md) | Tunnel Interface IP Parent | [optional] 
**ipv6** | [**TunnelInterfacesIpv6**](TunnelInterfacesIpv6.md) |  | [optional] 
**mtu** | **int** | MTU for tunnel interface | [optional] 
**name** | **str** | L3 sub-interface name for tunnel interface | 
**netflow_profile** | **str** | Name of Netflow Profile to assign to Interface | [optional] 
**snippet** | **str** | The snippet in which the resource is defined | [optional] 

## Example

```python
from scm.network_services.models.tunnel_interfaces import TunnelInterfaces

# TODO update the JSON string below
json = "{}"
# create an instance of TunnelInterfaces from a JSON string
tunnel_interfaces_instance = TunnelInterfaces.from_json(json)
# print the JSON string representation of the object
print(TunnelInterfaces.to_json())

# convert the object into a dict
tunnel_interfaces_dict = tunnel_interfaces_instance.to_dict()
# create an instance of TunnelInterfaces from a dict
tunnel_interfaces_from_dict = TunnelInterfaces.from_dict(tunnel_interfaces_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


