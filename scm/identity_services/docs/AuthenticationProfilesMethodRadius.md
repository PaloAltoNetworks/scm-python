# AuthenticationProfilesMethodRadius


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**checkgroup** | **bool** | method radius object check group of authentication profile | [optional] 
**server_profile** | **str** | method radius object server profile of authentication profile | [optional] 

## Example

```python
from scm_identity_services.models.authentication_profiles_method_radius import AuthenticationProfilesMethodRadius

# TODO update the JSON string below
json = "{}"
# create an instance of AuthenticationProfilesMethodRadius from a JSON string
authentication_profiles_method_radius_instance = AuthenticationProfilesMethodRadius.from_json(json)
# print the JSON string representation of the object
print(AuthenticationProfilesMethodRadius.to_json())

# convert the object into a dict
authentication_profiles_method_radius_dict = authentication_profiles_method_radius_instance.to_dict()
# create an instance of AuthenticationProfilesMethodRadius from a dict
authentication_profiles_method_radius_from_dict = AuthenticationProfilesMethodRadius.from_dict(authentication_profiles_method_radius_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


