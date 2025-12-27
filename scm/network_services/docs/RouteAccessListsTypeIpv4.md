# RouteAccessListsTypeIpv4


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ipv4_entry** | [**List[RouteAccessListsTypeIpv4Ipv4EntryInner]**](RouteAccessListsTypeIpv4Ipv4EntryInner.md) | IPv4 access lists | [optional] 

## Example

```python
from scm_network_services.models.route_access_lists_type_ipv4 import RouteAccessListsTypeIpv4

# TODO update the JSON string below
json = "{}"
# create an instance of RouteAccessListsTypeIpv4 from a JSON string
route_access_lists_type_ipv4_instance = RouteAccessListsTypeIpv4.from_json(json)
# print the JSON string representation of the object
print(RouteAccessListsTypeIpv4.to_json())

# convert the object into a dict
route_access_lists_type_ipv4_dict = route_access_lists_type_ipv4_instance.to_dict()
# create an instance of RouteAccessListsTypeIpv4 from a dict
route_access_lists_type_ipv4_from_dict = RouteAccessListsTypeIpv4.from_dict(route_access_lists_type_ipv4_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


