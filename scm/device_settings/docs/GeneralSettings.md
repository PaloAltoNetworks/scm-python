# GeneralSettings


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**device** | **str** | The device in which the resource is defined | [optional] 
**folder** | **str** | The folder in which the resource is defined | [optional] 
**general** | [**GeneralSettingsGeneral**](GeneralSettingsGeneral.md) |  | [optional] 
**id** | **str** | UUID of the resource | [optional] [readonly] 
**snippet** | **str** | The snippet in which the resource is defined | [optional] 

## Example

```python
from scm_device_settings.models.general_settings import GeneralSettings

# TODO update the JSON string below
json = "{}"
# create an instance of GeneralSettings from a JSON string
general_settings_instance = GeneralSettings.from_json(json)
# print the JSON string representation of the object
print(GeneralSettings.to_json())

# convert the object into a dict
general_settings_dict = general_settings_instance.to_dict()
# create an instance of GeneralSettings from a dict
general_settings_from_dict = GeneralSettings.from_dict(general_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


