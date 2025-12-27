# AntiSpywareProfiles


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cloud_inline_analysis** | **bool** |  | [optional] [default to False]
**description** | **str** |  | [optional] 
**device** | **str** | The device in which the resource is defined | [optional] 
**folder** | **str** | The folder in which the resource is defined | [optional] 
**id** | **str** | The UUID of the anti-spyware profile | [readonly] 
**inline_exception_edl_url** | **List[str]** |  | [optional] 
**inline_exception_ip_address** | **List[str]** |  | [optional] 
**mica_engine_spyware_enabled** | [**List[AntiSpywareProfilesMicaEngineSpywareEnabledInner]**](AntiSpywareProfilesMicaEngineSpywareEnabledInner.md) |  | [optional] 
**name** | **str** | The name of the anti-spyware profile | 
**rules** | [**List[AntiSpywareProfilesRulesInner]**](AntiSpywareProfilesRulesInner.md) |  | [optional] 
**snippet** | **str** | The snippet in which the resource is defined | [optional] 
**threat_exception** | [**List[AntiSpywareProfilesThreatExceptionInner]**](AntiSpywareProfilesThreatExceptionInner.md) |  | [optional] 

## Example

```python
from scm.security_services.models.anti_spyware_profiles import AntiSpywareProfiles

# TODO update the JSON string below
json = "{}"
# create an instance of AntiSpywareProfiles from a JSON string
anti_spyware_profiles_instance = AntiSpywareProfiles.from_json(json)
# print the JSON string representation of the object
print(AntiSpywareProfiles.to_json())

# convert the object into a dict
anti_spyware_profiles_dict = anti_spyware_profiles_instance.to_dict()
# create an instance of AntiSpywareProfiles from a dict
anti_spyware_profiles_from_dict = AntiSpywareProfiles.from_dict(anti_spyware_profiles_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


