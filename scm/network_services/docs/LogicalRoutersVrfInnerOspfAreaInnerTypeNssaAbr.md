# LogicalRoutersVrfInnerOspfAreaInnerTypeNssaAbr


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**export_list** | **str** |  | [optional] 
**import_list** | **str** |  | [optional] 
**inbound_filter_list** | **str** |  | [optional] 
**nssa_ext_range** | [**List[LogicalRoutersVrfInnerOspfAreaInnerTypeNssaAbrNssaExtRangeInner]**](LogicalRoutersVrfInnerOspfAreaInnerTypeNssaAbrNssaExtRangeInner.md) |  | [optional] 
**outbound_filter_list** | **str** |  | [optional] 

## Example

```python
from scm.network_services.models.logical_routers_vrf_inner_ospf_area_inner_type_nssa_abr import LogicalRoutersVrfInnerOspfAreaInnerTypeNssaAbr

# TODO update the JSON string below
json = "{}"
# create an instance of LogicalRoutersVrfInnerOspfAreaInnerTypeNssaAbr from a JSON string
logical_routers_vrf_inner_ospf_area_inner_type_nssa_abr_instance = LogicalRoutersVrfInnerOspfAreaInnerTypeNssaAbr.from_json(json)
# print the JSON string representation of the object
print(LogicalRoutersVrfInnerOspfAreaInnerTypeNssaAbr.to_json())

# convert the object into a dict
logical_routers_vrf_inner_ospf_area_inner_type_nssa_abr_dict = logical_routers_vrf_inner_ospf_area_inner_type_nssa_abr_instance.to_dict()
# create an instance of LogicalRoutersVrfInnerOspfAreaInnerTypeNssaAbr from a dict
logical_routers_vrf_inner_ospf_area_inner_type_nssa_abr_from_dict = LogicalRoutersVrfInnerOspfAreaInnerTypeNssaAbr.from_dict(logical_routers_vrf_inner_ospf_area_inner_type_nssa_abr_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


