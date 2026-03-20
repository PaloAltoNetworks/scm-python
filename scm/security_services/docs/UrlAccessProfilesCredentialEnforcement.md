# UrlAccessProfilesCredentialEnforcement


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**alert** | **List[str]** |  | [optional] 
**allow** | **List[str]** |  | [optional] 
**block** | **List[str]** |  | [optional] 
**var_continue** | **List[str]** |  | [optional] 
**log_severity** | **str** |  | [optional] [default to 'medium']
**mode** | [**UrlAccessProfilesCredentialEnforcementMode**](UrlAccessProfilesCredentialEnforcementMode.md) |  | [optional] 

## Example

```python
from scm.security_services.models.url_access_profiles_credential_enforcement import UrlAccessProfilesCredentialEnforcement

# TODO update the JSON string below
json = "{}"
# create an instance of UrlAccessProfilesCredentialEnforcement from a JSON string
url_access_profiles_credential_enforcement_instance = UrlAccessProfilesCredentialEnforcement.from_json(json)
# print the JSON string representation of the object
print(UrlAccessProfilesCredentialEnforcement.to_json())

# convert the object into a dict
url_access_profiles_credential_enforcement_dict = url_access_profiles_credential_enforcement_instance.to_dict()
# create an instance of UrlAccessProfilesCredentialEnforcement from a dict
url_access_profiles_credential_enforcement_from_dict = UrlAccessProfilesCredentialEnforcement.from_dict(url_access_profiles_credential_enforcement_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


