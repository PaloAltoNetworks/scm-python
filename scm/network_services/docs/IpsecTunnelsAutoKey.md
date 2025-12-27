# IpsecTunnelsAutoKey


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ike_gateway** | [**List[IpsecTunnelsAutoKeyIkeGatewayInner]**](IpsecTunnelsAutoKeyIkeGatewayInner.md) |  | 
**ipsec_crypto_profile** | **str** |  | 
**proxy_id** | [**List[IpsecTunnelsAutoKeyProxyIdInner]**](IpsecTunnelsAutoKeyProxyIdInner.md) | IPv4 type of proxy_id values | [optional] 
**proxy_id_v6** | [**List[IpsecTunnelsAutoKeyProxyIdV6Inner]**](IpsecTunnelsAutoKeyProxyIdV6Inner.md) | IPv6 type of proxy_id values | [optional] 

## Example

```python
from scm.network_services.models.ipsec_tunnels_auto_key import IpsecTunnelsAutoKey

# TODO update the JSON string below
json = "{}"
# create an instance of IpsecTunnelsAutoKey from a JSON string
ipsec_tunnels_auto_key_instance = IpsecTunnelsAutoKey.from_json(json)
# print the JSON string representation of the object
print(IpsecTunnelsAutoKey.to_json())

# convert the object into a dict
ipsec_tunnels_auto_key_dict = ipsec_tunnels_auto_key_instance.to_dict()
# create an instance of IpsecTunnelsAutoKey from a dict
ipsec_tunnels_auto_key_from_dict = IpsecTunnelsAutoKey.from_dict(ipsec_tunnels_auto_key_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


