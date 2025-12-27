# SdwanSaasQualityProfiles


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**device** | **str** | The device in which the resource is defined | [optional] 
**folder** | **str** | The folder in which the resource is defined | [optional] 
**id** | **str** | UUID of the resource | [optional] [readonly] 
**monitor_mode** | [**SdwanSaasQualityProfilesMonitorMode**](SdwanSaasQualityProfilesMonitorMode.md) |  | 
**name** | **str** | Profile name | 
**snippet** | **str** | The snippet in which the resource is defined | [optional] 

## Example

```python
from scm.network_services.models.sdwan_saas_quality_profiles import SdwanSaasQualityProfiles

# TODO update the JSON string below
json = "{}"
# create an instance of SdwanSaasQualityProfiles from a JSON string
sdwan_saas_quality_profiles_instance = SdwanSaasQualityProfiles.from_json(json)
# print the JSON string representation of the object
print(SdwanSaasQualityProfiles.to_json())

# convert the object into a dict
sdwan_saas_quality_profiles_dict = sdwan_saas_quality_profiles_instance.to_dict()
# create an instance of SdwanSaasQualityProfiles from a dict
sdwan_saas_quality_profiles_from_dict = SdwanSaasQualityProfiles.from_dict(sdwan_saas_quality_profiles_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


