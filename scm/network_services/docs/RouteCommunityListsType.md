# RouteCommunityListsType


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**extended** | [**RouteCommunityListsTypeExtended**](RouteCommunityListsTypeExtended.md) |  | [optional] 
**large** | [**RouteCommunityListsTypeLarge**](RouteCommunityListsTypeLarge.md) |  | [optional] 
**regular** | [**RouteCommunityListsTypeRegular**](RouteCommunityListsTypeRegular.md) |  | [optional] 

## Example

```python
from scm.network_services.models.route_community_lists_type import RouteCommunityListsType

# TODO update the JSON string below
json = "{}"
# create an instance of RouteCommunityListsType from a JSON string
route_community_lists_type_instance = RouteCommunityListsType.from_json(json)
# print the JSON string representation of the object
print(RouteCommunityListsType.to_json())

# convert the object into a dict
route_community_lists_type_dict = route_community_lists_type_instance.to_dict()
# create an instance of RouteCommunityListsType from a dict
route_community_lists_type_from_dict = RouteCommunityListsType.from_dict(route_community_lists_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


