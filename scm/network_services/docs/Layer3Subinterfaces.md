# Layer3Subinterfaces


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**arp** | [**List[Layer3SubinterfacesArpInner]**](Layer3SubinterfacesArpInner.md) | Layer 3 sub Interfaces ARP configuration | [optional] 
**comment** | **str** | Description | [optional] 
**ddns_config** | [**Layer3SubinterfacesDdnsConfig**](Layer3SubinterfacesDdnsConfig.md) |  | [optional] 
**device** | **str** | The device in which the resource is defined | [optional] 
**dhcp_client** | [**Layer3SubInterfacesDhcpClientDhcpClient**](Layer3SubInterfacesDhcpClientDhcpClient.md) |  | [optional] 
**folder** | **str** | The folder in which the resource is defined | [optional] 
**id** | **str** | UUID of the resource | [optional] [readonly] 
**interface_management_profile** | **str** | Interface management profile | [optional] 
**ip** | [**List[Layer3SubinterfacesIpInner]**](Layer3SubinterfacesIpInner.md) | L3 sub-interface IP Parent | [optional] 
**mtu** | **int** | MTU | [optional] 
**name** | **str** | L3 sub-interface name | 
**parent_interface** | **str** | Parent interface | [optional] 
**snippet** | **str** | The snippet in which the resource is defined | [optional] 
**tag** | **int** | VLAN tag | [optional] 

## Example

```python
from scm.network_services.models.layer3_subinterfaces import Layer3Subinterfaces

# TODO update the JSON string below
json = "{}"
# create an instance of Layer3Subinterfaces from a JSON string
layer3_subinterfaces_instance = Layer3Subinterfaces.from_json(json)
# print the JSON string representation of the object
print(Layer3Subinterfaces.to_json())

# convert the object into a dict
layer3_subinterfaces_dict = layer3_subinterfaces_instance.to_dict()
# create an instance of Layer3Subinterfaces from a dict
layer3_subinterfaces_from_dict = Layer3Subinterfaces.from_dict(layer3_subinterfaces_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


