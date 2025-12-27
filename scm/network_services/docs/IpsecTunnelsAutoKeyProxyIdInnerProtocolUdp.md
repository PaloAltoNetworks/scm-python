# IpsecTunnelsAutoKeyProxyIdInnerProtocolUdp

IPv6 type of proxy_id protocol values for UDP protocol

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**local_port** | **int** |  | [optional] [default to 0]
**remote_port** | **int** |  | [optional] [default to 0]

## Example

```python
from scm_network_services.models.ipsec_tunnels_auto_key_proxy_id_inner_protocol_udp import IpsecTunnelsAutoKeyProxyIdInnerProtocolUdp

# TODO update the JSON string below
json = "{}"
# create an instance of IpsecTunnelsAutoKeyProxyIdInnerProtocolUdp from a JSON string
ipsec_tunnels_auto_key_proxy_id_inner_protocol_udp_instance = IpsecTunnelsAutoKeyProxyIdInnerProtocolUdp.from_json(json)
# print the JSON string representation of the object
print(IpsecTunnelsAutoKeyProxyIdInnerProtocolUdp.to_json())

# convert the object into a dict
ipsec_tunnels_auto_key_proxy_id_inner_protocol_udp_dict = ipsec_tunnels_auto_key_proxy_id_inner_protocol_udp_instance.to_dict()
# create an instance of IpsecTunnelsAutoKeyProxyIdInnerProtocolUdp from a dict
ipsec_tunnels_auto_key_proxy_id_inner_protocol_udp_from_dict = IpsecTunnelsAutoKeyProxyIdInnerProtocolUdp.from_dict(ipsec_tunnels_auto_key_proxy_id_inner_protocol_udp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


