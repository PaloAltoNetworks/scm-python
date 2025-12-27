# LogicalRoutersVrfInnerOspfAreaInnerVirtualLinkInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**authentication** | **str** |  | [optional] 
**bfd** | [**LogicalRoutersVrfInnerBgpGlobalBfd**](LogicalRoutersVrfInnerBgpGlobalBfd.md) |  | [optional] 
**enable** | **bool** |  | [optional] 
**instance_id** | **int** |  | [optional] 
**interface_id** | **int** |  | [optional] 
**name** | **str** |  | 
**neighbor_id** | **str** |  | [optional] 
**passive** | **bool** |  | [optional] 
**timing** | **str** |  | [optional] 
**transit_area_id** | **str** |  | [optional] 
**vr_timing** | [**LogicalRoutersVrfInnerOspfAreaInnerVirtualLinkInnerVrTiming**](LogicalRoutersVrfInnerOspfAreaInnerVirtualLinkInnerVrTiming.md) |  | [optional] 

## Example

```python
from scm.network_services.models.logical_routers_vrf_inner_ospf_area_inner_virtual_link_inner import LogicalRoutersVrfInnerOspfAreaInnerVirtualLinkInner

# TODO update the JSON string below
json = "{}"
# create an instance of LogicalRoutersVrfInnerOspfAreaInnerVirtualLinkInner from a JSON string
logical_routers_vrf_inner_ospf_area_inner_virtual_link_inner_instance = LogicalRoutersVrfInnerOspfAreaInnerVirtualLinkInner.from_json(json)
# print the JSON string representation of the object
print(LogicalRoutersVrfInnerOspfAreaInnerVirtualLinkInner.to_json())

# convert the object into a dict
logical_routers_vrf_inner_ospf_area_inner_virtual_link_inner_dict = logical_routers_vrf_inner_ospf_area_inner_virtual_link_inner_instance.to_dict()
# create an instance of LogicalRoutersVrfInnerOspfAreaInnerVirtualLinkInner from a dict
logical_routers_vrf_inner_ospf_area_inner_virtual_link_inner_from_dict = LogicalRoutersVrfInnerOspfAreaInnerVirtualLinkInner.from_dict(logical_routers_vrf_inner_ospf_area_inner_virtual_link_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


