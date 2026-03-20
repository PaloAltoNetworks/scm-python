# LogicalRoutersVrfInnerMulticastPim


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enable** | **bool** |  | [optional] 
**group_permission** | **str** |  | [optional] 
**if_timer_global** | **str** |  | [optional] 
**interface** | [**List[LogicalRoutersVrfInnerMulticastPimInterfaceInner]**](LogicalRoutersVrfInnerMulticastPimInterfaceInner.md) |  | [optional] 
**route_ageout_time** | **int** |  | [optional] 
**rp** | [**LogicalRoutersVrfInnerMulticastPimRp**](LogicalRoutersVrfInnerMulticastPimRp.md) |  | [optional] 
**rpf_lookup_mode** | **str** |  | [optional] 
**spt_threshold** | [**List[LogicalRoutersVrfInnerMulticastPimSptThresholdInner]**](LogicalRoutersVrfInnerMulticastPimSptThresholdInner.md) |  | [optional] 
**ssm_address_space** | [**LogicalRoutersVrfInnerMulticastPimSsmAddressSpace**](LogicalRoutersVrfInnerMulticastPimSsmAddressSpace.md) |  | [optional] 

## Example

```python
from scm.network_services.models.logical_routers_vrf_inner_multicast_pim import LogicalRoutersVrfInnerMulticastPim

# TODO update the JSON string below
json = "{}"
# create an instance of LogicalRoutersVrfInnerMulticastPim from a JSON string
logical_routers_vrf_inner_multicast_pim_instance = LogicalRoutersVrfInnerMulticastPim.from_json(json)
# print the JSON string representation of the object
print(LogicalRoutersVrfInnerMulticastPim.to_json())

# convert the object into a dict
logical_routers_vrf_inner_multicast_pim_dict = logical_routers_vrf_inner_multicast_pim_instance.to_dict()
# create an instance of LogicalRoutersVrfInnerMulticastPim from a dict
logical_routers_vrf_inner_multicast_pim_from_dict = LogicalRoutersVrfInnerMulticastPim.from_dict(logical_routers_vrf_inner_multicast_pim_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


