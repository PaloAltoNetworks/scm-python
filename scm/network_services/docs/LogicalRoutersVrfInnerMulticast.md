# LogicalRoutersVrfInnerMulticast


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enable** | **bool** |  | [optional] 
**enable_v6** | **bool** |  | [optional] 
**igmp** | [**LogicalRoutersVrfInnerMulticastIgmp**](LogicalRoutersVrfInnerMulticastIgmp.md) |  | [optional] 
**interface_group** | [**List[LogicalRoutersVrfInnerMulticastInterfaceGroupInner]**](LogicalRoutersVrfInnerMulticastInterfaceGroupInner.md) |  | [optional] 
**mode** | **str** |  | [optional] 
**msdp** | [**LogicalRoutersVrfInnerMulticastMsdp**](LogicalRoutersVrfInnerMulticastMsdp.md) |  | [optional] 
**pim** | [**LogicalRoutersVrfInnerMulticastPim**](LogicalRoutersVrfInnerMulticastPim.md) |  | [optional] 
**route_ageout_time** | **int** |  | [optional] 
**rp** | [**LogicalRoutersVrfInnerMulticastRp**](LogicalRoutersVrfInnerMulticastRp.md) |  | [optional] 
**spt_threshold** | [**List[LogicalRoutersVrfInnerMulticastPimSptThresholdInner]**](LogicalRoutersVrfInnerMulticastPimSptThresholdInner.md) |  | [optional] 
**ssm_address_space** | [**List[LogicalRoutersVrfInnerMulticastInterfaceGroupInnerGroupPermissionAnySourceMulticastInner]**](LogicalRoutersVrfInnerMulticastInterfaceGroupInnerGroupPermissionAnySourceMulticastInner.md) |  | [optional] 
**static_route** | [**List[LogicalRoutersVrfInnerMulticastStaticRouteInner]**](LogicalRoutersVrfInnerMulticastStaticRouteInner.md) |  | [optional] 

## Example

```python
from scm.network_services.models.logical_routers_vrf_inner_multicast import LogicalRoutersVrfInnerMulticast

# TODO update the JSON string below
json = "{}"
# create an instance of LogicalRoutersVrfInnerMulticast from a JSON string
logical_routers_vrf_inner_multicast_instance = LogicalRoutersVrfInnerMulticast.from_json(json)
# print the JSON string representation of the object
print(LogicalRoutersVrfInnerMulticast.to_json())

# convert the object into a dict
logical_routers_vrf_inner_multicast_dict = logical_routers_vrf_inner_multicast_instance.to_dict()
# create an instance of LogicalRoutersVrfInnerMulticast from a dict
logical_routers_vrf_inner_multicast_from_dict = LogicalRoutersVrfInnerMulticast.from_dict(logical_routers_vrf_inner_multicast_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


