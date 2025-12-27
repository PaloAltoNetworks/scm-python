# SdwanErrorCorrectionProfilesMode


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**forward_error_correction** | [**SdwanErrorCorrectionProfilesModeForwardErrorCorrection**](SdwanErrorCorrectionProfilesModeForwardErrorCorrection.md) |  | [optional] 
**packet_duplication** | [**SdwanErrorCorrectionProfilesModePacketDuplication**](SdwanErrorCorrectionProfilesModePacketDuplication.md) |  | [optional] 

## Example

```python
from scm.network_services.models.sdwan_error_correction_profiles_mode import SdwanErrorCorrectionProfilesMode

# TODO update the JSON string below
json = "{}"
# create an instance of SdwanErrorCorrectionProfilesMode from a JSON string
sdwan_error_correction_profiles_mode_instance = SdwanErrorCorrectionProfilesMode.from_json(json)
# print the JSON string representation of the object
print(SdwanErrorCorrectionProfilesMode.to_json())

# convert the object into a dict
sdwan_error_correction_profiles_mode_dict = sdwan_error_correction_profiles_mode_instance.to_dict()
# create an instance of SdwanErrorCorrectionProfilesMode from a dict
sdwan_error_correction_profiles_mode_from_dict = SdwanErrorCorrectionProfilesMode.from_dict(sdwan_error_correction_profiles_mode_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


