# LogicalRoutersVrfInnerBgp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**advertise_network** | [**LogicalRoutersVrfInnerBgpAdvertiseNetwork**](LogicalRoutersVrfInnerBgpAdvertiseNetwork.md) |  | [optional] 
**aggregate** | [**LogicalRoutersVrfInnerBgpAggregate**](LogicalRoutersVrfInnerBgpAggregate.md) |  | [optional] 
**aggregate_routes** | [**List[LogicalRoutersVrfInnerBgpAggregateRoutesInner]**](LogicalRoutersVrfInnerBgpAggregateRoutesInner.md) |  | [optional] 
**allow_redist_default_route** | **bool** |  | [optional] 
**always_advertise_network_route** | **bool** |  | [optional] 
**as_format** | **str** |  | [optional] 
**confederation_member_as** | **str** |  | [optional] 
**default_local_preference** | **int** |  | [optional] 
**ecmp_multi_as** | **bool** |  | [optional] 
**enable** | **bool** |  | [optional] 
**enforce_first_as** | **bool** |  | [optional] 
**fast_external_failover** | **bool** |  | [optional] 
**global_bfd** | [**LogicalRoutersVrfInnerBgpGlobalBfd**](LogicalRoutersVrfInnerBgpGlobalBfd.md) |  | [optional] 
**graceful_restart** | [**LogicalRoutersVrfInnerBgpGracefulRestart**](LogicalRoutersVrfInnerBgpGracefulRestart.md) |  | [optional] 
**graceful_shutdown** | **bool** |  | [optional] 
**install_route** | **bool** |  | [optional] 
**local_as** | **str** |  | [optional] 
**med** | [**LogicalRoutersVrfInnerBgpMed**](LogicalRoutersVrfInnerBgpMed.md) |  | [optional] 
**peer_group** | [**List[LogicalRoutersVrfInnerBgpPeerGroupInner]**](LogicalRoutersVrfInnerBgpPeerGroupInner.md) |  | [optional] 
**policy** | [**LogicalRoutersVrfInnerBgpPolicy**](LogicalRoutersVrfInnerBgpPolicy.md) |  | [optional] 
**redist_rules** | [**List[LogicalRoutersVrfInnerBgpRedistRulesInner]**](LogicalRoutersVrfInnerBgpRedistRulesInner.md) |  | [optional] 
**redistribution_profile** | [**LogicalRoutersVrfInnerBgpRedistributionProfile**](LogicalRoutersVrfInnerBgpRedistributionProfile.md) |  | [optional] 
**reject_default_route** | **bool** |  | [optional] 
**router_id** | **str** |  | [optional] 

## Example

```python
from scm_network_services.models.logical_routers_vrf_inner_bgp import LogicalRoutersVrfInnerBgp

# TODO update the JSON string below
json = "{}"
# create an instance of LogicalRoutersVrfInnerBgp from a JSON string
logical_routers_vrf_inner_bgp_instance = LogicalRoutersVrfInnerBgp.from_json(json)
# print the JSON string representation of the object
print(LogicalRoutersVrfInnerBgp.to_json())

# convert the object into a dict
logical_routers_vrf_inner_bgp_dict = logical_routers_vrf_inner_bgp_instance.to_dict()
# create an instance of LogicalRoutersVrfInnerBgp from a dict
logical_routers_vrf_inner_bgp_from_dict = LogicalRoutersVrfInnerBgp.from_dict(logical_routers_vrf_inner_bgp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


