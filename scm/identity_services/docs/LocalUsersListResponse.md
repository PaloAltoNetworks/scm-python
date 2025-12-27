# LocalUsersListResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[LocalUsers]**](LocalUsers.md) |  | 
**limit** | **int** | The maximum number of results per page | [default to 200]
**offset** | **int** | The offset into the list of results returned | [default to 0]
**total** | **int** | The total count of results | 

## Example

```python
from scm.identity_services.models.local_users_list_response import LocalUsersListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of LocalUsersListResponse from a JSON string
local_users_list_response_instance = LocalUsersListResponse.from_json(json)
# print the JSON string representation of the object
print(LocalUsersListResponse.to_json())

# convert the object into a dict
local_users_list_response_dict = local_users_list_response_instance.to_dict()
# create an instance of LocalUsersListResponse from a dict
local_users_list_response_from_dict = LocalUsersListResponse.from_dict(local_users_list_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


