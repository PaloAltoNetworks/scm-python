# GeneralSettingsGeneralSetting


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**auto_mac_detect** | **bool** | Use hypervisor assigned MAC addresses | [optional] [default to False]
**fail_open** | **bool** | Fail open | [optional] [default to False]
**management** | [**GeneralSettingsGeneralSettingManagement**](GeneralSettingsGeneralSettingManagement.md) |  | [optional] 
**tunnel_acceleration** | **bool** | Tunnel acceleration | [optional] [default to True]

## Example

```python
from scm_device_settings.models.general_settings_general_setting import GeneralSettingsGeneralSetting

# TODO update the JSON string below
json = "{}"
# create an instance of GeneralSettingsGeneralSetting from a JSON string
general_settings_general_setting_instance = GeneralSettingsGeneralSetting.from_json(json)
# print the JSON string representation of the object
print(GeneralSettingsGeneralSetting.to_json())

# convert the object into a dict
general_settings_general_setting_dict = general_settings_general_setting_instance.to_dict()
# create an instance of GeneralSettingsGeneralSetting from a dict
general_settings_general_setting_from_dict = GeneralSettingsGeneralSetting.from_dict(general_settings_general_setting_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


