# LogicalRoutersVrfInnerOspfAreaInnerInterfaceInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**authentication** | **str** |  | [optional] 
**bfd** | [**LogicalRoutersVrfInnerBgpGlobalBfd**](LogicalRoutersVrfInnerBgpGlobalBfd.md) |  | [optional] 
**enable** | **bool** |  | [optional] 
**link_type** | [**LogicalRoutersVrfInnerOspfAreaInnerInterfaceInnerLinkType**](LogicalRoutersVrfInnerOspfAreaInnerInterfaceInnerLinkType.md) |  | [optional] 
**metric** | **int** |  | [optional] 
**mtu_ignore** | **bool** |  | [optional] 
**name** | **str** |  | 
**passive** | **bool** |  | [optional] 
**priority** | **int** |  | [optional] 
**timing** | **str** |  | [optional] 
**vr_timing** | [**LogicalRoutersVrfInnerOspfAreaInnerInterfaceInnerVrTiming**](LogicalRoutersVrfInnerOspfAreaInnerInterfaceInnerVrTiming.md) |  | [optional] 

## Example

```python
from scm.network_services.models.logical_routers_vrf_inner_ospf_area_inner_interface_inner import LogicalRoutersVrfInnerOspfAreaInnerInterfaceInner

# TODO update the JSON string below
json = "{}"
# create an instance of LogicalRoutersVrfInnerOspfAreaInnerInterfaceInner from a JSON string
logical_routers_vrf_inner_ospf_area_inner_interface_inner_instance = LogicalRoutersVrfInnerOspfAreaInnerInterfaceInner.from_json(json)
# print the JSON string representation of the object
print(LogicalRoutersVrfInnerOspfAreaInnerInterfaceInner.to_json())

# convert the object into a dict
logical_routers_vrf_inner_ospf_area_inner_interface_inner_dict = logical_routers_vrf_inner_ospf_area_inner_interface_inner_instance.to_dict()
# create an instance of LogicalRoutersVrfInnerOspfAreaInnerInterfaceInner from a dict
logical_routers_vrf_inner_ospf_area_inner_interface_inner_from_dict = LogicalRoutersVrfInnerOspfAreaInnerInterfaceInner.from_dict(logical_routers_vrf_inner_ospf_area_inner_interface_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


