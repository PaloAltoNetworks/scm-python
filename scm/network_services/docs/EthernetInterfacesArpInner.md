# EthernetInterfacesArpInner

Ethernet Interfaces ARP configuration object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hw_address** | **str** | MAC address | [optional] 
**name** | **str** | IP address | [optional] 

## Example

```python
from scm.network_services.models.ethernet_interfaces_arp_inner import EthernetInterfacesArpInner

# TODO update the JSON string below
json = "{}"
# create an instance of EthernetInterfacesArpInner from a JSON string
ethernet_interfaces_arp_inner_instance = EthernetInterfacesArpInner.from_json(json)
# print the JSON string representation of the object
print(EthernetInterfacesArpInner.to_json())

# convert the object into a dict
ethernet_interfaces_arp_inner_dict = ethernet_interfaces_arp_inner_instance.to_dict()
# create an instance of EthernetInterfacesArpInner from a dict
ethernet_interfaces_arp_inner_from_dict = EthernetInterfacesArpInner.from_dict(ethernet_interfaces_arp_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


