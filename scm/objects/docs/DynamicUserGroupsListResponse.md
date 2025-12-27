# DynamicUserGroupsListResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[DynamicUserGroups]**](DynamicUserGroups.md) |  | 
**limit** | **int** | The maximum number of results per page | [default to 200]
**offset** | **int** | The offset into the list of results returned | [default to 0]
**total** | **int** | The total count of results | 

## Example

```python
from scm_objects.models.dynamic_user_groups_list_response import DynamicUserGroupsListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DynamicUserGroupsListResponse from a JSON string
dynamic_user_groups_list_response_instance = DynamicUserGroupsListResponse.from_json(json)
# print the JSON string representation of the object
print(DynamicUserGroupsListResponse.to_json())

# convert the object into a dict
dynamic_user_groups_list_response_dict = dynamic_user_groups_list_response_instance.to_dict()
# create an instance of DynamicUserGroupsListResponse from a dict
dynamic_user_groups_list_response_from_dict = DynamicUserGroupsListResponse.from_dict(dynamic_user_groups_list_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


