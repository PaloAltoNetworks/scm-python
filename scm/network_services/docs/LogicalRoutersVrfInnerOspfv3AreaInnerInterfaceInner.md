# LogicalRoutersVrfInnerOspfv3AreaInnerInterfaceInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**authentication** | **str** |  | [optional] 
**bfd** | [**LogicalRoutersVrfInnerBgpGlobalBfd**](LogicalRoutersVrfInnerBgpGlobalBfd.md) |  | [optional] 
**enable** | **bool** |  | [optional] 
**instance_id** | **int** |  | [optional] 
**link_type** | [**LogicalRoutersVrfInnerOspfAreaInnerInterfaceInnerLinkType**](LogicalRoutersVrfInnerOspfAreaInnerInterfaceInnerLinkType.md) |  | [optional] 
**metric** | **int** |  | [optional] 
**mtu_ignore** | **bool** |  | [optional] 
**name** | **str** |  | 
**neighbor** | [**List[LogicalRoutersVrfInnerMulticastInterfaceGroupInnerPimAllowedNeighborsInner]**](LogicalRoutersVrfInnerMulticastInterfaceGroupInnerPimAllowedNeighborsInner.md) |  | [optional] 
**passive** | **bool** |  | [optional] 
**priority** | **int** |  | [optional] 
**timing** | **str** |  | [optional] 
**vr_timing** | [**LogicalRoutersVrfInnerOspfAreaInnerInterfaceInnerVrTiming**](LogicalRoutersVrfInnerOspfAreaInnerInterfaceInnerVrTiming.md) |  | [optional] 

## Example

```python
from scm_network_services.models.logical_routers_vrf_inner_ospfv3_area_inner_interface_inner import LogicalRoutersVrfInnerOspfv3AreaInnerInterfaceInner

# TODO update the JSON string below
json = "{}"
# create an instance of LogicalRoutersVrfInnerOspfv3AreaInnerInterfaceInner from a JSON string
logical_routers_vrf_inner_ospfv3_area_inner_interface_inner_instance = LogicalRoutersVrfInnerOspfv3AreaInnerInterfaceInner.from_json(json)
# print the JSON string representation of the object
print(LogicalRoutersVrfInnerOspfv3AreaInnerInterfaceInner.to_json())

# convert the object into a dict
logical_routers_vrf_inner_ospfv3_area_inner_interface_inner_dict = logical_routers_vrf_inner_ospfv3_area_inner_interface_inner_instance.to_dict()
# create an instance of LogicalRoutersVrfInnerOspfv3AreaInnerInterfaceInner from a dict
logical_routers_vrf_inner_ospfv3_area_inner_interface_inner_from_dict = LogicalRoutersVrfInnerOspfv3AreaInnerInterfaceInner.from_dict(logical_routers_vrf_inner_ospfv3_area_inner_interface_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


