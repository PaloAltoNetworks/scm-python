# MotdBannerSettingsMotdAndBanner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**banner_footer** | **str** |  | [optional] 
**banner_footer_color** | [**MotdColor**](MotdColor.md) |  | [optional] 
**banner_footer_text_color** | [**MotdColor**](MotdColor.md) |  | [optional] 
**banner_header** | **str** |  | [optional] 
**banner_header_color** | [**MotdColor**](MotdColor.md) |  | [optional] 
**banner_header_footer_match** | **bool** |  | [optional] 
**banner_header_text_color** | [**MotdColor**](MotdColor.md) |  | [optional] 
**message** | **str** |  | [optional] 
**motd_color** | [**MotdColor**](MotdColor.md) |  | [optional] 
**motd_do_not_display_again** | **bool** |  | [optional] 
**motd_enable** | **bool** |  | [optional] 
**motd_title** | **str** |  | [optional] 
**severity** | **str** |  | [optional] 

## Example

```python
from scm.device_settings.models.motd_banner_settings_motd_and_banner import MotdBannerSettingsMotdAndBanner

# TODO update the JSON string below
json = "{}"
# create an instance of MotdBannerSettingsMotdAndBanner from a JSON string
motd_banner_settings_motd_and_banner_instance = MotdBannerSettingsMotdAndBanner.from_json(json)
# print the JSON string representation of the object
print(MotdBannerSettingsMotdAndBanner.to_json())

# convert the object into a dict
motd_banner_settings_motd_and_banner_dict = motd_banner_settings_motd_and_banner_instance.to_dict()
# create an instance of MotdBannerSettingsMotdAndBanner from a dict
motd_banner_settings_motd_and_banner_from_dict = MotdBannerSettingsMotdAndBanner.from_dict(motd_banner_settings_motd_and_banner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


