# EthernetInterfacesDhcpClient

Ethernet Interfaces DHCP Client

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dhcp_client** | [**EthernetInterfacesLayer3DhcpClient**](EthernetInterfacesLayer3DhcpClient.md) |  | [optional] 

## Example

```python
from scm.network_services.models.ethernet_interfaces_dhcp_client import EthernetInterfacesDhcpClient

# TODO update the JSON string below
json = "{}"
# create an instance of EthernetInterfacesDhcpClient from a JSON string
ethernet_interfaces_dhcp_client_instance = EthernetInterfacesDhcpClient.from_json(json)
# print the JSON string representation of the object
print(EthernetInterfacesDhcpClient.to_json())

# convert the object into a dict
ethernet_interfaces_dhcp_client_dict = ethernet_interfaces_dhcp_client_instance.to_dict()
# create an instance of EthernetInterfacesDhcpClient from a dict
ethernet_interfaces_dhcp_client_from_dict = EthernetInterfacesDhcpClient.from_dict(ethernet_interfaces_dhcp_client_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


