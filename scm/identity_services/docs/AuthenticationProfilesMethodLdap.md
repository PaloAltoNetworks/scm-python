# AuthenticationProfilesMethodLdap


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**login_attribute** | **str** |  | [optional] 
**passwd_exp_days** | **int** |  | [optional] 
**server_profile** | **str** |  | [optional] 

## Example

```python
from scm.identity_services.models.authentication_profiles_method_ldap import AuthenticationProfilesMethodLdap

# TODO update the JSON string below
json = "{}"
# create an instance of AuthenticationProfilesMethodLdap from a JSON string
authentication_profiles_method_ldap_instance = AuthenticationProfilesMethodLdap.from_json(json)
# print the JSON string representation of the object
print(AuthenticationProfilesMethodLdap.to_json())

# convert the object into a dict
authentication_profiles_method_ldap_dict = authentication_profiles_method_ldap_instance.to_dict()
# create an instance of AuthenticationProfilesMethodLdap from a dict
authentication_profiles_method_ldap_from_dict = AuthenticationProfilesMethodLdap.from_dict(authentication_profiles_method_ldap_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


