# RouteCommunityListsTypeExtendedExtendedEntryInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **str** | Action | [optional] 
**lc_regex** | **List[str]** | Extended community regular expression | [optional] 
**name** | **int** | Sequence number | [optional] 

## Example

```python
from scm_network_services.models.route_community_lists_type_extended_extended_entry_inner import RouteCommunityListsTypeExtendedExtendedEntryInner

# TODO update the JSON string below
json = "{}"
# create an instance of RouteCommunityListsTypeExtendedExtendedEntryInner from a JSON string
route_community_lists_type_extended_extended_entry_inner_instance = RouteCommunityListsTypeExtendedExtendedEntryInner.from_json(json)
# print the JSON string representation of the object
print(RouteCommunityListsTypeExtendedExtendedEntryInner.to_json())

# convert the object into a dict
route_community_lists_type_extended_extended_entry_inner_dict = route_community_lists_type_extended_extended_entry_inner_instance.to_dict()
# create an instance of RouteCommunityListsTypeExtendedExtendedEntryInner from a dict
route_community_lists_type_extended_extended_entry_inner_from_dict = RouteCommunityListsTypeExtendedExtendedEntryInner.from_dict(route_community_lists_type_extended_extended_entry_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


