# LogicalRoutersVrfInnerOspfAreaInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**authentication** | **str** |  | [optional] 
**interface** | [**List[LogicalRoutersVrfInnerOspfAreaInnerInterfaceInner]**](LogicalRoutersVrfInnerOspfAreaInnerInterfaceInner.md) |  | [optional] 
**name** | **str** |  | 
**range** | [**List[LogicalRoutersVrfInnerOspfAreaInnerRangeInner]**](LogicalRoutersVrfInnerOspfAreaInnerRangeInner.md) |  | [optional] 
**type** | [**LogicalRoutersVrfInnerOspfAreaInnerType**](LogicalRoutersVrfInnerOspfAreaInnerType.md) |  | [optional] 
**virtual_link** | [**List[LogicalRoutersVrfInnerOspfAreaInnerVirtualLinkInner]**](LogicalRoutersVrfInnerOspfAreaInnerVirtualLinkInner.md) |  | [optional] 
**vr_range** | [**List[LogicalRoutersVrfInnerOspfAreaInnerTypeNssaNssaExtRangeInner]**](LogicalRoutersVrfInnerOspfAreaInnerTypeNssaNssaExtRangeInner.md) |  | [optional] 

## Example

```python
from scm_network_services.models.logical_routers_vrf_inner_ospf_area_inner import LogicalRoutersVrfInnerOspfAreaInner

# TODO update the JSON string below
json = "{}"
# create an instance of LogicalRoutersVrfInnerOspfAreaInner from a JSON string
logical_routers_vrf_inner_ospf_area_inner_instance = LogicalRoutersVrfInnerOspfAreaInner.from_json(json)
# print the JSON string representation of the object
print(LogicalRoutersVrfInnerOspfAreaInner.to_json())

# convert the object into a dict
logical_routers_vrf_inner_ospf_area_inner_dict = logical_routers_vrf_inner_ospf_area_inner_instance.to_dict()
# create an instance of LogicalRoutersVrfInnerOspfAreaInner from a dict
logical_routers_vrf_inner_ospf_area_inner_from_dict = LogicalRoutersVrfInnerOspfAreaInner.from_dict(logical_routers_vrf_inner_ospf_area_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


