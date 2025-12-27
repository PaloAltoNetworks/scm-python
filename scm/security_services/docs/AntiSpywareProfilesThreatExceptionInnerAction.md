# AntiSpywareProfilesThreatExceptionInnerAction

anti spyware profiles threat exception default action

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**alert** | **object** |  | [optional] 
**allow** | **object** |  | [optional] 
**block_ip** | [**AntiSpywareProfilesThreatExceptionInnerActionBlockIp**](AntiSpywareProfilesThreatExceptionInnerActionBlockIp.md) |  | [optional] 
**default** | **object** |  | [optional] 
**drop** | **object** |  | [optional] 
**reset_both** | **object** |  | [optional] 
**reset_client** | **object** |  | [optional] 
**reset_server** | **object** |  | [optional] 

## Example

```python
from scm_security_services.models.anti_spyware_profiles_threat_exception_inner_action import AntiSpywareProfilesThreatExceptionInnerAction

# TODO update the JSON string below
json = "{}"
# create an instance of AntiSpywareProfilesThreatExceptionInnerAction from a JSON string
anti_spyware_profiles_threat_exception_inner_action_instance = AntiSpywareProfilesThreatExceptionInnerAction.from_json(json)
# print the JSON string representation of the object
print(AntiSpywareProfilesThreatExceptionInnerAction.to_json())

# convert the object into a dict
anti_spyware_profiles_threat_exception_inner_action_dict = anti_spyware_profiles_threat_exception_inner_action_instance.to_dict()
# create an instance of AntiSpywareProfilesThreatExceptionInnerAction from a dict
anti_spyware_profiles_threat_exception_inner_action_from_dict = AntiSpywareProfilesThreatExceptionInnerAction.from_dict(anti_spyware_profiles_threat_exception_inner_action_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


