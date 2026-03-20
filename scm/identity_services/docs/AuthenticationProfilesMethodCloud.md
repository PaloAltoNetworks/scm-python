# AuthenticationProfilesMethodCloud


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**profile_name** | **str** | The tenant profile name | [optional] 

## Example

```python
from scm.identity_services.models.authentication_profiles_method_cloud import AuthenticationProfilesMethodCloud

# TODO update the JSON string below
json = "{}"
# create an instance of AuthenticationProfilesMethodCloud from a JSON string
authentication_profiles_method_cloud_instance = AuthenticationProfilesMethodCloud.from_json(json)
# print the JSON string representation of the object
print(AuthenticationProfilesMethodCloud.to_json())

# convert the object into a dict
authentication_profiles_method_cloud_dict = authentication_profiles_method_cloud_instance.to_dict()
# create an instance of AuthenticationProfilesMethodCloud from a dict
authentication_profiles_method_cloud_from_dict = AuthenticationProfilesMethodCloud.from_dict(authentication_profiles_method_cloud_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


