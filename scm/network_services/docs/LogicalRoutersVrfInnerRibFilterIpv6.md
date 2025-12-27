# LogicalRoutersVrfInnerRibFilterIpv6


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bgp** | [**LogicalRoutersVrfInnerRibFilterIpv4Bgp**](LogicalRoutersVrfInnerRibFilterIpv4Bgp.md) |  | [optional] 
**ospfv3** | [**LogicalRoutersVrfInnerRibFilterIpv4Bgp**](LogicalRoutersVrfInnerRibFilterIpv4Bgp.md) |  | [optional] 
**static** | [**LogicalRoutersVrfInnerRibFilterIpv4Bgp**](LogicalRoutersVrfInnerRibFilterIpv4Bgp.md) |  | [optional] 

## Example

```python
from scm_network_services.models.logical_routers_vrf_inner_rib_filter_ipv6 import LogicalRoutersVrfInnerRibFilterIpv6

# TODO update the JSON string below
json = "{}"
# create an instance of LogicalRoutersVrfInnerRibFilterIpv6 from a JSON string
logical_routers_vrf_inner_rib_filter_ipv6_instance = LogicalRoutersVrfInnerRibFilterIpv6.from_json(json)
# print the JSON string representation of the object
print(LogicalRoutersVrfInnerRibFilterIpv6.to_json())

# convert the object into a dict
logical_routers_vrf_inner_rib_filter_ipv6_dict = logical_routers_vrf_inner_rib_filter_ipv6_instance.to_dict()
# create an instance of LogicalRoutersVrfInnerRibFilterIpv6 from a dict
logical_routers_vrf_inner_rib_filter_ipv6_from_dict = LogicalRoutersVrfInnerRibFilterIpv6.from_dict(logical_routers_vrf_inner_rib_filter_ipv6_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


