# RouteCommunityListsTypeRegular


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**regular_entry** | [**List[RouteCommunityListsTypeRegularRegularEntryInner]**](RouteCommunityListsTypeRegularRegularEntryInner.md) | Regular community lists | [optional] 

## Example

```python
from scm_network_services.models.route_community_lists_type_regular import RouteCommunityListsTypeRegular

# TODO update the JSON string below
json = "{}"
# create an instance of RouteCommunityListsTypeRegular from a JSON string
route_community_lists_type_regular_instance = RouteCommunityListsTypeRegular.from_json(json)
# print the JSON string representation of the object
print(RouteCommunityListsTypeRegular.to_json())

# convert the object into a dict
route_community_lists_type_regular_dict = route_community_lists_type_regular_instance.to_dict()
# create an instance of RouteCommunityListsTypeRegular from a dict
route_community_lists_type_regular_from_dict = RouteCommunityListsTypeRegular.from_dict(route_community_lists_type_regular_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


