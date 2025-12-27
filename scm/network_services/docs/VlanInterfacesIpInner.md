# VlanInterfacesIpInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | VLAN Interface IP address(es) | 

## Example

```python
from scm_network_services.models.vlan_interfaces_ip_inner import VlanInterfacesIpInner

# TODO update the JSON string below
json = "{}"
# create an instance of VlanInterfacesIpInner from a JSON string
vlan_interfaces_ip_inner_instance = VlanInterfacesIpInner.from_json(json)
# print the JSON string representation of the object
print(VlanInterfacesIpInner.to_json())

# convert the object into a dict
vlan_interfaces_ip_inner_dict = vlan_interfaces_ip_inner_instance.to_dict()
# create an instance of VlanInterfacesIpInner from a dict
vlan_interfaces_ip_inner_from_dict = VlanInterfacesIpInner.from_dict(vlan_interfaces_ip_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


