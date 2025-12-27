# AuthenticationProfilesMethodSamlIdp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attribute_name_usergroup** | **str** |  | [optional] 
**attribute_name_username** | **str** |  | [optional] 
**certificate_profile** | **str** | method object saml idp certificate profile of authentication profile | [optional] 
**enable_single_logout** | **bool** |  | [optional] 
**request_signing_certificate** | **str** |  | [optional] 
**server_profile** | **str** | method object saml idp server profile of authentication profile | [optional] 

## Example

```python
from scm_identity_services.models.authentication_profiles_method_saml_idp import AuthenticationProfilesMethodSamlIdp

# TODO update the JSON string below
json = "{}"
# create an instance of AuthenticationProfilesMethodSamlIdp from a JSON string
authentication_profiles_method_saml_idp_instance = AuthenticationProfilesMethodSamlIdp.from_json(json)
# print the JSON string representation of the object
print(AuthenticationProfilesMethodSamlIdp.to_json())

# convert the object into a dict
authentication_profiles_method_saml_idp_dict = authentication_profiles_method_saml_idp_instance.to_dict()
# create an instance of AuthenticationProfilesMethodSamlIdp from a dict
authentication_profiles_method_saml_idp_from_dict = AuthenticationProfilesMethodSamlIdp.from_dict(authentication_profiles_method_saml_idp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


