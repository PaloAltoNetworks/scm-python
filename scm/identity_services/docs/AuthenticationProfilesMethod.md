# AuthenticationProfilesMethod

method object of authentication profile

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cloud** | [**AuthenticationProfilesMethodCloud**](AuthenticationProfilesMethodCloud.md) |  | [optional] 
**kerberos** | [**AuthenticationProfilesMethodKerberos**](AuthenticationProfilesMethodKerberos.md) |  | [optional] 
**ldap** | [**AuthenticationProfilesMethodLdap**](AuthenticationProfilesMethodLdap.md) |  | [optional] 
**local_database** | **object** |  | [optional] 
**radius** | [**AuthenticationProfilesMethodRadius**](AuthenticationProfilesMethodRadius.md) |  | [optional] 
**saml_idp** | [**AuthenticationProfilesMethodSamlIdp**](AuthenticationProfilesMethodSamlIdp.md) |  | [optional] 
**tacplus** | [**AuthenticationProfilesMethodTacplus**](AuthenticationProfilesMethodTacplus.md) |  | [optional] 

## Example

```python
from scm_identity_services.models.authentication_profiles_method import AuthenticationProfilesMethod

# TODO update the JSON string below
json = "{}"
# create an instance of AuthenticationProfilesMethod from a JSON string
authentication_profiles_method_instance = AuthenticationProfilesMethod.from_json(json)
# print the JSON string representation of the object
print(AuthenticationProfilesMethod.to_json())

# convert the object into a dict
authentication_profiles_method_dict = authentication_profiles_method_instance.to_dict()
# create an instance of AuthenticationProfilesMethod from a dict
authentication_profiles_method_from_dict = AuthenticationProfilesMethod.from_dict(authentication_profiles_method_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


