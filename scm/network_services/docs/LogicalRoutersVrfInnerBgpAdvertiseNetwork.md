# LogicalRoutersVrfInnerBgpAdvertiseNetwork


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ipv4** | [**LogicalRoutersVrfInnerBgpAdvertiseNetworkIpv4**](LogicalRoutersVrfInnerBgpAdvertiseNetworkIpv4.md) |  | [optional] 
**ipv6** | [**LogicalRoutersVrfInnerBgpAdvertiseNetworkIpv6**](LogicalRoutersVrfInnerBgpAdvertiseNetworkIpv6.md) |  | [optional] 

## Example

```python
from scm.network_services.models.logical_routers_vrf_inner_bgp_advertise_network import LogicalRoutersVrfInnerBgpAdvertiseNetwork

# TODO update the JSON string below
json = "{}"
# create an instance of LogicalRoutersVrfInnerBgpAdvertiseNetwork from a JSON string
logical_routers_vrf_inner_bgp_advertise_network_instance = LogicalRoutersVrfInnerBgpAdvertiseNetwork.from_json(json)
# print the JSON string representation of the object
print(LogicalRoutersVrfInnerBgpAdvertiseNetwork.to_json())

# convert the object into a dict
logical_routers_vrf_inner_bgp_advertise_network_dict = logical_routers_vrf_inner_bgp_advertise_network_instance.to_dict()
# create an instance of LogicalRoutersVrfInnerBgpAdvertiseNetwork from a dict
logical_routers_vrf_inner_bgp_advertise_network_from_dict = LogicalRoutersVrfInnerBgpAdvertiseNetwork.from_dict(logical_routers_vrf_inner_bgp_advertise_network_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


