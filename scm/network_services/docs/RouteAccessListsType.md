# RouteAccessListsType


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ipv4** | [**RouteAccessListsTypeIpv4**](RouteAccessListsTypeIpv4.md) |  | [optional] 

## Example

```python
from scm.network_services.models.route_access_lists_type import RouteAccessListsType

# TODO update the JSON string below
json = "{}"
# create an instance of RouteAccessListsType from a JSON string
route_access_lists_type_instance = RouteAccessListsType.from_json(json)
# print the JSON string representation of the object
print(RouteAccessListsType.to_json())

# convert the object into a dict
route_access_lists_type_dict = route_access_lists_type_instance.to_dict()
# create an instance of RouteAccessListsType from a dict
route_access_lists_type_from_dict = RouteAccessListsType.from_dict(route_access_lists_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


