# IpsecTunnelsAutoKeyProxyIdV6InnerProtocol

IPv6 type of proxy_id protocol values for protocol

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**number** | **int** | IP protocol number | [optional] 
**tcp** | [**IpsecTunnelsAutoKeyProxyIdV6InnerProtocolTcp**](IpsecTunnelsAutoKeyProxyIdV6InnerProtocolTcp.md) |  | [optional] 
**udp** | [**IpsecTunnelsAutoKeyProxyIdInnerProtocolUdp**](IpsecTunnelsAutoKeyProxyIdInnerProtocolUdp.md) |  | [optional] 

## Example

```python
from scm_network_services.models.ipsec_tunnels_auto_key_proxy_id_v6_inner_protocol import IpsecTunnelsAutoKeyProxyIdV6InnerProtocol

# TODO update the JSON string below
json = "{}"
# create an instance of IpsecTunnelsAutoKeyProxyIdV6InnerProtocol from a JSON string
ipsec_tunnels_auto_key_proxy_id_v6_inner_protocol_instance = IpsecTunnelsAutoKeyProxyIdV6InnerProtocol.from_json(json)
# print the JSON string representation of the object
print(IpsecTunnelsAutoKeyProxyIdV6InnerProtocol.to_json())

# convert the object into a dict
ipsec_tunnels_auto_key_proxy_id_v6_inner_protocol_dict = ipsec_tunnels_auto_key_proxy_id_v6_inner_protocol_instance.to_dict()
# create an instance of IpsecTunnelsAutoKeyProxyIdV6InnerProtocol from a dict
ipsec_tunnels_auto_key_proxy_id_v6_inner_protocol_from_dict = IpsecTunnelsAutoKeyProxyIdV6InnerProtocol.from_dict(ipsec_tunnels_auto_key_proxy_id_v6_inner_protocol_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


