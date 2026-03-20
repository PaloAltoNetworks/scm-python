# RoutePathAccessListsListResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[RoutePathAccessLists]**](RoutePathAccessLists.md) |  | 
**limit** | **int** | The maximum number of results per page | [default to 200]
**offset** | **int** | The offset into the list of results returned | [default to 0]
**total** | **int** | The total count of results | 

## Example

```python
from scm.network_services.models.route_path_access_lists_list_response import RoutePathAccessListsListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of RoutePathAccessListsListResponse from a JSON string
route_path_access_lists_list_response_instance = RoutePathAccessListsListResponse.from_json(json)
# print the JSON string representation of the object
print(RoutePathAccessListsListResponse.to_json())

# convert the object into a dict
route_path_access_lists_list_response_dict = route_path_access_lists_list_response_instance.to_dict()
# create an instance of RoutePathAccessListsListResponse from a dict
route_path_access_lists_list_response_from_dict = RoutePathAccessListsListResponse.from_dict(route_path_access_lists_list_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


