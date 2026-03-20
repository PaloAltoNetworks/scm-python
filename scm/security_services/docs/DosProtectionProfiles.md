# DosProtectionProfiles


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | Description | [optional] 
**device** | **str** | The device in which the resource is defined | [optional] 
**flood** | [**DosProtectionProfilesFlood**](DosProtectionProfilesFlood.md) |  | [optional] 
**folder** | **str** | The folder in which the resource is defined | [optional] 
**id** | **str** | The UUID of the DNS security profile | [optional] [readonly] 
**name** | **str** | Profile name | 
**resource** | [**DosProtectionProfilesResource**](DosProtectionProfilesResource.md) |  | [optional] 
**snippet** | **str** | The snippet in which the resource is defined | [optional] 
**type** | **str** | Type | 

## Example

```python
from scm.security_services.models.dos_protection_profiles import DosProtectionProfiles

# TODO update the JSON string below
json = "{}"
# create an instance of DosProtectionProfiles from a JSON string
dos_protection_profiles_instance = DosProtectionProfiles.from_json(json)
# print the JSON string representation of the object
print(DosProtectionProfiles.to_json())

# convert the object into a dict
dos_protection_profiles_dict = dos_protection_profiles_instance.to_dict()
# create an instance of DosProtectionProfiles from a dict
dos_protection_profiles_from_dict = DosProtectionProfiles.from_dict(dos_protection_profiles_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


