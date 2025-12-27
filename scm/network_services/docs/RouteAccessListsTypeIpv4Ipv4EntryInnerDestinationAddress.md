# RouteAccessListsTypeIpv4Ipv4EntryInnerDestinationAddress


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | **str** | Destination IP address | [optional] 
**entry** | [**RouteAccessListsTypeIpv4Ipv4EntryInnerDestinationAddressEntry**](RouteAccessListsTypeIpv4Ipv4EntryInnerDestinationAddressEntry.md) |  | [optional] 

## Example

```python
from scm_network_services.models.route_access_lists_type_ipv4_ipv4_entry_inner_destination_address import RouteAccessListsTypeIpv4Ipv4EntryInnerDestinationAddress

# TODO update the JSON string below
json = "{}"
# create an instance of RouteAccessListsTypeIpv4Ipv4EntryInnerDestinationAddress from a JSON string
route_access_lists_type_ipv4_ipv4_entry_inner_destination_address_instance = RouteAccessListsTypeIpv4Ipv4EntryInnerDestinationAddress.from_json(json)
# print the JSON string representation of the object
print(RouteAccessListsTypeIpv4Ipv4EntryInnerDestinationAddress.to_json())

# convert the object into a dict
route_access_lists_type_ipv4_ipv4_entry_inner_destination_address_dict = route_access_lists_type_ipv4_ipv4_entry_inner_destination_address_instance.to_dict()
# create an instance of RouteAccessListsTypeIpv4Ipv4EntryInnerDestinationAddress from a dict
route_access_lists_type_ipv4_ipv4_entry_inner_destination_address_from_dict = RouteAccessListsTypeIpv4Ipv4EntryInnerDestinationAddress.from_dict(route_access_lists_type_ipv4_ipv4_entry_inner_destination_address_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


