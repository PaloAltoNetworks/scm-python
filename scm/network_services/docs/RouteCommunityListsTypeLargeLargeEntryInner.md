# RouteCommunityListsTypeLargeLargeEntryInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **str** | Action | [optional] 
**lc_regex** | **List[str]** | Large community regular expression | [optional] 
**name** | **int** | Sequence number | [optional] 

## Example

```python
from scm.network_services.models.route_community_lists_type_large_large_entry_inner import RouteCommunityListsTypeLargeLargeEntryInner

# TODO update the JSON string below
json = "{}"
# create an instance of RouteCommunityListsTypeLargeLargeEntryInner from a JSON string
route_community_lists_type_large_large_entry_inner_instance = RouteCommunityListsTypeLargeLargeEntryInner.from_json(json)
# print the JSON string representation of the object
print(RouteCommunityListsTypeLargeLargeEntryInner.to_json())

# convert the object into a dict
route_community_lists_type_large_large_entry_inner_dict = route_community_lists_type_large_large_entry_inner_instance.to_dict()
# create an instance of RouteCommunityListsTypeLargeLargeEntryInner from a dict
route_community_lists_type_large_large_entry_inner_from_dict = RouteCommunityListsTypeLargeLargeEntryInner.from_dict(route_community_lists_type_large_large_entry_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


