# RoutePrefixListsType

Address Family Type

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ipv4** | [**RoutePrefixListsTypeIpv4**](RoutePrefixListsTypeIpv4.md) |  | 

## Example

```python
from scm_network_services.models.route_prefix_lists_type import RoutePrefixListsType

# TODO update the JSON string below
json = "{}"
# create an instance of RoutePrefixListsType from a JSON string
route_prefix_lists_type_instance = RoutePrefixListsType.from_json(json)
# print the JSON string representation of the object
print(RoutePrefixListsType.to_json())

# convert the object into a dict
route_prefix_lists_type_dict = route_prefix_lists_type_instance.to_dict()
# create an instance of RoutePrefixListsType from a dict
route_prefix_lists_type_from_dict = RoutePrefixListsType.from_dict(route_prefix_lists_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


