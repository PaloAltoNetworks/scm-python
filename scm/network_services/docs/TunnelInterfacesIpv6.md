# TunnelInterfacesIpv6

Tunnel Interface IPv6 Configuration

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | [**List[LoopbackInterfacesIpv6AddressInner]**](LoopbackInterfacesIpv6AddressInner.md) | IPv6 Address Parent | [optional] 
**enabled** | **bool** | Enable IPv6 | [optional] [default to False]
**interface_id** | **str** | Interface ID | [optional] [default to 'EUI-64']

## Example

```python
from scm.network_services.models.tunnel_interfaces_ipv6 import TunnelInterfacesIpv6

# TODO update the JSON string below
json = "{}"
# create an instance of TunnelInterfacesIpv6 from a JSON string
tunnel_interfaces_ipv6_instance = TunnelInterfacesIpv6.from_json(json)
# print the JSON string representation of the object
print(TunnelInterfacesIpv6.to_json())

# convert the object into a dict
tunnel_interfaces_ipv6_dict = tunnel_interfaces_ipv6_instance.to_dict()
# create an instance of TunnelInterfacesIpv6 from a dict
tunnel_interfaces_ipv6_from_dict = TunnelInterfacesIpv6.from_dict(tunnel_interfaces_ipv6_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


