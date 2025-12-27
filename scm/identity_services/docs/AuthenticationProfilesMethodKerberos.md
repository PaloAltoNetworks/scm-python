# AuthenticationProfilesMethodKerberos


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**realm** | **str** | method kerberos object realm of authentication profile | [optional] 
**server_profile** | **str** | method kerberos object server profile of authentication profile | [optional] 

## Example

```python
from scm_identity_services.models.authentication_profiles_method_kerberos import AuthenticationProfilesMethodKerberos

# TODO update the JSON string below
json = "{}"
# create an instance of AuthenticationProfilesMethodKerberos from a JSON string
authentication_profiles_method_kerberos_instance = AuthenticationProfilesMethodKerberos.from_json(json)
# print the JSON string representation of the object
print(AuthenticationProfilesMethodKerberos.to_json())

# convert the object into a dict
authentication_profiles_method_kerberos_dict = authentication_profiles_method_kerberos_instance.to_dict()
# create an instance of AuthenticationProfilesMethodKerberos from a dict
authentication_profiles_method_kerberos_from_dict = AuthenticationProfilesMethodKerberos.from_dict(authentication_profiles_method_kerberos_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


