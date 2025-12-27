# EthernetInterfacesLayer3DhcpClient

Ethernet Interfaces DHCP Client Object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**create_default_route** | **bool** | Automatically create default route pointing to default gateway provided by server | [optional] [default to True]
**default_route_metric** | **int** | Metric of the default route created | [optional] [default to 10]
**enable** | **bool** | Enable DHCP? | [optional] [default to True]
**send_hostname** | [**EthernetInterfacesLayer3DhcpClientSendHostname**](EthernetInterfacesLayer3DhcpClientSendHostname.md) |  | [optional] 

## Example

```python
from scm_network_services.models.ethernet_interfaces_layer3_dhcp_client import EthernetInterfacesLayer3DhcpClient

# TODO update the JSON string below
json = "{}"
# create an instance of EthernetInterfacesLayer3DhcpClient from a JSON string
ethernet_interfaces_layer3_dhcp_client_instance = EthernetInterfacesLayer3DhcpClient.from_json(json)
# print the JSON string representation of the object
print(EthernetInterfacesLayer3DhcpClient.to_json())

# convert the object into a dict
ethernet_interfaces_layer3_dhcp_client_dict = ethernet_interfaces_layer3_dhcp_client_instance.to_dict()
# create an instance of EthernetInterfacesLayer3DhcpClient from a dict
ethernet_interfaces_layer3_dhcp_client_from_dict = EthernetInterfacesLayer3DhcpClient.from_dict(ethernet_interfaces_layer3_dhcp_client_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


