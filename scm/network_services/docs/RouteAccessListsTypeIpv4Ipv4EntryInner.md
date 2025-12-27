# RouteAccessListsTypeIpv4Ipv4EntryInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **str** | Action | [optional] 
**destination_address** | [**RouteAccessListsTypeIpv4Ipv4EntryInnerDestinationAddress**](RouteAccessListsTypeIpv4Ipv4EntryInnerDestinationAddress.md) |  | [optional] 
**name** | **int** | Sequence number | [optional] 
**source_address** | [**RouteAccessListsTypeIpv4Ipv4EntryInnerSourceAddress**](RouteAccessListsTypeIpv4Ipv4EntryInnerSourceAddress.md) |  | [optional] 

## Example

```python
from scm_network_services.models.route_access_lists_type_ipv4_ipv4_entry_inner import RouteAccessListsTypeIpv4Ipv4EntryInner

# TODO update the JSON string below
json = "{}"
# create an instance of RouteAccessListsTypeIpv4Ipv4EntryInner from a JSON string
route_access_lists_type_ipv4_ipv4_entry_inner_instance = RouteAccessListsTypeIpv4Ipv4EntryInner.from_json(json)
# print the JSON string representation of the object
print(RouteAccessListsTypeIpv4Ipv4EntryInner.to_json())

# convert the object into a dict
route_access_lists_type_ipv4_ipv4_entry_inner_dict = route_access_lists_type_ipv4_ipv4_entry_inner_instance.to_dict()
# create an instance of RouteAccessListsTypeIpv4Ipv4EntryInner from a dict
route_access_lists_type_ipv4_ipv4_entry_inner_from_dict = RouteAccessListsTypeIpv4Ipv4EntryInner.from_dict(route_access_lists_type_ipv4_ipv4_entry_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


