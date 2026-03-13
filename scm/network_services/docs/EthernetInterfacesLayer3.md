# EthernetInterfacesLayer3

Ethernet Interface Layer 3 configuration

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**arp** | [**List[EthernetInterfacesArpInner]**](EthernetInterfacesArpInner.md) | Ethernet Interfaces ARP configuration | [optional] 
**ddns_config** | [**EthernetInterfacesLayer3DdnsConfig**](EthernetInterfacesLayer3DdnsConfig.md) |  | [optional] 
**dhcp_client** | [**EthernetInterfacesLayer3DhcpClient**](EthernetInterfacesLayer3DhcpClient.md) |  | [optional] 
**interface_management_profile** | **str** | Interface management profile | [optional] 
**ip** | [**List[EthernetInterfacesLayer3IpInner]**](EthernetInterfacesLayer3IpInner.md) | Ethernet Interface IP addresses | [optional] 
**mtu** | **int** | MTU | [optional] [default to 1500]
**netflow_profile** | **str** | Name of Netflow Profile to assign to Interface | [optional] 
**pppoe** | [**EthernetInterfacesLayer3Pppoe**](EthernetInterfacesLayer3Pppoe.md) |  | [optional] 

## Example

```python
from scm.network_services.models.ethernet_interfaces_layer3 import EthernetInterfacesLayer3

# TODO update the JSON string below
json = "{}"
# create an instance of EthernetInterfacesLayer3 from a JSON string
ethernet_interfaces_layer3_instance = EthernetInterfacesLayer3.from_json(json)
# print the JSON string representation of the object
print(EthernetInterfacesLayer3.to_json())

# convert the object into a dict
ethernet_interfaces_layer3_dict = ethernet_interfaces_layer3_instance.to_dict()
# create an instance of EthernetInterfacesLayer3 from a dict
ethernet_interfaces_layer3_from_dict = EthernetInterfacesLayer3.from_dict(ethernet_interfaces_layer3_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


