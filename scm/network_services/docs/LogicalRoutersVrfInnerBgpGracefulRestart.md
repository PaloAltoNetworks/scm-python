# LogicalRoutersVrfInnerBgpGracefulRestart


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enable** | **bool** |  | [optional] 
**local_restart_time** | **int** |  | [optional] 
**max_peer_restart_time** | **int** |  | [optional] 
**stale_route_time** | **int** |  | [optional] 

## Example

```python
from scm_network_services.models.logical_routers_vrf_inner_bgp_graceful_restart import LogicalRoutersVrfInnerBgpGracefulRestart

# TODO update the JSON string below
json = "{}"
# create an instance of LogicalRoutersVrfInnerBgpGracefulRestart from a JSON string
logical_routers_vrf_inner_bgp_graceful_restart_instance = LogicalRoutersVrfInnerBgpGracefulRestart.from_json(json)
# print the JSON string representation of the object
print(LogicalRoutersVrfInnerBgpGracefulRestart.to_json())

# convert the object into a dict
logical_routers_vrf_inner_bgp_graceful_restart_dict = logical_routers_vrf_inner_bgp_graceful_restart_instance.to_dict()
# create an instance of LogicalRoutersVrfInnerBgpGracefulRestart from a dict
logical_routers_vrf_inner_bgp_graceful_restart_from_dict = LogicalRoutersVrfInnerBgpGracefulRestart.from_dict(logical_routers_vrf_inner_bgp_graceful_restart_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


