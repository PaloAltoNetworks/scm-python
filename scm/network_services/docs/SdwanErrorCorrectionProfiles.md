# SdwanErrorCorrectionProfiles


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**activation_threshold** | **int** |  | 
**device** | **str** | The device in which the resource is defined | [optional] 
**folder** | **str** | The folder in which the resource is defined | [optional] 
**id** | **str** | UUID of the resource | [optional] [readonly] 
**mode** | [**SdwanErrorCorrectionProfilesMode**](SdwanErrorCorrectionProfilesMode.md) |  | 
**name** | **str** |  | 
**snippet** | **str** | The snippet in which the resource is defined | [optional] 

## Example

```python
from scm.network_services.models.sdwan_error_correction_profiles import SdwanErrorCorrectionProfiles

# TODO update the JSON string below
json = "{}"
# create an instance of SdwanErrorCorrectionProfiles from a JSON string
sdwan_error_correction_profiles_instance = SdwanErrorCorrectionProfiles.from_json(json)
# print the JSON string representation of the object
print(SdwanErrorCorrectionProfiles.to_json())

# convert the object into a dict
sdwan_error_correction_profiles_dict = sdwan_error_correction_profiles_instance.to_dict()
# create an instance of SdwanErrorCorrectionProfiles from a dict
sdwan_error_correction_profiles_from_dict = SdwanErrorCorrectionProfiles.from_dict(sdwan_error_correction_profiles_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


