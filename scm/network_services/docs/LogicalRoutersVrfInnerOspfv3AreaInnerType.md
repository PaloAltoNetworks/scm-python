# LogicalRoutersVrfInnerOspfv3AreaInnerType


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**normal** | [**LogicalRoutersVrfInnerOspfAreaInnerTypeNormal**](LogicalRoutersVrfInnerOspfAreaInnerTypeNormal.md) |  | [optional] 
**nssa** | [**LogicalRoutersVrfInnerOspfv3AreaInnerTypeNssa**](LogicalRoutersVrfInnerOspfv3AreaInnerTypeNssa.md) |  | [optional] 
**stub** | [**LogicalRoutersVrfInnerOspfAreaInnerTypeStub**](LogicalRoutersVrfInnerOspfAreaInnerTypeStub.md) |  | [optional] 

## Example

```python
from scm.network_services.models.logical_routers_vrf_inner_ospfv3_area_inner_type import LogicalRoutersVrfInnerOspfv3AreaInnerType

# TODO update the JSON string below
json = "{}"
# create an instance of LogicalRoutersVrfInnerOspfv3AreaInnerType from a JSON string
logical_routers_vrf_inner_ospfv3_area_inner_type_instance = LogicalRoutersVrfInnerOspfv3AreaInnerType.from_json(json)
# print the JSON string representation of the object
print(LogicalRoutersVrfInnerOspfv3AreaInnerType.to_json())

# convert the object into a dict
logical_routers_vrf_inner_ospfv3_area_inner_type_dict = logical_routers_vrf_inner_ospfv3_area_inner_type_instance.to_dict()
# create an instance of LogicalRoutersVrfInnerOspfv3AreaInnerType from a dict
logical_routers_vrf_inner_ospfv3_area_inner_type_from_dict = LogicalRoutersVrfInnerOspfv3AreaInnerType.from_dict(logical_routers_vrf_inner_ospfv3_area_inner_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


