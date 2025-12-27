# ApplicationGroupsListResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[ApplicationGroups]**](ApplicationGroups.md) |  | 
**limit** | **int** | The maximum number of results per page | [default to 200]
**offset** | **int** | The offset into the list of results returned | [default to 0]
**total** | **int** | The total count of results | 

## Example

```python
from scm_objects.models.application_groups_list_response import ApplicationGroupsListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ApplicationGroupsListResponse from a JSON string
application_groups_list_response_instance = ApplicationGroupsListResponse.from_json(json)
# print the JSON string representation of the object
print(ApplicationGroupsListResponse.to_json())

# convert the object into a dict
application_groups_list_response_dict = application_groups_list_response_instance.to_dict()
# create an instance of ApplicationGroupsListResponse from a dict
application_groups_list_response_from_dict = ApplicationGroupsListResponse.from_dict(application_groups_list_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


