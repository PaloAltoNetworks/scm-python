# RouteAccessLists


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | Description | [optional] 
**device** | **str** | The device in which the resource is defined | [optional] 
**folder** | **str** | The folder in which the resource is defined | [optional] 
**id** | **str** | UUID of the resource | [optional] [readonly] 
**name** | **str** | Route access list name | 
**snippet** | **str** | The snippet in which the resource is defined | [optional] 
**type** | [**RouteAccessListsType**](RouteAccessListsType.md) |  | [optional] 

## Example

```python
from scm.network_services.models.route_access_lists import RouteAccessLists

# TODO update the JSON string below
json = "{}"
# create an instance of RouteAccessLists from a JSON string
route_access_lists_instance = RouteAccessLists.from_json(json)
# print the JSON string representation of the object
print(RouteAccessLists.to_json())

# convert the object into a dict
route_access_lists_dict = route_access_lists_instance.to_dict()
# create an instance of RouteAccessLists from a dict
route_access_lists_from_dict = RouteAccessLists.from_dict(route_access_lists_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


