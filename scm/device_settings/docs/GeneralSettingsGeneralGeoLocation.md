# GeneralSettingsGeneralGeoLocation

Geographic coordinates

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**latitude** | **str** | Latitude | 
**longitude** | **str** | Longitude | 

## Example

```python
from scm_device_settings.models.general_settings_general_geo_location import GeneralSettingsGeneralGeoLocation

# TODO update the JSON string below
json = "{}"
# create an instance of GeneralSettingsGeneralGeoLocation from a JSON string
general_settings_general_geo_location_instance = GeneralSettingsGeneralGeoLocation.from_json(json)
# print the JSON string representation of the object
print(GeneralSettingsGeneralGeoLocation.to_json())

# convert the object into a dict
general_settings_general_geo_location_dict = general_settings_general_geo_location_instance.to_dict()
# create an instance of GeneralSettingsGeneralGeoLocation from a dict
general_settings_general_geo_location_from_dict = GeneralSettingsGeneralGeoLocation.from_dict(general_settings_general_geo_location_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


