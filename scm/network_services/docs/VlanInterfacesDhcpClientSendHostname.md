# VlanInterfacesDhcpClientSendHostname

Send hostname

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enable** | **bool** |  | [optional] [default to True]
**hostname** | **str** | Set interface hostname | [optional] [default to 'system-hostname']

## Example

```python
from scm.network_services.models.vlan_interfaces_dhcp_client_send_hostname import VlanInterfacesDhcpClientSendHostname

# TODO update the JSON string below
json = "{}"
# create an instance of VlanInterfacesDhcpClientSendHostname from a JSON string
vlan_interfaces_dhcp_client_send_hostname_instance = VlanInterfacesDhcpClientSendHostname.from_json(json)
# print the JSON string representation of the object
print(VlanInterfacesDhcpClientSendHostname.to_json())

# convert the object into a dict
vlan_interfaces_dhcp_client_send_hostname_dict = vlan_interfaces_dhcp_client_send_hostname_instance.to_dict()
# create an instance of VlanInterfacesDhcpClientSendHostname from a dict
vlan_interfaces_dhcp_client_send_hostname_from_dict = VlanInterfacesDhcpClientSendHostname.from_dict(vlan_interfaces_dhcp_client_send_hostname_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


