# DosProtectionProfilesResource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sessions** | [**DosProtectionProfilesResourceSessions**](DosProtectionProfilesResourceSessions.md) |  | [optional] 

## Example

```python
from scm.security_services.models.dos_protection_profiles_resource import DosProtectionProfilesResource

# TODO update the JSON string below
json = "{}"
# create an instance of DosProtectionProfilesResource from a JSON string
dos_protection_profiles_resource_instance = DosProtectionProfilesResource.from_json(json)
# print the JSON string representation of the object
print(DosProtectionProfilesResource.to_json())

# convert the object into a dict
dos_protection_profiles_resource_dict = dos_protection_profiles_resource_instance.to_dict()
# create an instance of DosProtectionProfilesResource from a dict
dos_protection_profiles_resource_from_dict = DosProtectionProfilesResource.from_dict(dos_protection_profiles_resource_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


