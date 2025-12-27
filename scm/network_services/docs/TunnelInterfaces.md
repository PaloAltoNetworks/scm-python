# TunnelInterfaces


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**comment** | **str** | Description | [optional] 
**default_value** | **str** | Default interface assignment | [optional] 
**device** | **str** | The device in which the resource is defined | [optional] 
**folder** | **str** | The folder in which the resource is defined | [optional] 
**id** | **str** | UUID of the resource | [optional] [readonly] 
**interface_management_profile** | **str** | Interface management profile | [optional] 
**ip** | [**List[TunnelInterfacesIpInner]**](TunnelInterfacesIpInner.md) | Tunnel Interface IP Parent | [optional] 
**mtu** | **int** | MTU | [optional] 
**name** | **str** | L3 sub-interface name | 
**snippet** | **str** | The snippet in which the resource is defined | [optional] 

## Example

```python
from scm_network_services.models.tunnel_interfaces import TunnelInterfaces

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


