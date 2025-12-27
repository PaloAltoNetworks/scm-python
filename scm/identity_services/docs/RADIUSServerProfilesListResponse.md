# RADIUSServerProfilesListResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[RadiusServerProfiles]**](RadiusServerProfiles.md) |  | 
**limit** | **int** | The maximum number of results per page | [default to 200]
**offset** | **int** | The offset into the list of results returned | [default to 0]
**total** | **int** | The total count of results | 

## Example

```python
from scm.identity_services.models.radius_server_profiles_list_response import RADIUSServerProfilesListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of RADIUSServerProfilesListResponse from a JSON string
radius_server_profiles_list_response_instance = RADIUSServerProfilesListResponse.from_json(json)
# print the JSON string representation of the object
print(RADIUSServerProfilesListResponse.to_json())

# convert the object into a dict
radius_server_profiles_list_response_dict = radius_server_profiles_list_response_instance.to_dict()
# create an instance of RADIUSServerProfilesListResponse from a dict
radius_server_profiles_list_response_from_dict = RADIUSServerProfilesListResponse.from_dict(radius_server_profiles_list_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


