# LogicalRoutersVrfInnerOspfAreaInnerType


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**normal** | [**LogicalRoutersVrfInnerOspfAreaInnerTypeNormal**](LogicalRoutersVrfInnerOspfAreaInnerTypeNormal.md) |  | [optional] 
**nssa** | [**LogicalRoutersVrfInnerOspfAreaInnerTypeNssa**](LogicalRoutersVrfInnerOspfAreaInnerTypeNssa.md) |  | [optional] 
**stub** | [**LogicalRoutersVrfInnerOspfAreaInnerTypeStub**](LogicalRoutersVrfInnerOspfAreaInnerTypeStub.md) |  | [optional] 

## Example

```python
from scm.network_services.models.logical_routers_vrf_inner_ospf_area_inner_type import LogicalRoutersVrfInnerOspfAreaInnerType

# TODO update the JSON string below
json = "{}"
# create an instance of LogicalRoutersVrfInnerOspfAreaInnerType from a JSON string
logical_routers_vrf_inner_ospf_area_inner_type_instance = LogicalRoutersVrfInnerOspfAreaInnerType.from_json(json)
# print the JSON string representation of the object
print(LogicalRoutersVrfInnerOspfAreaInnerType.to_json())

# convert the object into a dict
logical_routers_vrf_inner_ospf_area_inner_type_dict = logical_routers_vrf_inner_ospf_area_inner_type_instance.to_dict()
# create an instance of LogicalRoutersVrfInnerOspfAreaInnerType from a dict
logical_routers_vrf_inner_ospf_area_inner_type_from_dict = LogicalRoutersVrfInnerOspfAreaInnerType.from_dict(logical_routers_vrf_inner_ospf_area_inner_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


