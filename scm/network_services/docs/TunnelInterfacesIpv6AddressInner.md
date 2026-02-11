# TunnelInterfacesIpv6AddressInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**anycast** | **object** | Anycast for tunnel interface | [optional] 
**enable_on_interface** | **bool** | Enable Address on Interface for tunnel interface | [optional] [default to True]
**name** | **str** | IPv6 Address for tunnel interface | [optional] 
**prefix** | **object** | Use interface ID as host portion for tunnel interface | [optional] 

## Example

```python
from scm.network_services.models.tunnel_interfaces_ipv6_address_inner import TunnelInterfacesIpv6AddressInner

# TODO update the JSON string below
json = "{}"
# create an instance of TunnelInterfacesIpv6AddressInner from a JSON string
tunnel_interfaces_ipv6_address_inner_instance = TunnelInterfacesIpv6AddressInner.from_json(json)
# print the JSON string representation of the object
print(TunnelInterfacesIpv6AddressInner.to_json())

# convert the object into a dict
tunnel_interfaces_ipv6_address_inner_dict = tunnel_interfaces_ipv6_address_inner_instance.to_dict()
# create an instance of TunnelInterfacesIpv6AddressInner from a dict
tunnel_interfaces_ipv6_address_inner_from_dict = TunnelInterfacesIpv6AddressInner.from_dict(tunnel_interfaces_ipv6_address_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


