# LogicalRoutersVrfInnerRibFilter


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ipv4** | [**LogicalRoutersVrfInnerRibFilterIpv4**](LogicalRoutersVrfInnerRibFilterIpv4.md) |  | [optional] 
**ipv6** | [**LogicalRoutersVrfInnerRibFilterIpv6**](LogicalRoutersVrfInnerRibFilterIpv6.md) |  | [optional] 

## Example

```python
from scm_network_services.models.logical_routers_vrf_inner_rib_filter import LogicalRoutersVrfInnerRibFilter

# TODO update the JSON string below
json = "{}"
# create an instance of LogicalRoutersVrfInnerRibFilter from a JSON string
logical_routers_vrf_inner_rib_filter_instance = LogicalRoutersVrfInnerRibFilter.from_json(json)
# print the JSON string representation of the object
print(LogicalRoutersVrfInnerRibFilter.to_json())

# convert the object into a dict
logical_routers_vrf_inner_rib_filter_dict = logical_routers_vrf_inner_rib_filter_instance.to_dict()
# create an instance of LogicalRoutersVrfInnerRibFilter from a dict
logical_routers_vrf_inner_rib_filter_from_dict = LogicalRoutersVrfInnerRibFilter.from_dict(logical_routers_vrf_inner_rib_filter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


