# IpsecTunnels


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**anti_replay** | **bool** | Enable Anti-Replay check on this tunnel | [optional] 
**auto_key** | [**IpsecTunnelsAutoKey**](IpsecTunnelsAutoKey.md) |  | 
**copy_tos** | **bool** | Copy IP TOS bits from inner packet to IPSec packet (not recommended) | [optional] [default to False]
**device** | **str** | The device in which the resource is defined | [optional] 
**enable_gre_encapsulation** | **bool** | allow GRE over IPSec | [optional] [default to False]
**folder** | **str** | The folder in which the resource is defined | [optional] 
**id** | **str** | UUID of the resource | [optional] [readonly] 
**name** | **str** | Alphanumeric string begin with letter: [0-9a-zA-Z._-] | 
**snippet** | **str** | The snippet in which the resource is defined | [optional] 
**tunnel_interface** | **str** | Tunnel interface variable or hardcoded tunnel. Default will be tunnels. | [optional] [default to 'tunnel']
**tunnel_monitor** | [**IpsecTunnelsTunnelMonitor**](IpsecTunnelsTunnelMonitor.md) |  | [optional] 

## Example

```python
from scm.network_services.models.ipsec_tunnels import IpsecTunnels

# TODO update the JSON string below
json = "{}"
# create an instance of IpsecTunnels from a JSON string
ipsec_tunnels_instance = IpsecTunnels.from_json(json)
# print the JSON string representation of the object
print(IpsecTunnels.to_json())

# convert the object into a dict
ipsec_tunnels_dict = ipsec_tunnels_instance.to_dict()
# create an instance of IpsecTunnels from a dict
ipsec_tunnels_from_dict = IpsecTunnels.from_dict(ipsec_tunnels_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


