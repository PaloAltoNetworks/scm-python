# SdwanPathQualityProfiles


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**device** | **str** | The device in which the resource is defined | [optional] 
**folder** | **str** | The folder in which the resource is defined | [optional] 
**id** | **str** | UUID of the resource | [optional] [readonly] 
**metric** | [**SdwanPathQualityProfilesMetric**](SdwanPathQualityProfilesMetric.md) |  | 
**name** | **str** | Profile name | 
**snippet** | **str** | The snippet in which the resource is defined | [optional] 

## Example

```python
from scm_network_services.models.sdwan_path_quality_profiles import SdwanPathQualityProfiles

# TODO update the JSON string below
json = "{}"
# create an instance of SdwanPathQualityProfiles from a JSON string
sdwan_path_quality_profiles_instance = SdwanPathQualityProfiles.from_json(json)
# print the JSON string representation of the object
print(SdwanPathQualityProfiles.to_json())

# convert the object into a dict
sdwan_path_quality_profiles_dict = sdwan_path_quality_profiles_instance.to_dict()
# create an instance of SdwanPathQualityProfiles from a dict
sdwan_path_quality_profiles_from_dict = SdwanPathQualityProfiles.from_dict(sdwan_path_quality_profiles_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


