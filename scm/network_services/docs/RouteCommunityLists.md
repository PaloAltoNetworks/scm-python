# RouteCommunityLists


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | Description | [optional] 
**device** | **str** | The device in which the resource is defined | [optional] 
**folder** | **str** | The folder in which the resource is defined | [optional] 
**id** | **str** | UUID of the resource | [optional] [readonly] 
**name** | **str** | Route community list name | 
**snippet** | **str** | The snippet in which the resource is defined | [optional] 
**type** | [**RouteCommunityListsType**](RouteCommunityListsType.md) |  | [optional] 

## Example

```python
from scm.network_services.models.route_community_lists import RouteCommunityLists

# TODO update the JSON string below
json = "{}"
# create an instance of RouteCommunityLists from a JSON string
route_community_lists_instance = RouteCommunityLists.from_json(json)
# print the JSON string representation of the object
print(RouteCommunityLists.to_json())

# convert the object into a dict
route_community_lists_dict = route_community_lists_instance.to_dict()
# create an instance of RouteCommunityLists from a dict
route_community_lists_from_dict = RouteCommunityLists.from_dict(route_community_lists_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


