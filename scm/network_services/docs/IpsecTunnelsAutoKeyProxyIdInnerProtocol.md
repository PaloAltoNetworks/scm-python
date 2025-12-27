# IpsecTunnelsAutoKeyProxyIdInnerProtocol

IPv4 type of proxy_id protocol values for TCP protocol

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**number** | **int** | IP protocol number | [optional] 
**tcp** | [**IpsecTunnelsAutoKeyProxyIdInnerProtocolTcp**](IpsecTunnelsAutoKeyProxyIdInnerProtocolTcp.md) |  | [optional] 
**udp** | [**IpsecTunnelsAutoKeyProxyIdInnerProtocolUdp**](IpsecTunnelsAutoKeyProxyIdInnerProtocolUdp.md) |  | [optional] 

## Example

```python
from scm_network_services.models.ipsec_tunnels_auto_key_proxy_id_inner_protocol import IpsecTunnelsAutoKeyProxyIdInnerProtocol

# TODO update the JSON string below
json = "{}"
# create an instance of IpsecTunnelsAutoKeyProxyIdInnerProtocol from a JSON string
ipsec_tunnels_auto_key_proxy_id_inner_protocol_instance = IpsecTunnelsAutoKeyProxyIdInnerProtocol.from_json(json)
# print the JSON string representation of the object
print(IpsecTunnelsAutoKeyProxyIdInnerProtocol.to_json())

# convert the object into a dict
ipsec_tunnels_auto_key_proxy_id_inner_protocol_dict = ipsec_tunnels_auto_key_proxy_id_inner_protocol_instance.to_dict()
# create an instance of IpsecTunnelsAutoKeyProxyIdInnerProtocol from a dict
ipsec_tunnels_auto_key_proxy_id_inner_protocol_from_dict = IpsecTunnelsAutoKeyProxyIdInnerProtocol.from_dict(ipsec_tunnels_auto_key_proxy_id_inner_protocol_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


