# LogicalRoutersVrfInnerOspfAreaInnerTypeNssa


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**abr** | [**LogicalRoutersVrfInnerOspfAreaInnerTypeNssaAbr**](LogicalRoutersVrfInnerOspfAreaInnerTypeNssaAbr.md) |  | [optional] 
**accept_summary** | **bool** |  | [optional] 
**default_information_originate** | [**LogicalRoutersVrfInnerOspfAreaInnerTypeNssaDefaultInformationOriginate**](LogicalRoutersVrfInnerOspfAreaInnerTypeNssaDefaultInformationOriginate.md) |  | [optional] 
**default_route** | [**LogicalRoutersVrfInnerOspfAreaInnerTypeNssaDefaultRoute**](LogicalRoutersVrfInnerOspfAreaInnerTypeNssaDefaultRoute.md) |  | [optional] 
**no_summary** | **bool** |  | [optional] 
**nssa_ext_range** | [**List[LogicalRoutersVrfInnerOspfAreaInnerTypeNssaNssaExtRangeInner]**](LogicalRoutersVrfInnerOspfAreaInnerTypeNssaNssaExtRangeInner.md) |  | [optional] 

## Example

```python
from scm_network_services.models.logical_routers_vrf_inner_ospf_area_inner_type_nssa import LogicalRoutersVrfInnerOspfAreaInnerTypeNssa

# TODO update the JSON string below
json = "{}"
# create an instance of LogicalRoutersVrfInnerOspfAreaInnerTypeNssa from a JSON string
logical_routers_vrf_inner_ospf_area_inner_type_nssa_instance = LogicalRoutersVrfInnerOspfAreaInnerTypeNssa.from_json(json)
# print the JSON string representation of the object
print(LogicalRoutersVrfInnerOspfAreaInnerTypeNssa.to_json())

# convert the object into a dict
logical_routers_vrf_inner_ospf_area_inner_type_nssa_dict = logical_routers_vrf_inner_ospf_area_inner_type_nssa_instance.to_dict()
# create an instance of LogicalRoutersVrfInnerOspfAreaInnerTypeNssa from a dict
logical_routers_vrf_inner_ospf_area_inner_type_nssa_from_dict = LogicalRoutersVrfInnerOspfAreaInnerTypeNssa.from_dict(logical_routers_vrf_inner_ospf_area_inner_type_nssa_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


