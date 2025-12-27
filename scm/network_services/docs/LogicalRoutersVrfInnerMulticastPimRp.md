# LogicalRoutersVrfInnerMulticastPimRp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**external_rp** | [**List[LogicalRoutersVrfInnerMulticastPimRpExternalRpInner]**](LogicalRoutersVrfInnerMulticastPimRpExternalRpInner.md) |  | [optional] 
**local_rp** | [**LogicalRoutersVrfInnerMulticastPimRpLocalRp**](LogicalRoutersVrfInnerMulticastPimRpLocalRp.md) |  | [optional] 

## Example

```python
from scm.network_services.models.logical_routers_vrf_inner_multicast_pim_rp import LogicalRoutersVrfInnerMulticastPimRp

# TODO update the JSON string below
json = "{}"
# create an instance of LogicalRoutersVrfInnerMulticastPimRp from a JSON string
logical_routers_vrf_inner_multicast_pim_rp_instance = LogicalRoutersVrfInnerMulticastPimRp.from_json(json)
# print the JSON string representation of the object
print(LogicalRoutersVrfInnerMulticastPimRp.to_json())

# convert the object into a dict
logical_routers_vrf_inner_multicast_pim_rp_dict = logical_routers_vrf_inner_multicast_pim_rp_instance.to_dict()
# create an instance of LogicalRoutersVrfInnerMulticastPimRp from a dict
logical_routers_vrf_inner_multicast_pim_rp_from_dict = LogicalRoutersVrfInnerMulticastPimRp.from_dict(logical_routers_vrf_inner_multicast_pim_rp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


