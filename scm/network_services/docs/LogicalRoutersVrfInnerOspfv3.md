# LogicalRoutersVrfInnerOspfv3


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allow_redist_default_route** | **bool** |  | [optional] 
**area** | [**List[LogicalRoutersVrfInnerOspfv3AreaInner]**](LogicalRoutersVrfInnerOspfv3AreaInner.md) |  | [optional] 
**auth_profile** | [**List[LogicalRoutersVrfInnerOspfv3AuthProfileInner]**](LogicalRoutersVrfInnerOspfv3AuthProfileInner.md) |  | [optional] 
**disable_transit_traffic** | **bool** |  | [optional] 
**enable** | **bool** |  | [optional] 
**export_rules** | [**List[LogicalRoutersVrfInnerOspfExportRulesInner]**](LogicalRoutersVrfInnerOspfExportRulesInner.md) |  | [optional] 
**global_bfd** | [**LogicalRoutersVrfInnerBgpGlobalBfd**](LogicalRoutersVrfInnerBgpGlobalBfd.md) |  | [optional] 
**global_if_timer** | **str** |  | [optional] 
**graceful_restart** | [**LogicalRoutersVrfInnerOspfGracefulRestart**](LogicalRoutersVrfInnerOspfGracefulRestart.md) |  | [optional] 
**redistribution_profile** | **str** |  | [optional] 
**reject_default_route** | **bool** |  | [optional] 
**router_id** | **str** |  | [optional] 
**spf_timer** | **str** |  | [optional] 
**vr_timers** | [**LogicalRoutersVrfInnerOspfVrTimers**](LogicalRoutersVrfInnerOspfVrTimers.md) |  | [optional] 

## Example

```python
from scm.network_services.models.logical_routers_vrf_inner_ospfv3 import LogicalRoutersVrfInnerOspfv3

# TODO update the JSON string below
json = "{}"
# create an instance of LogicalRoutersVrfInnerOspfv3 from a JSON string
logical_routers_vrf_inner_ospfv3_instance = LogicalRoutersVrfInnerOspfv3.from_json(json)
# print the JSON string representation of the object
print(LogicalRoutersVrfInnerOspfv3.to_json())

# convert the object into a dict
logical_routers_vrf_inner_ospfv3_dict = logical_routers_vrf_inner_ospfv3_instance.to_dict()
# create an instance of LogicalRoutersVrfInnerOspfv3 from a dict
logical_routers_vrf_inner_ospfv3_from_dict = LogicalRoutersVrfInnerOspfv3.from_dict(logical_routers_vrf_inner_ospfv3_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


