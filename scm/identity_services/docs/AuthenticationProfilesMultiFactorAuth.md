# AuthenticationProfilesMultiFactorAuth


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**factors** | **List[str]** |  | [optional] 
**mfa_enable** | **bool** |  | [optional] 

## Example

```python
from scm.identity_services.models.authentication_profiles_multi_factor_auth import AuthenticationProfilesMultiFactorAuth

# TODO update the JSON string below
json = "{}"
# create an instance of AuthenticationProfilesMultiFactorAuth from a JSON string
authentication_profiles_multi_factor_auth_instance = AuthenticationProfilesMultiFactorAuth.from_json(json)
# print the JSON string representation of the object
print(AuthenticationProfilesMultiFactorAuth.to_json())

# convert the object into a dict
authentication_profiles_multi_factor_auth_dict = authentication_profiles_multi_factor_auth_instance.to_dict()
# create an instance of AuthenticationProfilesMultiFactorAuth from a dict
authentication_profiles_multi_factor_auth_from_dict = AuthenticationProfilesMultiFactorAuth.from_dict(authentication_profiles_multi_factor_auth_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


