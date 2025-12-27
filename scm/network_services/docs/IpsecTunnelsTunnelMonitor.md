# IpsecTunnelsTunnelMonitor


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**destination_ip** | **str** | Destination IP to send ICMP probe | 
**enable** | **bool** | Enable tunnel monitoring on this tunnel | [optional] [default to True]
**proxy_id** | **str** | Which proxy-id (or proxy-id-v6) the monitoring traffic will use | [optional] 

## Example

```python
from scm_network_services.models.ipsec_tunnels_tunnel_monitor import IpsecTunnelsTunnelMonitor

# TODO update the JSON string below
json = "{}"
# create an instance of IpsecTunnelsTunnelMonitor from a JSON string
ipsec_tunnels_tunnel_monitor_instance = IpsecTunnelsTunnelMonitor.from_json(json)
# print the JSON string representation of the object
print(IpsecTunnelsTunnelMonitor.to_json())

# convert the object into a dict
ipsec_tunnels_tunnel_monitor_dict = ipsec_tunnels_tunnel_monitor_instance.to_dict()
# create an instance of IpsecTunnelsTunnelMonitor from a dict
ipsec_tunnels_tunnel_monitor_from_dict = IpsecTunnelsTunnelMonitor.from_dict(ipsec_tunnels_tunnel_monitor_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


