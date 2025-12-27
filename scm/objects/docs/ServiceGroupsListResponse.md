# ServiceGroupsListResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[ServiceGroups]**](ServiceGroups.md) |  | 
**limit** | **int** | The maximum number of results per page | [default to 200]
**offset** | **int** | The offset into the list of results returned | [default to 0]
**total** | **int** | The total count of results | 

## Example

```python
from scm_objects.models.service_groups_list_response import ServiceGroupsListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceGroupsListResponse from a JSON string
service_groups_list_response_instance = ServiceGroupsListResponse.from_json(json)
# print the JSON string representation of the object
print(ServiceGroupsListResponse.to_json())

# convert the object into a dict
service_groups_list_response_dict = service_groups_list_response_instance.to_dict()
# create an instance of ServiceGroupsListResponse from a dict
service_groups_list_response_from_dict = ServiceGroupsListResponse.from_dict(service_groups_list_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


