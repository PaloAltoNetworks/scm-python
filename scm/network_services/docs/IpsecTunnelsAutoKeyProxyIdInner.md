# IpsecTunnelsAutoKeyProxyIdInner

IPv4 type of proxy_id values for TCP protocol

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**local** | **str** |  | [optional] 
**name** | **str** |  | 
**protocol** | [**IpsecTunnelsAutoKeyProxyIdInnerProtocol**](IpsecTunnelsAutoKeyProxyIdInnerProtocol.md) |  | [optional] 
**remote** | **str** |  | [optional] 

## Example

```python
from scm_network_services.models.ipsec_tunnels_auto_key_proxy_id_inner import IpsecTunnelsAutoKeyProxyIdInner

# TODO update the JSON string below
json = "{}"
# create an instance of IpsecTunnelsAutoKeyProxyIdInner from a JSON string
ipsec_tunnels_auto_key_proxy_id_inner_instance = IpsecTunnelsAutoKeyProxyIdInner.from_json(json)
# print the JSON string representation of the object
print(IpsecTunnelsAutoKeyProxyIdInner.to_json())

# convert the object into a dict
ipsec_tunnels_auto_key_proxy_id_inner_dict = ipsec_tunnels_auto_key_proxy_id_inner_instance.to_dict()
# create an instance of IpsecTunnelsAutoKeyProxyIdInner from a dict
ipsec_tunnels_auto_key_proxy_id_inner_from_dict = IpsecTunnelsAutoKeyProxyIdInner.from_dict(ipsec_tunnels_auto_key_proxy_id_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


