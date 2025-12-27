# RoutePrefixListsTypeIpv4Ipv4EntryInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **str** | Action | [optional] 
**name** | **int** | Sequence number | [optional] 
**prefix** | [**RoutePrefixListsTypeIpv4Ipv4EntryInnerPrefix**](RoutePrefixListsTypeIpv4Ipv4EntryInnerPrefix.md) |  | [optional] 

## Example

```python
from scm_network_services.models.route_prefix_lists_type_ipv4_ipv4_entry_inner import RoutePrefixListsTypeIpv4Ipv4EntryInner

# TODO update the JSON string below
json = "{}"
# create an instance of RoutePrefixListsTypeIpv4Ipv4EntryInner from a JSON string
route_prefix_lists_type_ipv4_ipv4_entry_inner_instance = RoutePrefixListsTypeIpv4Ipv4EntryInner.from_json(json)
# print the JSON string representation of the object
print(RoutePrefixListsTypeIpv4Ipv4EntryInner.to_json())

# convert the object into a dict
route_prefix_lists_type_ipv4_ipv4_entry_inner_dict = route_prefix_lists_type_ipv4_ipv4_entry_inner_instance.to_dict()
# create an instance of RoutePrefixListsTypeIpv4Ipv4EntryInner from a dict
route_prefix_lists_type_ipv4_ipv4_entry_inner_from_dict = RoutePrefixListsTypeIpv4Ipv4EntryInner.from_dict(route_prefix_lists_type_ipv4_ipv4_entry_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


