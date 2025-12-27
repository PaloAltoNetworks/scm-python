# LoopbackInterfacesIpv6

Loopback IPv6 Configuration

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | [**List[LoopbackInterfacesIpv6AddressInner]**](LoopbackInterfacesIpv6AddressInner.md) | IPv6 Address Parent | [optional] 
**enabled** | **bool** | Enable IPv6 | [optional] [default to False]

## Example

```python
from scm_network_services.models.loopback_interfaces_ipv6 import LoopbackInterfacesIpv6

# TODO update the JSON string below
json = "{}"
# create an instance of LoopbackInterfacesIpv6 from a JSON string
loopback_interfaces_ipv6_instance = LoopbackInterfacesIpv6.from_json(json)
# print the JSON string representation of the object
print(LoopbackInterfacesIpv6.to_json())

# convert the object into a dict
loopback_interfaces_ipv6_dict = loopback_interfaces_ipv6_instance.to_dict()
# create an instance of LoopbackInterfacesIpv6 from a dict
loopback_interfaces_ipv6_from_dict = LoopbackInterfacesIpv6.from_dict(loopback_interfaces_ipv6_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


