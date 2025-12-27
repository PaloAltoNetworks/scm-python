# LogicalRoutersVrfInnerRip


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**auth_profile** | **str** |  | [optional] 
**default_information_originate** | **bool** |  | [optional] 
**enable** | **bool** |  | [optional] 
**global_bfd** | [**LogicalRoutersVrfInnerBgpGlobalBfd**](LogicalRoutersVrfInnerBgpGlobalBfd.md) |  | [optional] 
**global_inbound_distribute_list** | [**LogicalRoutersVrfInnerRipGlobalInboundDistributeList**](LogicalRoutersVrfInnerRipGlobalInboundDistributeList.md) |  | [optional] 
**global_outbound_distribute_list** | [**LogicalRoutersVrfInnerRipGlobalInboundDistributeList**](LogicalRoutersVrfInnerRipGlobalInboundDistributeList.md) |  | [optional] 
**global_timer** | **str** |  | [optional] 
**interface** | [**List[LogicalRoutersVrfInnerRipInterfaceInner]**](LogicalRoutersVrfInnerRipInterfaceInner.md) |  | [optional] 
**redistribution_profile** | **str** |  | [optional] 

## Example

```python
from scm_network_services.models.logical_routers_vrf_inner_rip import LogicalRoutersVrfInnerRip

# TODO update the JSON string below
json = "{}"
# create an instance of LogicalRoutersVrfInnerRip from a JSON string
logical_routers_vrf_inner_rip_instance = LogicalRoutersVrfInnerRip.from_json(json)
# print the JSON string representation of the object
print(LogicalRoutersVrfInnerRip.to_json())

# convert the object into a dict
logical_routers_vrf_inner_rip_dict = logical_routers_vrf_inner_rip_instance.to_dict()
# create an instance of LogicalRoutersVrfInnerRip from a dict
logical_routers_vrf_inner_rip_from_dict = LogicalRoutersVrfInnerRip.from_dict(logical_routers_vrf_inner_rip_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


