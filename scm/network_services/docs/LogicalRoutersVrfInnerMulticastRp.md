# LogicalRoutersVrfInnerMulticastRp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**external_rp** | [**List[LogicalRoutersVrfInnerMulticastRpExternalRpInner]**](LogicalRoutersVrfInnerMulticastRpExternalRpInner.md) |  | [optional] 
**local_rp** | [**LogicalRoutersVrfInnerMulticastRpLocalRp**](LogicalRoutersVrfInnerMulticastRpLocalRp.md) |  | [optional] 

## Example

```python
from scm_network_services.models.logical_routers_vrf_inner_multicast_rp import LogicalRoutersVrfInnerMulticastRp

# TODO update the JSON string below
json = "{}"
# create an instance of LogicalRoutersVrfInnerMulticastRp from a JSON string
logical_routers_vrf_inner_multicast_rp_instance = LogicalRoutersVrfInnerMulticastRp.from_json(json)
# print the JSON string representation of the object
print(LogicalRoutersVrfInnerMulticastRp.to_json())

# convert the object into a dict
logical_routers_vrf_inner_multicast_rp_dict = logical_routers_vrf_inner_multicast_rp_instance.to_dict()
# create an instance of LogicalRoutersVrfInnerMulticastRp from a dict
logical_routers_vrf_inner_multicast_rp_from_dict = LogicalRoutersVrfInnerMulticastRp.from_dict(logical_routers_vrf_inner_multicast_rp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


