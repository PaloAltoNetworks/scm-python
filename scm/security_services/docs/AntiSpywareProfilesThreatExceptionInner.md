# AntiSpywareProfilesThreatExceptionInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | [**AntiSpywareProfilesThreatExceptionInnerAction**](AntiSpywareProfilesThreatExceptionInnerAction.md) |  | [optional] 
**exempt_ip** | [**List[AntiSpywareProfilesThreatExceptionInnerExemptIpInner]**](AntiSpywareProfilesThreatExceptionInnerExemptIpInner.md) |  | [optional] 
**name** | **str** |  | [optional] 
**notes** | **str** |  | [optional] 
**packet_capture** | **str** |  | [optional] 

## Example

```python
from scm_security_services.models.anti_spyware_profiles_threat_exception_inner import AntiSpywareProfilesThreatExceptionInner

# TODO update the JSON string below
json = "{}"
# create an instance of AntiSpywareProfilesThreatExceptionInner from a JSON string
anti_spyware_profiles_threat_exception_inner_instance = AntiSpywareProfilesThreatExceptionInner.from_json(json)
# print the JSON string representation of the object
print(AntiSpywareProfilesThreatExceptionInner.to_json())

# convert the object into a dict
anti_spyware_profiles_threat_exception_inner_dict = anti_spyware_profiles_threat_exception_inner_instance.to_dict()
# create an instance of AntiSpywareProfilesThreatExceptionInner from a dict
anti_spyware_profiles_threat_exception_inner_from_dict = AntiSpywareProfilesThreatExceptionInner.from_dict(anti_spyware_profiles_threat_exception_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


