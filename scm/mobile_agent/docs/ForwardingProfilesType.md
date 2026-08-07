# ForwardingProfilesType

Forwarding profile type configuration (PAC file, GlobalProtect proxy, or ZTNA agent)

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**global_protect_proxy** | [**ForwardingProfileGlobalProtectProxyGlobalProtectProxy**](ForwardingProfileGlobalProtectProxyGlobalProtectProxy.md) |  | [optional] 
**pac_file** | [**ForwardingProfilePacFilePacFile**](ForwardingProfilePacFilePacFile.md) |  | [optional] 
**ztna_agent** | [**ForwardingProfileZtnaAgentZtnaAgent**](ForwardingProfileZtnaAgentZtnaAgent.md) |  | [optional] 

## Example

```python
from scm.mobile_agent.models.forwarding_profiles_type import ForwardingProfilesType

# TODO update the JSON string below
json = "{}"
# create an instance of ForwardingProfilesType from a JSON string
forwarding_profiles_type_instance = ForwardingProfilesType.from_json(json)
# print the JSON string representation of the object
print(ForwardingProfilesType.to_json())

# convert the object into a dict
forwarding_profiles_type_dict = forwarding_profiles_type_instance.to_dict()
# create an instance of ForwardingProfilesType from a dict
forwarding_profiles_type_from_dict = ForwardingProfilesType.from_dict(forwarding_profiles_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


