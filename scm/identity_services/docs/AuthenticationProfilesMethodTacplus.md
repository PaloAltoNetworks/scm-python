# AuthenticationProfilesMethodTacplus


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**checkgroup** | **bool** | method tacplus object check group of authentication profile | [optional] 
**server_profile** | **str** | method tacplus object check group of authentication profile | [optional] 

## Example

```python
from scm.identity_services.models.authentication_profiles_method_tacplus import AuthenticationProfilesMethodTacplus

# TODO update the JSON string below
json = "{}"
# create an instance of AuthenticationProfilesMethodTacplus from a JSON string
authentication_profiles_method_tacplus_instance = AuthenticationProfilesMethodTacplus.from_json(json)
# print the JSON string representation of the object
print(AuthenticationProfilesMethodTacplus.to_json())

# convert the object into a dict
authentication_profiles_method_tacplus_dict = authentication_profiles_method_tacplus_instance.to_dict()
# create an instance of AuthenticationProfilesMethodTacplus from a dict
authentication_profiles_method_tacplus_from_dict = AuthenticationProfilesMethodTacplus.from_dict(authentication_profiles_method_tacplus_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


