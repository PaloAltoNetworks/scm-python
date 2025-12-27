# AutoVpnPushConfigAutoVpnDevicesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | VPN cluster to push to | [optional] 
**refresh_psk** | **bool** |  | [optional] [default to True]

## Example

```python
from scm_network_services.models.auto_vpn_push_config_auto_vpn_devices_inner import AutoVpnPushConfigAutoVpnDevicesInner

# TODO update the JSON string below
json = "{}"
# create an instance of AutoVpnPushConfigAutoVpnDevicesInner from a JSON string
auto_vpn_push_config_auto_vpn_devices_inner_instance = AutoVpnPushConfigAutoVpnDevicesInner.from_json(json)
# print the JSON string representation of the object
print(AutoVpnPushConfigAutoVpnDevicesInner.to_json())

# convert the object into a dict
auto_vpn_push_config_auto_vpn_devices_inner_dict = auto_vpn_push_config_auto_vpn_devices_inner_instance.to_dict()
# create an instance of AutoVpnPushConfigAutoVpnDevicesInner from a dict
auto_vpn_push_config_auto_vpn_devices_inner_from_dict = AutoVpnPushConfigAutoVpnDevicesInner.from_dict(auto_vpn_push_config_auto_vpn_devices_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


