# TunnelInterfacesIpInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Tunnel Interface IP address(es) | 

## Example

```python
from scm.network_services.models.tunnel_interfaces_ip_inner import TunnelInterfacesIpInner

# TODO update the JSON string below
json = "{}"
# create an instance of TunnelInterfacesIpInner from a JSON string
tunnel_interfaces_ip_inner_instance = TunnelInterfacesIpInner.from_json(json)
# print the JSON string representation of the object
print(TunnelInterfacesIpInner.to_json())

# convert the object into a dict
tunnel_interfaces_ip_inner_dict = tunnel_interfaces_ip_inner_instance.to_dict()
# create an instance of TunnelInterfacesIpInner from a dict
tunnel_interfaces_ip_inner_from_dict = TunnelInterfacesIpInner.from_dict(tunnel_interfaces_ip_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


