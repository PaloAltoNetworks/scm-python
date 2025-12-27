# UrlAccessProfilesCredentialEnforcementMode


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**disabled** | **object** |  | [optional] 
**domain_credentials** | **object** |  | [optional] 
**group_mapping** | **str** |  | [optional] 
**ip_user** | **object** |  | [optional] 

## Example

```python
from scm.security_services.models.url_access_profiles_credential_enforcement_mode import UrlAccessProfilesCredentialEnforcementMode

# TODO update the JSON string below
json = "{}"
# create an instance of UrlAccessProfilesCredentialEnforcementMode from a JSON string
url_access_profiles_credential_enforcement_mode_instance = UrlAccessProfilesCredentialEnforcementMode.from_json(json)
# print the JSON string representation of the object
print(UrlAccessProfilesCredentialEnforcementMode.to_json())

# convert the object into a dict
url_access_profiles_credential_enforcement_mode_dict = url_access_profiles_credential_enforcement_mode_instance.to_dict()
# create an instance of UrlAccessProfilesCredentialEnforcementMode from a dict
url_access_profiles_credential_enforcement_mode_from_dict = UrlAccessProfilesCredentialEnforcementMode.from_dict(url_access_profiles_credential_enforcement_mode_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


