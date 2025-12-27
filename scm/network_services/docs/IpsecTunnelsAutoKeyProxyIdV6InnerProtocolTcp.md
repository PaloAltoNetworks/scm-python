# IpsecTunnelsAutoKeyProxyIdV6InnerProtocolTcp

IPv6 type of proxy_id protocol values for TCP protocol

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**local_port** | **int** |  | [optional] [default to 0]
**remote_port** | **int** |  | [optional] [default to 0]

## Example

```python
from scm_network_services.models.ipsec_tunnels_auto_key_proxy_id_v6_inner_protocol_tcp import IpsecTunnelsAutoKeyProxyIdV6InnerProtocolTcp

# TODO update the JSON string below
json = "{}"
# create an instance of IpsecTunnelsAutoKeyProxyIdV6InnerProtocolTcp from a JSON string
ipsec_tunnels_auto_key_proxy_id_v6_inner_protocol_tcp_instance = IpsecTunnelsAutoKeyProxyIdV6InnerProtocolTcp.from_json(json)
# print the JSON string representation of the object
print(IpsecTunnelsAutoKeyProxyIdV6InnerProtocolTcp.to_json())

# convert the object into a dict
ipsec_tunnels_auto_key_proxy_id_v6_inner_protocol_tcp_dict = ipsec_tunnels_auto_key_proxy_id_v6_inner_protocol_tcp_instance.to_dict()
# create an instance of IpsecTunnelsAutoKeyProxyIdV6InnerProtocolTcp from a dict
ipsec_tunnels_auto_key_proxy_id_v6_inner_protocol_tcp_from_dict = IpsecTunnelsAutoKeyProxyIdV6InnerProtocolTcp.from_dict(ipsec_tunnels_auto_key_proxy_id_v6_inner_protocol_tcp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


