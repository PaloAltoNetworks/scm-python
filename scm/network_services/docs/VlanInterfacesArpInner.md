# VlanInterfacesArpInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hw_address** | **str** | MAC address | [optional] 
**interface** | **str** | ARP interface | [optional] 
**name** | **str** | IP address | [optional] 

## Example

```python
from scm_network_services.models.vlan_interfaces_arp_inner import VlanInterfacesArpInner

# TODO update the JSON string below
json = "{}"
# create an instance of VlanInterfacesArpInner from a JSON string
vlan_interfaces_arp_inner_instance = VlanInterfacesArpInner.from_json(json)
# print the JSON string representation of the object
print(VlanInterfacesArpInner.to_json())

# convert the object into a dict
vlan_interfaces_arp_inner_dict = vlan_interfaces_arp_inner_instance.to_dict()
# create an instance of VlanInterfacesArpInner from a dict
vlan_interfaces_arp_inner_from_dict = VlanInterfacesArpInner.from_dict(vlan_interfaces_arp_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


