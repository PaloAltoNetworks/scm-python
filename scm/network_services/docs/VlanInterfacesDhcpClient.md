# VlanInterfacesDhcpClient

Vlan interfaces DHCP Client Object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**create_default_route** | **bool** | Automatically create default route pointing to default gateway provided by server | [optional] [default to True]
**default_route_metric** | **int** | Metric of the default route created | [optional] [default to 10]
**enable** | **bool** | Enable DHCP? | [optional] [default to True]
**send_hostname** | [**VlanInterfacesDhcpClientSendHostname**](VlanInterfacesDhcpClientSendHostname.md) |  | [optional] 

## Example

```python
from scm.network_services.models.vlan_interfaces_dhcp_client import VlanInterfacesDhcpClient

# TODO update the JSON string below
json = "{}"
# create an instance of VlanInterfacesDhcpClient from a JSON string
vlan_interfaces_dhcp_client_instance = VlanInterfacesDhcpClient.from_json(json)
# print the JSON string representation of the object
print(VlanInterfacesDhcpClient.to_json())

# convert the object into a dict
vlan_interfaces_dhcp_client_dict = vlan_interfaces_dhcp_client_instance.to_dict()
# create an instance of VlanInterfacesDhcpClient from a dict
vlan_interfaces_dhcp_client_from_dict = VlanInterfacesDhcpClient.from_dict(vlan_interfaces_dhcp_client_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


