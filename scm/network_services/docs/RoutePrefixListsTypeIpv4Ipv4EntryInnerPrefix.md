# RoutePrefixListsTypeIpv4Ipv4EntryInnerPrefix


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entry** | [**RoutePrefixListsTypeIpv4Ipv4EntryInnerPrefixEntry**](RoutePrefixListsTypeIpv4Ipv4EntryInnerPrefixEntry.md) |  | [optional] 
**network** | **str** | Network | [optional] 

## Example

```python
from scm.network_services.models.route_prefix_lists_type_ipv4_ipv4_entry_inner_prefix import RoutePrefixListsTypeIpv4Ipv4EntryInnerPrefix

# TODO update the JSON string below
json = "{}"
# create an instance of RoutePrefixListsTypeIpv4Ipv4EntryInnerPrefix from a JSON string
route_prefix_lists_type_ipv4_ipv4_entry_inner_prefix_instance = RoutePrefixListsTypeIpv4Ipv4EntryInnerPrefix.from_json(json)
# print the JSON string representation of the object
print(RoutePrefixListsTypeIpv4Ipv4EntryInnerPrefix.to_json())

# convert the object into a dict
route_prefix_lists_type_ipv4_ipv4_entry_inner_prefix_dict = route_prefix_lists_type_ipv4_ipv4_entry_inner_prefix_instance.to_dict()
# create an instance of RoutePrefixListsTypeIpv4Ipv4EntryInnerPrefix from a dict
route_prefix_lists_type_ipv4_ipv4_entry_inner_prefix_from_dict = RoutePrefixListsTypeIpv4Ipv4EntryInnerPrefix.from_dict(route_prefix_lists_type_ipv4_ipv4_entry_inner_prefix_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


