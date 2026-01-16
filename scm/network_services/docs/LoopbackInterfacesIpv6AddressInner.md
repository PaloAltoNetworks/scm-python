# LoopbackInterfacesIpv6AddressInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**anycast** | **object** | Anycast | [optional] 
**enable_on_interface** | **bool** | Enable Address on Interface | [optional] [default to True]
**name** | **str** | IPv6 Address | [optional] 
**prefix** | **object** | Use interface ID as host portion | [optional] 

## Example

```python
from scm.network_services.models.loopback_interfaces_ipv6_address_inner import LoopbackInterfacesIpv6AddressInner

# TODO update the JSON string below
json = "{}"
# create an instance of LoopbackInterfacesIpv6AddressInner from a JSON string
loopback_interfaces_ipv6_address_inner_instance = LoopbackInterfacesIpv6AddressInner.from_json(json)
# print the JSON string representation of the object
print(LoopbackInterfacesIpv6AddressInner.to_json())

# convert the object into a dict
loopback_interfaces_ipv6_address_inner_dict = loopback_interfaces_ipv6_address_inner_instance.to_dict()
# create an instance of LoopbackInterfacesIpv6AddressInner from a dict
loopback_interfaces_ipv6_address_inner_from_dict = LoopbackInterfacesIpv6AddressInner.from_dict(loopback_interfaces_ipv6_address_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


