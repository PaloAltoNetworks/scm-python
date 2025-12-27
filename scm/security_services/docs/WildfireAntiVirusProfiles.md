# WildfireAntiVirusProfiles


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** |  | [optional] 
**device** | **str** | The device in which the resource is defined | [optional] 
**folder** | **str** | The folder in which the resource is defined | [optional] 
**id** | **str** | UUID of the resource | [optional] [readonly] 
**mlav_exception** | [**List[WildfireAntiVirusProfilesMlavExceptionInner]**](WildfireAntiVirusProfilesMlavExceptionInner.md) |  | [optional] 
**name** | **str** |  | 
**packet_capture** | **bool** |  | [optional] 
**rules** | [**List[WildfireAntiVirusProfilesRulesInner]**](WildfireAntiVirusProfilesRulesInner.md) |  | [optional] 
**snippet** | **str** | The snippet in which the resource is defined | [optional] 
**threat_exception** | [**List[WildfireAntiVirusProfilesThreatExceptionInner]**](WildfireAntiVirusProfilesThreatExceptionInner.md) |  | [optional] 

## Example

```python
from scm.security_services.models.wildfire_anti_virus_profiles import WildfireAntiVirusProfiles

# TODO update the JSON string below
json = "{}"
# create an instance of WildfireAntiVirusProfiles from a JSON string
wildfire_anti_virus_profiles_instance = WildfireAntiVirusProfiles.from_json(json)
# print the JSON string representation of the object
print(WildfireAntiVirusProfiles.to_json())

# convert the object into a dict
wildfire_anti_virus_profiles_dict = wildfire_anti_virus_profiles_instance.to_dict()
# create an instance of WildfireAntiVirusProfiles from a dict
wildfire_anti_virus_profiles_from_dict = WildfireAntiVirusProfiles.from_dict(wildfire_anti_virus_profiles_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


