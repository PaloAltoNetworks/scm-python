# LogicalRoutersVrfInnerOspfv3AreaInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**authentication** | **str** |  | [optional] 
**interface** | [**List[LogicalRoutersVrfInnerOspfv3AreaInnerInterfaceInner]**](LogicalRoutersVrfInnerOspfv3AreaInnerInterfaceInner.md) |  | [optional] 
**name** | **str** |  | 
**range** | [**List[LogicalRoutersVrfInnerOspfv3AreaInnerRangeInner]**](LogicalRoutersVrfInnerOspfv3AreaInnerRangeInner.md) |  | [optional] 
**type** | [**LogicalRoutersVrfInnerOspfv3AreaInnerType**](LogicalRoutersVrfInnerOspfv3AreaInnerType.md) |  | [optional] 
**virtual_link** | [**List[LogicalRoutersVrfInnerOspfAreaInnerVirtualLinkInner]**](LogicalRoutersVrfInnerOspfAreaInnerVirtualLinkInner.md) |  | [optional] 
**vr_range** | [**List[LogicalRoutersVrfInnerOspfAreaInnerTypeNssaNssaExtRangeInner]**](LogicalRoutersVrfInnerOspfAreaInnerTypeNssaNssaExtRangeInner.md) |  | [optional] 

## Example

```python
from scm.network_services.models.logical_routers_vrf_inner_ospfv3_area_inner import LogicalRoutersVrfInnerOspfv3AreaInner

# TODO update the JSON string below
json = "{}"
# create an instance of LogicalRoutersVrfInnerOspfv3AreaInner from a JSON string
logical_routers_vrf_inner_ospfv3_area_inner_instance = LogicalRoutersVrfInnerOspfv3AreaInner.from_json(json)
# print the JSON string representation of the object
print(LogicalRoutersVrfInnerOspfv3AreaInner.to_json())

# convert the object into a dict
logical_routers_vrf_inner_ospfv3_area_inner_dict = logical_routers_vrf_inner_ospfv3_area_inner_instance.to_dict()
# create an instance of LogicalRoutersVrfInnerOspfv3AreaInner from a dict
logical_routers_vrf_inner_ospfv3_area_inner_from_dict = LogicalRoutersVrfInnerOspfv3AreaInner.from_dict(logical_routers_vrf_inner_ospfv3_area_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


