# RoutePathAccessListsAspathEntryInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **str** | Action | [optional] 
**aspath_regex** | **str** | AS path regular expression | [optional] 
**name** | **int** | Sequence number | [optional] 

## Example

```python
from scm_network_services.models.route_path_access_lists_aspath_entry_inner import RoutePathAccessListsAspathEntryInner

# TODO update the JSON string below
json = "{}"
# create an instance of RoutePathAccessListsAspathEntryInner from a JSON string
route_path_access_lists_aspath_entry_inner_instance = RoutePathAccessListsAspathEntryInner.from_json(json)
# print the JSON string representation of the object
print(RoutePathAccessListsAspathEntryInner.to_json())

# convert the object into a dict
route_path_access_lists_aspath_entry_inner_dict = route_path_access_lists_aspath_entry_inner_instance.to_dict()
# create an instance of RoutePathAccessListsAspathEntryInner from a dict
route_path_access_lists_aspath_entry_inner_from_dict = RoutePathAccessListsAspathEntryInner.from_dict(route_path_access_lists_aspath_entry_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


