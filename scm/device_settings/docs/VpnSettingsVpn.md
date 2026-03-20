# VpnSettingsVpn


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ikev2** | [**VpnSettingsVpnIkev2**](VpnSettingsVpnIkev2.md) |  | [optional] 

## Example

```python
from scm.device_settings.models.vpn_settings_vpn import VpnSettingsVpn

# TODO update the JSON string below
json = "{}"
# create an instance of VpnSettingsVpn from a JSON string
vpn_settings_vpn_instance = VpnSettingsVpn.from_json(json)
# print the JSON string representation of the object
print(VpnSettingsVpn.to_json())

# convert the object into a dict
vpn_settings_vpn_dict = vpn_settings_vpn_instance.to_dict()
# create an instance of VpnSettingsVpn from a dict
vpn_settings_vpn_from_dict = VpnSettingsVpn.from_dict(vpn_settings_vpn_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


