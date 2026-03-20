# LogicalRoutersVrfInnerOspf


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allow_redist_default_route** | **bool** |  | [optional] 
**area** | [**List[LogicalRoutersVrfInnerOspfAreaInner]**](LogicalRoutersVrfInnerOspfAreaInner.md) |  | [optional] 
**auth_profile** | [**List[LogicalRoutersVrfInnerOspfAuthProfileInner]**](LogicalRoutersVrfInnerOspfAuthProfileInner.md) |  | [optional] 
**enable** | **bool** |  | [optional] 
**export_rules** | [**List[LogicalRoutersVrfInnerOspfExportRulesInner]**](LogicalRoutersVrfInnerOspfExportRulesInner.md) |  | [optional] 
**flood_prevention** | [**LogicalRoutersVrfInnerOspfFloodPrevention**](LogicalRoutersVrfInnerOspfFloodPrevention.md) |  | [optional] 
**global_bfd** | [**LogicalRoutersVrfInnerBgpGlobalBfd**](LogicalRoutersVrfInnerBgpGlobalBfd.md) |  | [optional] 
**global_if_timer** | **str** |  | [optional] 
**graceful_restart** | [**LogicalRoutersVrfInnerOspfGracefulRestart**](LogicalRoutersVrfInnerOspfGracefulRestart.md) |  | [optional] 
**redistribution_profile** | **str** |  | [optional] 
**reject_default_route** | **bool** |  | [optional] 
**rfc1583** | **bool** |  | [optional] 
**router_id** | **str** |  | [optional] 
**spf_timer** | **str** |  | [optional] 
**vr_timers** | [**LogicalRoutersVrfInnerOspfVrTimers**](LogicalRoutersVrfInnerOspfVrTimers.md) |  | [optional] 

## Example

```python
from scm.network_services.models.logical_routers_vrf_inner_ospf import LogicalRoutersVrfInnerOspf

# TODO update the JSON string below
json = "{}"
# create an instance of LogicalRoutersVrfInnerOspf from a JSON string
logical_routers_vrf_inner_ospf_instance = LogicalRoutersVrfInnerOspf.from_json(json)
# print the JSON string representation of the object
print(LogicalRoutersVrfInnerOspf.to_json())

# convert the object into a dict
logical_routers_vrf_inner_ospf_dict = logical_routers_vrf_inner_ospf_instance.to_dict()
# create an instance of LogicalRoutersVrfInnerOspf from a dict
logical_routers_vrf_inner_ospf_from_dict = LogicalRoutersVrfInnerOspf.from_dict(logical_routers_vrf_inner_ospf_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


