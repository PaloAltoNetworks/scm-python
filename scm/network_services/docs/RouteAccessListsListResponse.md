# RouteAccessListsListResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[RouteAccessLists]**](RouteAccessLists.md) |  | 
**limit** | **int** | The maximum number of results per page | [default to 200]
**offset** | **int** | The offset into the list of results returned | [default to 0]
**total** | **int** | The total count of results | 

## Example

```python
from scm.network_services.models.route_access_lists_list_response import RouteAccessListsListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of RouteAccessListsListResponse from a JSON string
route_access_lists_list_response_instance = RouteAccessListsListResponse.from_json(json)
# print the JSON string representation of the object
print(RouteAccessListsListResponse.to_json())

# convert the object into a dict
route_access_lists_list_response_dict = route_access_lists_list_response_instance.to_dict()
# create an instance of RouteAccessListsListResponse from a dict
route_access_lists_list_response_from_dict = RouteAccessListsListResponse.from_dict(route_access_lists_list_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


