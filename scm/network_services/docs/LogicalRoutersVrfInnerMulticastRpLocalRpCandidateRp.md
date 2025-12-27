# LogicalRoutersVrfInnerMulticastRpLocalRpCandidateRp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | **str** |  | [optional] 
**advertisement_interval** | **int** |  | [optional] 
**group_addresses** | **List[str]** |  | [optional] 
**interface** | **str** |  | [optional] 
**priority** | **int** |  | [optional] 

## Example

```python
from scm_network_services.models.logical_routers_vrf_inner_multicast_rp_local_rp_candidate_rp import LogicalRoutersVrfInnerMulticastRpLocalRpCandidateRp

# TODO update the JSON string below
json = "{}"
# create an instance of LogicalRoutersVrfInnerMulticastRpLocalRpCandidateRp from a JSON string
logical_routers_vrf_inner_multicast_rp_local_rp_candidate_rp_instance = LogicalRoutersVrfInnerMulticastRpLocalRpCandidateRp.from_json(json)
# print the JSON string representation of the object
print(LogicalRoutersVrfInnerMulticastRpLocalRpCandidateRp.to_json())

# convert the object into a dict
logical_routers_vrf_inner_multicast_rp_local_rp_candidate_rp_dict = logical_routers_vrf_inner_multicast_rp_local_rp_candidate_rp_instance.to_dict()
# create an instance of LogicalRoutersVrfInnerMulticastRpLocalRpCandidateRp from a dict
logical_routers_vrf_inner_multicast_rp_local_rp_candidate_rp_from_dict = LogicalRoutersVrfInnerMulticastRpLocalRpCandidateRp.from_dict(logical_routers_vrf_inner_multicast_rp_local_rp_candidate_rp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


