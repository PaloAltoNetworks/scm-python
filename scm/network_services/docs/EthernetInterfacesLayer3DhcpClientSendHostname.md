# EthernetInterfacesLayer3DhcpClientSendHostname

Ethernet Interfaces DHCP ClientSend hostname

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enable** | **bool** |  | [optional] [default to True]
**hostname** | **str** | Set interface hostname | [optional] [default to 'system-hostname']

## Example

```python
from scm.network_services.models.ethernet_interfaces_layer3_dhcp_client_send_hostname import EthernetInterfacesLayer3DhcpClientSendHostname

# TODO update the JSON string below
json = "{}"
# create an instance of EthernetInterfacesLayer3DhcpClientSendHostname from a JSON string
ethernet_interfaces_layer3_dhcp_client_send_hostname_instance = EthernetInterfacesLayer3DhcpClientSendHostname.from_json(json)
# print the JSON string representation of the object
print(EthernetInterfacesLayer3DhcpClientSendHostname.to_json())

# convert the object into a dict
ethernet_interfaces_layer3_dhcp_client_send_hostname_dict = ethernet_interfaces_layer3_dhcp_client_send_hostname_instance.to_dict()
# create an instance of EthernetInterfacesLayer3DhcpClientSendHostname from a dict
ethernet_interfaces_layer3_dhcp_client_send_hostname_from_dict = EthernetInterfacesLayer3DhcpClientSendHostname.from_dict(ethernet_interfaces_layer3_dhcp_client_send_hostname_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


