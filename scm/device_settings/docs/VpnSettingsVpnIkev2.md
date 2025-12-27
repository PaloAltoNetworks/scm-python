# VpnSettingsVpnIkev2


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**certificate_cache_size** | **int** | Maximum cached certificates | [optional] [default to 500]
**cookie_threshold** | **int** | Cookie activation threshold | [optional] [default to 500]
**max_half_opened_sa** | **int** | Maximum half-opened SA | [optional] [default to 65535]

## Example

```python
from scm_device_settings.models.vpn_settings_vpn_ikev2 import VpnSettingsVpnIkev2

# TODO update the JSON string below
json = "{}"
# create an instance of VpnSettingsVpnIkev2 from a JSON string
vpn_settings_vpn_ikev2_instance = VpnSettingsVpnIkev2.from_json(json)
# print the JSON string representation of the object
print(VpnSettingsVpnIkev2.to_json())

# convert the object into a dict
vpn_settings_vpn_ikev2_dict = vpn_settings_vpn_ikev2_instance.to_dict()
# create an instance of VpnSettingsVpnIkev2 from a dict
vpn_settings_vpn_ikev2_from_dict = VpnSettingsVpnIkev2.from_dict(vpn_settings_vpn_ikev2_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


