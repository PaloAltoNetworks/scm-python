# LogicalRoutersVrfInnerBgpPeerGroupInnerType


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ebgp** | [**LogicalRoutersVrfInnerBgpPeerGroupInnerTypeEbgp**](LogicalRoutersVrfInnerBgpPeerGroupInnerTypeEbgp.md) |  | [optional] 
**ebgp_confed** | [**LogicalRoutersVrfInnerBgpPeerGroupInnerTypeEbgpConfed**](LogicalRoutersVrfInnerBgpPeerGroupInnerTypeEbgpConfed.md) |  | [optional] 
**ibgp** | [**LogicalRoutersVrfInnerBgpPeerGroupInnerTypeEbgpConfed**](LogicalRoutersVrfInnerBgpPeerGroupInnerTypeEbgpConfed.md) |  | [optional] 
**ibgp_confed** | [**LogicalRoutersVrfInnerBgpPeerGroupInnerTypeEbgpConfed**](LogicalRoutersVrfInnerBgpPeerGroupInnerTypeEbgpConfed.md) |  | [optional] 

## Example

```python
from scm.network_services.models.logical_routers_vrf_inner_bgp_peer_group_inner_type import LogicalRoutersVrfInnerBgpPeerGroupInnerType

# TODO update the JSON string below
json = "{}"
# create an instance of LogicalRoutersVrfInnerBgpPeerGroupInnerType from a JSON string
logical_routers_vrf_inner_bgp_peer_group_inner_type_instance = LogicalRoutersVrfInnerBgpPeerGroupInnerType.from_json(json)
# print the JSON string representation of the object
print(LogicalRoutersVrfInnerBgpPeerGroupInnerType.to_json())

# convert the object into a dict
logical_routers_vrf_inner_bgp_peer_group_inner_type_dict = logical_routers_vrf_inner_bgp_peer_group_inner_type_instance.to_dict()
# create an instance of LogicalRoutersVrfInnerBgpPeerGroupInnerType from a dict
logical_routers_vrf_inner_bgp_peer_group_inner_type_from_dict = LogicalRoutersVrfInnerBgpPeerGroupInnerType.from_dict(logical_routers_vrf_inner_bgp_peer_group_inner_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


