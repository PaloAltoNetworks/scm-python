# DhcpInterfacesServerReservedInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | Reservation description | [optional] 
**mac** | **str** | Reserved MAC address | [optional] 
**name** | **str** | Reserved IP address | [optional] 

## Example

```python
from scm.network_services.models.dhcp_interfaces_server_reserved_inner import DhcpInterfacesServerReservedInner

# TODO update the JSON string below
json = "{}"
# create an instance of DhcpInterfacesServerReservedInner from a JSON string
dhcp_interfaces_server_reserved_inner_instance = DhcpInterfacesServerReservedInner.from_json(json)
# print the JSON string representation of the object
print(DhcpInterfacesServerReservedInner.to_json())

# convert the object into a dict
dhcp_interfaces_server_reserved_inner_dict = dhcp_interfaces_server_reserved_inner_instance.to_dict()
# create an instance of DhcpInterfacesServerReservedInner from a dict
dhcp_interfaces_server_reserved_inner_from_dict = DhcpInterfacesServerReservedInner.from_dict(dhcp_interfaces_server_reserved_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


