# LogicalRoutersVrfInnerOspfGracefulRestart


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enable** | **bool** |  | [optional] 
**grace_period** | **int** |  | [optional] 
**helper_enable** | **bool** |  | [optional] 
**max_neighbor_restart_time** | **int** |  | [optional] 
**strict_lsa_checking** | **bool** |  | [optional] 

## Example

```python
from scm_network_services.models.logical_routers_vrf_inner_ospf_graceful_restart import LogicalRoutersVrfInnerOspfGracefulRestart

# TODO update the JSON string below
json = "{}"
# create an instance of LogicalRoutersVrfInnerOspfGracefulRestart from a JSON string
logical_routers_vrf_inner_ospf_graceful_restart_instance = LogicalRoutersVrfInnerOspfGracefulRestart.from_json(json)
# print the JSON string representation of the object
print(LogicalRoutersVrfInnerOspfGracefulRestart.to_json())

# convert the object into a dict
logical_routers_vrf_inner_ospf_graceful_restart_dict = logical_routers_vrf_inner_ospf_graceful_restart_instance.to_dict()
# create an instance of LogicalRoutersVrfInnerOspfGracefulRestart from a dict
logical_routers_vrf_inner_ospf_graceful_restart_from_dict = LogicalRoutersVrfInnerOspfGracefulRestart.from_dict(logical_routers_vrf_inner_ospf_graceful_restart_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


