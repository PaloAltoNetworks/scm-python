# RoutePrefixListsTypeIpv4


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ipv4_entry** | [**List[RoutePrefixListsTypeIpv4Ipv4EntryInner]**](RoutePrefixListsTypeIpv4Ipv4EntryInner.md) | IPv4 prefix lists | [optional] 

## Example

```python
from scm.network_services.models.route_prefix_lists_type_ipv4 import RoutePrefixListsTypeIpv4

# TODO update the JSON string below
json = "{}"
# create an instance of RoutePrefixListsTypeIpv4 from a JSON string
route_prefix_lists_type_ipv4_instance = RoutePrefixListsTypeIpv4.from_json(json)
# print the JSON string representation of the object
print(RoutePrefixListsTypeIpv4.to_json())

# convert the object into a dict
route_prefix_lists_type_ipv4_dict = route_prefix_lists_type_ipv4_instance.to_dict()
# create an instance of RoutePrefixListsTypeIpv4 from a dict
route_prefix_lists_type_ipv4_from_dict = RoutePrefixListsTypeIpv4.from_dict(route_prefix_lists_type_ipv4_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


