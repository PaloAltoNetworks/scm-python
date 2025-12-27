# DhcpInterfacesServer


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ip_pool** | **List[str]** | List of IP address pools | [optional] 
**mode** | **str** | DHCP server mode | [optional] 
**option** | [**DhcpInterfacesServerOption**](DhcpInterfacesServerOption.md) |  | [optional] 
**probe_ip** | **bool** | Ping IP before allocating? | [optional] 
**reserved** | [**List[DhcpInterfacesServerReservedInner]**](DhcpInterfacesServerReservedInner.md) | List of IP reservations | [optional] 

## Example

```python
from scm_network_services.models.dhcp_interfaces_server import DhcpInterfacesServer

# TODO update the JSON string below
json = "{}"
# create an instance of DhcpInterfacesServer from a JSON string
dhcp_interfaces_server_instance = DhcpInterfacesServer.from_json(json)
# print the JSON string representation of the object
print(DhcpInterfacesServer.to_json())

# convert the object into a dict
dhcp_interfaces_server_dict = dhcp_interfaces_server_instance.to_dict()
# create an instance of DhcpInterfacesServer from a dict
dhcp_interfaces_server_from_dict = DhcpInterfacesServer.from_dict(dhcp_interfaces_server_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


