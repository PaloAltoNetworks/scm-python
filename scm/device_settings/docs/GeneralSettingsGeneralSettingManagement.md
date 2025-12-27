# GeneralSettingsGeneralSettingManagement


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**auto_acquire_commit_lock** | **bool** | Automatically acquire commit lock | [optional] [default to False]
**enable_certificate_expiration_check** | **bool** | Certificate expiration check | [optional] [default to False]

## Example

```python
from scm.device_settings.models.general_settings_general_setting_management import GeneralSettingsGeneralSettingManagement

# TODO update the JSON string below
json = "{}"
# create an instance of GeneralSettingsGeneralSettingManagement from a JSON string
general_settings_general_setting_management_instance = GeneralSettingsGeneralSettingManagement.from_json(json)
# print the JSON string representation of the object
print(GeneralSettingsGeneralSettingManagement.to_json())

# convert the object into a dict
general_settings_general_setting_management_dict = general_settings_general_setting_management_instance.to_dict()
# create an instance of GeneralSettingsGeneralSettingManagement from a dict
general_settings_general_setting_management_from_dict = GeneralSettingsGeneralSettingManagement.from_dict(general_settings_general_setting_management_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


