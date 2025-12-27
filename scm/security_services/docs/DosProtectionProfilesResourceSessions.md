# DosProtectionProfilesResourceSessions


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | **bool** |  | [optional] [default to False]
**max_concurrent_limit** | **int** |  | [optional] [default to 32768]

## Example

```python
from scm_security_services.models.dos_protection_profiles_resource_sessions import DosProtectionProfilesResourceSessions

# TODO update the JSON string below
json = "{}"
# create an instance of DosProtectionProfilesResourceSessions from a JSON string
dos_protection_profiles_resource_sessions_instance = DosProtectionProfilesResourceSessions.from_json(json)
# print the JSON string representation of the object
print(DosProtectionProfilesResourceSessions.to_json())

# convert the object into a dict
dos_protection_profiles_resource_sessions_dict = dos_protection_profiles_resource_sessions_instance.to_dict()
# create an instance of DosProtectionProfilesResourceSessions from a dict
dos_protection_profiles_resource_sessions_from_dict = DosProtectionProfilesResourceSessions.from_dict(dos_protection_profiles_resource_sessions_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


