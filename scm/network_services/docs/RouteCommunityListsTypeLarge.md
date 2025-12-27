# RouteCommunityListsTypeLarge


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**large_entry** | [**List[RouteCommunityListsTypeLargeLargeEntryInner]**](RouteCommunityListsTypeLargeLargeEntryInner.md) | Large community lists | [optional] 

## Example

```python
from scm_network_services.models.route_community_lists_type_large import RouteCommunityListsTypeLarge

# TODO update the JSON string below
json = "{}"
# create an instance of RouteCommunityListsTypeLarge from a JSON string
route_community_lists_type_large_instance = RouteCommunityListsTypeLarge.from_json(json)
# print the JSON string representation of the object
print(RouteCommunityListsTypeLarge.to_json())

# convert the object into a dict
route_community_lists_type_large_dict = route_community_lists_type_large_instance.to_dict()
# create an instance of RouteCommunityListsTypeLarge from a dict
route_community_lists_type_large_from_dict = RouteCommunityListsTypeLarge.from_dict(route_community_lists_type_large_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


