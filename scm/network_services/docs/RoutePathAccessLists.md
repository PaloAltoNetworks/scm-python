# RoutePathAccessLists


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**aspath_entry** | [**List[RoutePathAccessListsAspathEntryInner]**](RoutePathAccessListsAspathEntryInner.md) | AS paths | [optional] 
**description** | **str** | Description | [optional] 
**device** | **str** | The device in which the resource is defined | [optional] 
**folder** | **str** | The folder in which the resource is defined | [optional] 
**id** | **str** | UUID of the resource | [optional] [readonly] 
**name** | **str** | AS path access list name | 
**snippet** | **str** | The snippet in which the resource is defined | [optional] 

## Example

```python
from scm_network_services.models.route_path_access_lists import RoutePathAccessLists

# TODO update the JSON string below
json = "{}"
# create an instance of RoutePathAccessLists from a JSON string
route_path_access_lists_instance = RoutePathAccessLists.from_json(json)
# print the JSON string representation of the object
print(RoutePathAccessLists.to_json())

# convert the object into a dict
route_path_access_lists_dict = route_path_access_lists_instance.to_dict()
# create an instance of RoutePathAccessLists from a dict
route_path_access_lists_from_dict = RoutePathAccessLists.from_dict(route_path_access_lists_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


