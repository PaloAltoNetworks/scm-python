# Layer3SubInterfacesDhcpClientDhcpClient

Layer3 sub interfaces DHCP Client Object

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**create_default_route** | **bool** | Automatically create default route pointing to default gateway provided by server | [optional] [default to True]
**default_route_metric** | **int** | Metric of the default route created | [optional] [default to 10]
**enable** | **bool** | Enable DHCP? | [optional] [default to True]
**send_hostname** | [**Layer3SubInterfacesDhcpClientDhcpClientSendHostname**](Layer3SubInterfacesDhcpClientDhcpClientSendHostname.md) |  | [optional] 

## Example

```python
from scm.network_services.models.layer3_sub_interfaces_dhcp_client_dhcp_client import Layer3SubInterfacesDhcpClientDhcpClient

# TODO update the JSON string below
json = "{}"
# create an instance of Layer3SubInterfacesDhcpClientDhcpClient from a JSON string
layer3_sub_interfaces_dhcp_client_dhcp_client_instance = Layer3SubInterfacesDhcpClientDhcpClient.from_json(json)
# print the JSON string representation of the object
print(Layer3SubInterfacesDhcpClientDhcpClient.to_json())

# convert the object into a dict
layer3_sub_interfaces_dhcp_client_dhcp_client_dict = layer3_sub_interfaces_dhcp_client_dhcp_client_instance.to_dict()
# create an instance of Layer3SubInterfacesDhcpClientDhcpClient from a dict
layer3_sub_interfaces_dhcp_client_dhcp_client_from_dict = Layer3SubInterfacesDhcpClientDhcpClient.from_dict(layer3_sub_interfaces_dhcp_client_dhcp_client_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


