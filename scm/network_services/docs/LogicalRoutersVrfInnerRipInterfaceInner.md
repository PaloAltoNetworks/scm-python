# LogicalRoutersVrfInnerRipInterfaceInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**authentication** | **str** |  | [optional] 
**bfd** | [**LogicalRoutersVrfInnerBgpGlobalBfd**](LogicalRoutersVrfInnerBgpGlobalBfd.md) |  | [optional] 
**enable** | **bool** |  | [optional] 
**interface_inbound_distribute_list** | [**LogicalRoutersVrfInnerRipInterfaceInnerInterfaceInboundDistributeList**](LogicalRoutersVrfInnerRipInterfaceInnerInterfaceInboundDistributeList.md) |  | [optional] 
**interface_outbound_distribute_list** | [**LogicalRoutersVrfInnerRipInterfaceInnerInterfaceInboundDistributeList**](LogicalRoutersVrfInnerRipInterfaceInnerInterfaceInboundDistributeList.md) |  | [optional] 
**mode** | **str** |  | [optional] 
**name** | **str** |  | 
**split_horizon** | **str** |  | [optional] 

## Example

```python
from scm_network_services.models.logical_routers_vrf_inner_rip_interface_inner import LogicalRoutersVrfInnerRipInterfaceInner

# TODO update the JSON string below
json = "{}"
# create an instance of LogicalRoutersVrfInnerRipInterfaceInner from a JSON string
logical_routers_vrf_inner_rip_interface_inner_instance = LogicalRoutersVrfInnerRipInterfaceInner.from_json(json)
# print the JSON string representation of the object
print(LogicalRoutersVrfInnerRipInterfaceInner.to_json())

# convert the object into a dict
logical_routers_vrf_inner_rip_interface_inner_dict = logical_routers_vrf_inner_rip_interface_inner_instance.to_dict()
# create an instance of LogicalRoutersVrfInnerRipInterfaceInner from a dict
logical_routers_vrf_inner_rip_interface_inner_from_dict = LogicalRoutersVrfInnerRipInterfaceInner.from_dict(logical_routers_vrf_inner_rip_interface_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


