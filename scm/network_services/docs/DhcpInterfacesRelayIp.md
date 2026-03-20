# DhcpInterfacesRelayIp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | **bool** | Enabled? | [default to True]
**server** | **List[str]** |  | 

## Example

```python
from scm.network_services.models.dhcp_interfaces_relay_ip import DhcpInterfacesRelayIp

# TODO update the JSON string below
json = "{}"
# create an instance of DhcpInterfacesRelayIp from a JSON string
dhcp_interfaces_relay_ip_instance = DhcpInterfacesRelayIp.from_json(json)
# print the JSON string representation of the object
print(DhcpInterfacesRelayIp.to_json())

# convert the object into a dict
dhcp_interfaces_relay_ip_dict = dhcp_interfaces_relay_ip_instance.to_dict()
# create an instance of DhcpInterfacesRelayIp from a dict
dhcp_interfaces_relay_ip_from_dict = DhcpInterfacesRelayIp.from_dict(dhcp_interfaces_relay_ip_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


