# AutoVpnPushConfig


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**auto_vpn_devices** | [**List[AutoVpnPushConfigAutoVpnDevicesInner]**](AutoVpnPushConfigAutoVpnDevicesInner.md) | VPN clusters | [optional] 

## Example

```python
from scm.network_services.models.auto_vpn_push_config import AutoVpnPushConfig

# TODO update the JSON string below
json = "{}"
# create an instance of AutoVpnPushConfig from a JSON string
auto_vpn_push_config_instance = AutoVpnPushConfig.from_json(json)
# print the JSON string representation of the object
print(AutoVpnPushConfig.to_json())

# convert the object into a dict
auto_vpn_push_config_dict = auto_vpn_push_config_instance.to_dict()
# create an instance of AutoVpnPushConfig from a dict
auto_vpn_push_config_from_dict = AutoVpnPushConfig.from_dict(auto_vpn_push_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


