# RoutePrefixLists


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | Description | [optional] 
**device** | **str** | The device in which the resource is defined | [optional] 
**folder** | **str** | The folder in which the resource is defined | [optional] 
**id** | **str** | UUID of the resource | [optional] [readonly] 
**name** | **str** | Filter prefix list name | 
**snippet** | **str** | The snippet in which the resource is defined | [optional] 
**type** | [**RoutePrefixListsType**](RoutePrefixListsType.md) |  | [optional] 

## Example

```python
from scm_network_services.models.route_prefix_lists import RoutePrefixLists

# TODO update the JSON string below
json = "{}"
# create an instance of RoutePrefixLists from a JSON string
route_prefix_lists_instance = RoutePrefixLists.from_json(json)
# print the JSON string representation of the object
print(RoutePrefixLists.to_json())

# convert the object into a dict
route_prefix_lists_dict = route_prefix_lists_instance.to_dict()
# create an instance of RoutePrefixLists from a dict
route_prefix_lists_from_dict = RoutePrefixLists.from_dict(route_prefix_lists_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


