# VpnSettings


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**device** | **str** | The device in which the resource is defined | [optional] 
**folder** | **str** | The folder in which the resource is defined | [optional] 
**id** | **str** | UUID of the resource | [optional] [readonly] 
**snippet** | **str** | The snippet in which the resource is defined | [optional] 
**vpn** | [**VpnSettingsVpn**](VpnSettingsVpn.md) |  | [optional] 

## Example

```python
from scm_device_settings.models.vpn_settings import VpnSettings

# TODO update the JSON string below
json = "{}"
# create an instance of VpnSettings from a JSON string
vpn_settings_instance = VpnSettings.from_json(json)
# print the JSON string representation of the object
print(VpnSettings.to_json())

# convert the object into a dict
vpn_settings_dict = vpn_settings_instance.to_dict()
# create an instance of VpnSettings from a dict
vpn_settings_from_dict = VpnSettings.from_dict(vpn_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


