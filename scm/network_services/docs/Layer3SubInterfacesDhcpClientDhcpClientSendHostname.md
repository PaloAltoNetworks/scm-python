# Layer3SubInterfacesDhcpClientDhcpClientSendHostname

Layer3 sub interfaces DHCP Client Send hostname

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enable** | **bool** |  | [optional] [default to True]
**hostname** | **str** | Set interface hostname | [optional] [default to 'system-hostname']

## Example

```python
from scm.network_services.models.layer3_sub_interfaces_dhcp_client_dhcp_client_send_hostname import Layer3SubInterfacesDhcpClientDhcpClientSendHostname

# TODO update the JSON string below
json = "{}"
# create an instance of Layer3SubInterfacesDhcpClientDhcpClientSendHostname from a JSON string
layer3_sub_interfaces_dhcp_client_dhcp_client_send_hostname_instance = Layer3SubInterfacesDhcpClientDhcpClientSendHostname.from_json(json)
# print the JSON string representation of the object
print(Layer3SubInterfacesDhcpClientDhcpClientSendHostname.to_json())

# convert the object into a dict
layer3_sub_interfaces_dhcp_client_dhcp_client_send_hostname_dict = layer3_sub_interfaces_dhcp_client_dhcp_client_send_hostname_instance.to_dict()
# create an instance of Layer3SubInterfacesDhcpClientDhcpClientSendHostname from a dict
layer3_sub_interfaces_dhcp_client_dhcp_client_send_hostname_from_dict = Layer3SubInterfacesDhcpClientDhcpClientSendHostname.from_dict(layer3_sub_interfaces_dhcp_client_dhcp_client_send_hostname_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


