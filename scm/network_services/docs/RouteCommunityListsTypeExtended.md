# RouteCommunityListsTypeExtended


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**extended_entry** | [**List[RouteCommunityListsTypeExtendedExtendedEntryInner]**](RouteCommunityListsTypeExtendedExtendedEntryInner.md) | Extended community lists | [optional] 

## Example

```python
from scm_network_services.models.route_community_lists_type_extended import RouteCommunityListsTypeExtended

# TODO update the JSON string below
json = "{}"
# create an instance of RouteCommunityListsTypeExtended from a JSON string
route_community_lists_type_extended_instance = RouteCommunityListsTypeExtended.from_json(json)
# print the JSON string representation of the object
print(RouteCommunityListsTypeExtended.to_json())

# convert the object into a dict
route_community_lists_type_extended_dict = route_community_lists_type_extended_instance.to_dict()
# create an instance of RouteCommunityListsTypeExtended from a dict
route_community_lists_type_extended_from_dict = RouteCommunityListsTypeExtended.from_dict(route_community_lists_type_extended_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


