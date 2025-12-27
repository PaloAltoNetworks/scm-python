# ProfileGroupsListResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[ProfileGroups]**](ProfileGroups.md) |  | 
**limit** | **int** | The maximum number of results per page | [default to 200]
**offset** | **int** | The offset into the list of results returned | [default to 0]
**total** | **int** | The total count of results | 

## Example

```python
from scm.security_services.models.profile_groups_list_response import ProfileGroupsListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ProfileGroupsListResponse from a JSON string
profile_groups_list_response_instance = ProfileGroupsListResponse.from_json(json)
# print the JSON string representation of the object
print(ProfileGroupsListResponse.to_json())

# convert the object into a dict
profile_groups_list_response_dict = profile_groups_list_response_instance.to_dict()
# create an instance of ProfileGroupsListResponse from a dict
profile_groups_list_response_from_dict = ProfileGroupsListResponse.from_dict(profile_groups_list_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


