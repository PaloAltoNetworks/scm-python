# LogicalRoutersVrfInnerBgpPeerGroupInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address_family** | [**LogicalRoutersVrfInnerBgpPeerGroupInnerAddressFamily**](LogicalRoutersVrfInnerBgpPeerGroupInnerAddressFamily.md) |  | [optional] 
**aggregated_confed_as_path** | **bool** |  | [optional] 
**connection_options** | [**LogicalRoutersVrfInnerBgpPeerGroupInnerConnectionOptions**](LogicalRoutersVrfInnerBgpPeerGroupInnerConnectionOptions.md) |  | [optional] 
**enable** | **bool** |  | [optional] 
**filtering_profile** | [**LogicalRoutersVrfInnerBgpPeerGroupInnerAddressFamily**](LogicalRoutersVrfInnerBgpPeerGroupInnerAddressFamily.md) |  | [optional] 
**name** | **str** |  | 
**peer** | [**List[LogicalRoutersVrfInnerBgpPeerGroupInnerPeerInner]**](LogicalRoutersVrfInnerBgpPeerGroupInnerPeerInner.md) |  | [optional] 
**soft_reset_with_stored_info** | **bool** |  | [optional] 
**type** | [**LogicalRoutersVrfInnerBgpPeerGroupInnerType**](LogicalRoutersVrfInnerBgpPeerGroupInnerType.md) |  | [optional] 

## Example

```python
from scm_network_services.models.logical_routers_vrf_inner_bgp_peer_group_inner import LogicalRoutersVrfInnerBgpPeerGroupInner

# TODO update the JSON string below
json = "{}"
# create an instance of LogicalRoutersVrfInnerBgpPeerGroupInner from a JSON string
logical_routers_vrf_inner_bgp_peer_group_inner_instance = LogicalRoutersVrfInnerBgpPeerGroupInner.from_json(json)
# print the JSON string representation of the object
print(LogicalRoutersVrfInnerBgpPeerGroupInner.to_json())

# convert the object into a dict
logical_routers_vrf_inner_bgp_peer_group_inner_dict = logical_routers_vrf_inner_bgp_peer_group_inner_instance.to_dict()
# create an instance of LogicalRoutersVrfInnerBgpPeerGroupInner from a dict
logical_routers_vrf_inner_bgp_peer_group_inner_from_dict = LogicalRoutersVrfInnerBgpPeerGroupInner.from_dict(logical_routers_vrf_inner_bgp_peer_group_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


