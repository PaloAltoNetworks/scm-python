# LogicalRoutersVrfInnerOspfv3AreaInnerTypeNssaAbr


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**export_list** | **str** |  | [optional] 
**import_list** | **str** |  | [optional] 
**inbound_filter_list** | **str** |  | [optional] 
**nssa_ext_range** | [**List[LogicalRoutersVrfInnerOspfv3AreaInnerTypeNssaAbrNssaExtRangeInner]**](LogicalRoutersVrfInnerOspfv3AreaInnerTypeNssaAbrNssaExtRangeInner.md) |  | [optional] 
**outbound_filter_list** | **str** |  | [optional] 

## Example

```python
from scm_network_services.models.logical_routers_vrf_inner_ospfv3_area_inner_type_nssa_abr import LogicalRoutersVrfInnerOspfv3AreaInnerTypeNssaAbr

# TODO update the JSON string below
json = "{}"
# create an instance of LogicalRoutersVrfInnerOspfv3AreaInnerTypeNssaAbr from a JSON string
logical_routers_vrf_inner_ospfv3_area_inner_type_nssa_abr_instance = LogicalRoutersVrfInnerOspfv3AreaInnerTypeNssaAbr.from_json(json)
# print the JSON string representation of the object
print(LogicalRoutersVrfInnerOspfv3AreaInnerTypeNssaAbr.to_json())

# convert the object into a dict
logical_routers_vrf_inner_ospfv3_area_inner_type_nssa_abr_dict = logical_routers_vrf_inner_ospfv3_area_inner_type_nssa_abr_instance.to_dict()
# create an instance of LogicalRoutersVrfInnerOspfv3AreaInnerTypeNssaAbr from a dict
logical_routers_vrf_inner_ospfv3_area_inner_type_nssa_abr_from_dict = LogicalRoutersVrfInnerOspfv3AreaInnerTypeNssaAbr.from_dict(logical_routers_vrf_inner_ospfv3_area_inner_type_nssa_abr_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


