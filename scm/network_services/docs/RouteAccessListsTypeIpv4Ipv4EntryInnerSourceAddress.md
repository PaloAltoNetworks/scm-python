# RouteAccessListsTypeIpv4Ipv4EntryInnerSourceAddress


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | **str** | Source IP address | [optional] 
**entry** | [**RouteAccessListsTypeIpv4Ipv4EntryInnerSourceAddressEntry**](RouteAccessListsTypeIpv4Ipv4EntryInnerSourceAddressEntry.md) |  | [optional] 

## Example

```python
from scm.network_services.models.route_access_lists_type_ipv4_ipv4_entry_inner_source_address import RouteAccessListsTypeIpv4Ipv4EntryInnerSourceAddress

# TODO update the JSON string below
json = "{}"
# create an instance of RouteAccessListsTypeIpv4Ipv4EntryInnerSourceAddress from a JSON string
route_access_lists_type_ipv4_ipv4_entry_inner_source_address_instance = RouteAccessListsTypeIpv4Ipv4EntryInnerSourceAddress.from_json(json)
# print the JSON string representation of the object
print(RouteAccessListsTypeIpv4Ipv4EntryInnerSourceAddress.to_json())

# convert the object into a dict
route_access_lists_type_ipv4_ipv4_entry_inner_source_address_dict = route_access_lists_type_ipv4_ipv4_entry_inner_source_address_instance.to_dict()
# create an instance of RouteAccessListsTypeIpv4Ipv4EntryInnerSourceAddress from a dict
route_access_lists_type_ipv4_ipv4_entry_inner_source_address_from_dict = RouteAccessListsTypeIpv4Ipv4EntryInnerSourceAddress.from_dict(route_access_lists_type_ipv4_ipv4_entry_inner_source_address_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


