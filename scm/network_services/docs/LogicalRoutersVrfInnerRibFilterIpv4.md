# LogicalRoutersVrfInnerRibFilterIpv4


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bgp** | [**LogicalRoutersVrfInnerRibFilterIpv4Bgp**](LogicalRoutersVrfInnerRibFilterIpv4Bgp.md) |  | [optional] 
**ospf** | [**LogicalRoutersVrfInnerRibFilterIpv4Bgp**](LogicalRoutersVrfInnerRibFilterIpv4Bgp.md) |  | [optional] 
**rip** | [**LogicalRoutersVrfInnerRibFilterIpv4Bgp**](LogicalRoutersVrfInnerRibFilterIpv4Bgp.md) |  | [optional] 
**static** | [**LogicalRoutersVrfInnerRibFilterIpv4Bgp**](LogicalRoutersVrfInnerRibFilterIpv4Bgp.md) |  | [optional] 

## Example

```python
from scm.network_services.models.logical_routers_vrf_inner_rib_filter_ipv4 import LogicalRoutersVrfInnerRibFilterIpv4

# TODO update the JSON string below
json = "{}"
# create an instance of LogicalRoutersVrfInnerRibFilterIpv4 from a JSON string
logical_routers_vrf_inner_rib_filter_ipv4_instance = LogicalRoutersVrfInnerRibFilterIpv4.from_json(json)
# print the JSON string representation of the object
print(LogicalRoutersVrfInnerRibFilterIpv4.to_json())

# convert the object into a dict
logical_routers_vrf_inner_rib_filter_ipv4_dict = logical_routers_vrf_inner_rib_filter_ipv4_instance.to_dict()
# create an instance of LogicalRoutersVrfInnerRibFilterIpv4 from a dict
logical_routers_vrf_inner_rib_filter_ipv4_from_dict = LogicalRoutersVrfInnerRibFilterIpv4.from_dict(logical_routers_vrf_inner_rib_filter_ipv4_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


