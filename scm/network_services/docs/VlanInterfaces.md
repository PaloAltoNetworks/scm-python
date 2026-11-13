# VlanInterfaces


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**adjust_tcp_mss** | [**AdjustTcpMss**](AdjustTcpMss.md) |  | [optional] 
**arp** | [**List[VlanInterfacesArpInner]**](VlanInterfacesArpInner.md) | ARP configuration | [optional] 
**comment** | **str** | Description | [optional] 
**ddns_config** | [**VlanInterfacesDdnsConfig**](VlanInterfacesDdnsConfig.md) |  | [optional] 
**default_value** | **str** | Default interface assignment | [optional] 
**device** | **str** | The device in which the resource is defined | [optional] 
**dhcp_client** | [**VlanInterfacesDhcpClient**](VlanInterfacesDhcpClient.md) |  | [optional] 
**folder** | **str** | The folder in which the resource is defined | [optional] 
**id** | **str** | UUID of the resource | [optional] [readonly] 
**interface_management_profile** | **str** | Interface management profile | [optional] 
**ip** | [**List[VlanInterfacesIpInner]**](VlanInterfacesIpInner.md) | VLAN Interface IP Parent | [optional] 
**mtu** | **int** | MTU | [optional] 
**name** | **str** | L3 sub-interface name | 
**netflow_profile** | **str** | Name of Netflow Profile to assign to Interface | [optional] 
**snippet** | **str** | The snippet in which the resource is defined | [optional] 
**vlan_tag** | **str** | VLAN tag | [optional] 

## Example

```python
from scm.network_services.models.vlan_interfaces import VlanInterfaces

# TODO update the JSON string below
json = "{}"
# create an instance of VlanInterfaces from a JSON string
vlan_interfaces_instance = VlanInterfaces.from_json(json)
# print the JSON string representation of the object
print(VlanInterfaces.to_json())

# convert the object into a dict
vlan_interfaces_dict = vlan_interfaces_instance.to_dict()
# create an instance of VlanInterfaces from a dict
vlan_interfaces_from_dict = VlanInterfaces.from_dict(vlan_interfaces_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


