# RoutePrefixListsListResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[RoutePrefixLists]**](RoutePrefixLists.md) |  | 
**limit** | **int** | The maximum number of results per page | [default to 200]
**offset** | **int** | The offset into the list of results returned | [default to 0]
**total** | **int** | The total count of results | 

## Example

```python
from scm.network_services.models.route_prefix_lists_list_response import RoutePrefixListsListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of RoutePrefixListsListResponse from a JSON string
route_prefix_lists_list_response_instance = RoutePrefixListsListResponse.from_json(json)
# print the JSON string representation of the object
print(RoutePrefixListsListResponse.to_json())

# convert the object into a dict
route_prefix_lists_list_response_dict = route_prefix_lists_list_response_instance.to_dict()
# create an instance of RoutePrefixListsListResponse from a dict
route_prefix_lists_list_response_from_dict = RoutePrefixListsListResponse.from_dict(route_prefix_lists_list_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


