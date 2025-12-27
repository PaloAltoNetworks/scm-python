# AuthenticationProfilesSingleSignOn


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**kerberos_keytab** | **str** |  | [optional] 
**realm** | **str** |  | [optional] 

## Example

```python
from scm.identity_services.models.authentication_profiles_single_sign_on import AuthenticationProfilesSingleSignOn

# TODO update the JSON string below
json = "{}"
# create an instance of AuthenticationProfilesSingleSignOn from a JSON string
authentication_profiles_single_sign_on_instance = AuthenticationProfilesSingleSignOn.from_json(json)
# print the JSON string representation of the object
print(AuthenticationProfilesSingleSignOn.to_json())

# convert the object into a dict
authentication_profiles_single_sign_on_dict = authentication_profiles_single_sign_on_instance.to_dict()
# create an instance of AuthenticationProfilesSingleSignOn from a dict
authentication_profiles_single_sign_on_from_dict = AuthenticationProfilesSingleSignOn.from_dict(authentication_profiles_single_sign_on_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


