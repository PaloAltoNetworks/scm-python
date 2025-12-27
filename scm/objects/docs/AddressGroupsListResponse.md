# AddressGroupsListResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[AddressGroups]**](AddressGroups.md) |  | 
**limit** | **int** | The maximum number of results per page | [default to 200]
**offset** | **int** | The offset into the list of results returned | [default to 0]
**total** | **int** | The total count of results | 

## Example

```python
from scm_objects.models.address_groups_list_response import AddressGroupsListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AddressGroupsListResponse from a JSON string
address_groups_list_response_instance = AddressGroupsListResponse.from_json(json)
# print the JSON string representation of the object
print(AddressGroupsListResponse.to_json())

# convert the object into a dict
address_groups_list_response_dict = address_groups_list_response_instance.to_dict()
# create an instance of AddressGroupsListResponse from a dict
address_groups_list_response_from_dict = AddressGroupsListResponse.from_dict(address_groups_list_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


