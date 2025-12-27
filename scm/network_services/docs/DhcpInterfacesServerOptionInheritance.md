# DhcpInterfacesServerOptionInheritance


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source** | **str** | Interface from which to inherit lease options | [optional] 

## Example

```python
from scm.network_services.models.dhcp_interfaces_server_option_inheritance import DhcpInterfacesServerOptionInheritance

# TODO update the JSON string below
json = "{}"
# create an instance of DhcpInterfacesServerOptionInheritance from a JSON string
dhcp_interfaces_server_option_inheritance_instance = DhcpInterfacesServerOptionInheritance.from_json(json)
# print the JSON string representation of the object
print(DhcpInterfacesServerOptionInheritance.to_json())

# convert the object into a dict
dhcp_interfaces_server_option_inheritance_dict = dhcp_interfaces_server_option_inheritance_instance.to_dict()
# create an instance of DhcpInterfacesServerOptionInheritance from a dict
dhcp_interfaces_server_option_inheritance_from_dict = DhcpInterfacesServerOptionInheritance.from_dict(dhcp_interfaces_server_option_inheritance_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


