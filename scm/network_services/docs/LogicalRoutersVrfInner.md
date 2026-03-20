# LogicalRoutersVrfInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**admin_dists** | [**LogicalRoutersVrfInnerAdminDists**](LogicalRoutersVrfInnerAdminDists.md) |  | [optional] 
**bgp** | [**LogicalRoutersVrfInnerBgp**](LogicalRoutersVrfInnerBgp.md) |  | [optional] 
**ecmp** | [**LogicalRoutersVrfInnerEcmp**](LogicalRoutersVrfInnerEcmp.md) |  | [optional] 
**global_vrid** | **int** |  | [optional] 
**interface** | **List[str]** |  | [optional] 
**multicast** | [**LogicalRoutersVrfInnerMulticast**](LogicalRoutersVrfInnerMulticast.md) |  | [optional] 
**name** | **str** |  | 
**ospf** | [**LogicalRoutersVrfInnerOspf**](LogicalRoutersVrfInnerOspf.md) |  | [optional] 
**ospfv3** | [**LogicalRoutersVrfInnerOspfv3**](LogicalRoutersVrfInnerOspfv3.md) |  | [optional] 
**rib_filter** | [**LogicalRoutersVrfInnerRibFilter**](LogicalRoutersVrfInnerRibFilter.md) |  | [optional] 
**rip** | [**LogicalRoutersVrfInnerRip**](LogicalRoutersVrfInnerRip.md) |  | [optional] 
**routing_table** | [**LogicalRoutersVrfInnerRoutingTable**](LogicalRoutersVrfInnerRoutingTable.md) |  | [optional] 
**sdwan_type** | **str** |  | [optional] 
**vr_admin_dists** | [**LogicalRoutersVrfInnerVrAdminDists**](LogicalRoutersVrfInnerVrAdminDists.md) |  | [optional] 
**zone_name** | **str** |  | [optional] 

## Example

```python
from scm.network_services.models.logical_routers_vrf_inner import LogicalRoutersVrfInner

# TODO update the JSON string below
json = "{}"
# create an instance of LogicalRoutersVrfInner from a JSON string
logical_routers_vrf_inner_instance = LogicalRoutersVrfInner.from_json(json)
# print the JSON string representation of the object
print(LogicalRoutersVrfInner.to_json())

# convert the object into a dict
logical_routers_vrf_inner_dict = logical_routers_vrf_inner_instance.to_dict()
# create an instance of LogicalRoutersVrfInner from a dict
logical_routers_vrf_inner_from_dict = LogicalRoutersVrfInner.from_dict(logical_routers_vrf_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


