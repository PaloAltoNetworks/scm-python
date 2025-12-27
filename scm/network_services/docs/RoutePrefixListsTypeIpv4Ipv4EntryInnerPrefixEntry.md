# RoutePrefixListsTypeIpv4Ipv4EntryInnerPrefixEntry


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**greater_than_or_equal** | **int** | Greater than or equal to | [optional] 
**less_than_or_equal** | **int** | Less than or equal to | [optional] 
**network** | **str** | Network | [optional] 

## Example

```python
from scm_network_services.models.route_prefix_lists_type_ipv4_ipv4_entry_inner_prefix_entry import RoutePrefixListsTypeIpv4Ipv4EntryInnerPrefixEntry

# TODO update the JSON string below
json = "{}"
# create an instance of RoutePrefixListsTypeIpv4Ipv4EntryInnerPrefixEntry from a JSON string
route_prefix_lists_type_ipv4_ipv4_entry_inner_prefix_entry_instance = RoutePrefixListsTypeIpv4Ipv4EntryInnerPrefixEntry.from_json(json)
# print the JSON string representation of the object
print(RoutePrefixListsTypeIpv4Ipv4EntryInnerPrefixEntry.to_json())

# convert the object into a dict
route_prefix_lists_type_ipv4_ipv4_entry_inner_prefix_entry_dict = route_prefix_lists_type_ipv4_ipv4_entry_inner_prefix_entry_instance.to_dict()
# create an instance of RoutePrefixListsTypeIpv4Ipv4EntryInnerPrefixEntry from a dict
route_prefix_lists_type_ipv4_ipv4_entry_inner_prefix_entry_from_dict = RoutePrefixListsTypeIpv4Ipv4EntryInnerPrefixEntry.from_dict(route_prefix_lists_type_ipv4_ipv4_entry_inner_prefix_entry_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


