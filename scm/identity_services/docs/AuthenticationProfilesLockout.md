# AuthenticationProfilesLockout

Lockout object of the authentication profile

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**failed_attempts** | **int** | Lockout object - failed_attempts of authentication profile | [optional] 
**lockout_time** | **int** | Lockout object - lockout-time of authentication profile | [optional] 

## Example

```python
from scm_identity_services.models.authentication_profiles_lockout import AuthenticationProfilesLockout

# TODO update the JSON string below
json = "{}"
# create an instance of AuthenticationProfilesLockout from a JSON string
authentication_profiles_lockout_instance = AuthenticationProfilesLockout.from_json(json)
# print the JSON string representation of the object
print(AuthenticationProfilesLockout.to_json())

# convert the object into a dict
authentication_profiles_lockout_dict = authentication_profiles_lockout_instance.to_dict()
# create an instance of AuthenticationProfilesLockout from a dict
authentication_profiles_lockout_from_dict = AuthenticationProfilesLockout.from_dict(authentication_profiles_lockout_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


