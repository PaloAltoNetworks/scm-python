# DhcpInterfacesRelay


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ip** | [**DhcpInterfacesRelayIp**](DhcpInterfacesRelayIp.md) |  | 

## Example

```python
from scm_network_services.models.dhcp_interfaces_relay import DhcpInterfacesRelay

# TODO update the JSON string below
json = "{}"
# create an instance of DhcpInterfacesRelay from a JSON string
dhcp_interfaces_relay_instance = DhcpInterfacesRelay.from_json(json)
# print the JSON string representation of the object
print(DhcpInterfacesRelay.to_json())

# convert the object into a dict
dhcp_interfaces_relay_dict = dhcp_interfaces_relay_instance.to_dict()
# create an instance of DhcpInterfacesRelay from a dict
dhcp_interfaces_relay_from_dict = DhcpInterfacesRelay.from_dict(dhcp_interfaces_relay_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


