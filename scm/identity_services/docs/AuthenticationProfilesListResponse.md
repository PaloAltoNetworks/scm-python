# AuthenticationProfilesListResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[AuthenticationProfiles]**](AuthenticationProfiles.md) |  | 
**limit** | **int** | The maximum number of results per page | [default to 200]
**offset** | **int** | The offset into the list of results returned | [default to 0]
**total** | **int** | The total count of results | 

## Example

```python
from scm_identity_services.models.authentication_profiles_list_response import AuthenticationProfilesListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AuthenticationProfilesListResponse from a JSON string
authentication_profiles_list_response_instance = AuthenticationProfilesListResponse.from_json(json)
# print the JSON string representation of the object
print(AuthenticationProfilesListResponse.to_json())

# convert the object into a dict
authentication_profiles_list_response_dict = authentication_profiles_list_response_instance.to_dict()
# create an instance of AuthenticationProfilesListResponse from a dict
authentication_profiles_list_response_from_dict = AuthenticationProfilesListResponse.from_dict(authentication_profiles_list_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


