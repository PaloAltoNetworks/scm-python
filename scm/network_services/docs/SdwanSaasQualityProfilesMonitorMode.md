# SdwanSaasQualityProfilesMonitorMode


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**adaptive** | **object** |  | [optional] 
**http_https** | [**SdwanSaasQualityProfilesMonitorModeHttpHttps**](SdwanSaasQualityProfilesMonitorModeHttpHttps.md) |  | [optional] 
**static_ip** | [**SdwanSaasQualityProfilesMonitorModeStaticIp**](SdwanSaasQualityProfilesMonitorModeStaticIp.md) |  | [optional] 

## Example

```python
from scm_network_services.models.sdwan_saas_quality_profiles_monitor_mode import SdwanSaasQualityProfilesMonitorMode

# TODO update the JSON string below
json = "{}"
# create an instance of SdwanSaasQualityProfilesMonitorMode from a JSON string
sdwan_saas_quality_profiles_monitor_mode_instance = SdwanSaasQualityProfilesMonitorMode.from_json(json)
# print the JSON string representation of the object
print(SdwanSaasQualityProfilesMonitorMode.to_json())

# convert the object into a dict
sdwan_saas_quality_profiles_monitor_mode_dict = sdwan_saas_quality_profiles_monitor_mode_instance.to_dict()
# create an instance of SdwanSaasQualityProfilesMonitorMode from a dict
sdwan_saas_quality_profiles_monitor_mode_from_dict = SdwanSaasQualityProfilesMonitorMode.from_dict(sdwan_saas_quality_profiles_monitor_mode_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


