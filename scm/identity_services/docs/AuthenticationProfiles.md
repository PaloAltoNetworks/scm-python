# AuthenticationProfiles


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allow_list** | **List[str]** | The allow_list of the authentication profile | [optional] [default to ["all"]]
**device** | **str** | The device in which the resource is defined | [optional] 
**folder** | **str** | The folder in which the resource is defined | [optional] 
**id** | **str** | The UUID of the authentication profile | [optional] [readonly] 
**lockout** | [**AuthenticationProfilesLockout**](AuthenticationProfilesLockout.md) |  | [optional] 
**method** | [**AuthenticationProfilesMethod**](AuthenticationProfilesMethod.md) |  | [optional] 
**multi_factor_auth** | [**AuthenticationProfilesMultiFactorAuth**](AuthenticationProfilesMultiFactorAuth.md) |  | [optional] 
**name** | **str** | The name of the authentication profile | 
**single_sign_on** | [**AuthenticationProfilesSingleSignOn**](AuthenticationProfilesSingleSignOn.md) |  | [optional] 
**snippet** | **str** | The snippet in which the resource is defined | [optional] 
**user_domain** | **str** |  | [optional] 
**username_modifier** | **str** |  | [optional] 

## Example

```python
from scm_identity_services.models.authentication_profiles import AuthenticationProfiles

# TODO update the JSON string below
json = "{}"
# create an instance of AuthenticationProfiles from a JSON string
authentication_profiles_instance = AuthenticationProfiles.from_json(json)
# print the JSON string representation of the object
print(AuthenticationProfiles.to_json())

# convert the object into a dict
authentication_profiles_dict = authentication_profiles_instance.to_dict()
# create an instance of AuthenticationProfiles from a dict
authentication_profiles_from_dict = AuthenticationProfiles.from_dict(authentication_profiles_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


