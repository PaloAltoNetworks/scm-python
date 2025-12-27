# IpsecTunnelsAutoKeyProxyIdV6Inner

IPv6 type of proxy_id values for TCP protocol

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**local** | **str** |  | [optional] 
**name** | **str** |  | 
**protocol** | [**IpsecTunnelsAutoKeyProxyIdV6InnerProtocol**](IpsecTunnelsAutoKeyProxyIdV6InnerProtocol.md) |  | [optional] 
**remote** | **str** |  | [optional] 

## Example

```python
from scm_network_services.models.ipsec_tunnels_auto_key_proxy_id_v6_inner import IpsecTunnelsAutoKeyProxyIdV6Inner

# TODO update the JSON string below
json = "{}"
# create an instance of IpsecTunnelsAutoKeyProxyIdV6Inner from a JSON string
ipsec_tunnels_auto_key_proxy_id_v6_inner_instance = IpsecTunnelsAutoKeyProxyIdV6Inner.from_json(json)
# print the JSON string representation of the object
print(IpsecTunnelsAutoKeyProxyIdV6Inner.to_json())

# convert the object into a dict
ipsec_tunnels_auto_key_proxy_id_v6_inner_dict = ipsec_tunnels_auto_key_proxy_id_v6_inner_instance.to_dict()
# create an instance of IpsecTunnelsAutoKeyProxyIdV6Inner from a dict
ipsec_tunnels_auto_key_proxy_id_v6_inner_from_dict = IpsecTunnelsAutoKeyProxyIdV6Inner.from_dict(ipsec_tunnels_auto_key_proxy_id_v6_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


