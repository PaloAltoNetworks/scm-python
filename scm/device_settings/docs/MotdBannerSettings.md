# MotdBannerSettings


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**device** | **str** | The device in which the resource is defined | [optional] 
**folder** | **str** | The folder in which the resource is defined | [optional] 
**id** | **str** | UUID of the resource | [optional] [readonly] 
**motd_and_banner** | [**MotdBannerSettingsMotdAndBanner**](MotdBannerSettingsMotdAndBanner.md) |  | [optional] 
**snippet** | **str** | The snippet in which the resource is defined | [optional] 

## Example

```python
from scm_device_settings.models.motd_banner_settings import MotdBannerSettings

# TODO update the JSON string below
json = "{}"
# create an instance of MotdBannerSettings from a JSON string
motd_banner_settings_instance = MotdBannerSettings.from_json(json)
# print the JSON string representation of the object
print(MotdBannerSettings.to_json())

# convert the object into a dict
motd_banner_settings_dict = motd_banner_settings_instance.to_dict()
# create an instance of MotdBannerSettings from a dict
motd_banner_settings_from_dict = MotdBannerSettings.from_dict(motd_banner_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


