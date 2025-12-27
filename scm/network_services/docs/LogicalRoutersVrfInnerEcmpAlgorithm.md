# LogicalRoutersVrfInnerEcmpAlgorithm


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**balanced_round_robin** | **object** |  | [optional] 
**ip_hash** | [**LogicalRoutersVrfInnerEcmpAlgorithmIpHash**](LogicalRoutersVrfInnerEcmpAlgorithmIpHash.md) |  | [optional] 
**ip_modulo** | **object** |  | [optional] 
**weighted_round_robin** | [**LogicalRoutersVrfInnerEcmpAlgorithmWeightedRoundRobin**](LogicalRoutersVrfInnerEcmpAlgorithmWeightedRoundRobin.md) |  | [optional] 

## Example

```python
from scm_network_services.models.logical_routers_vrf_inner_ecmp_algorithm import LogicalRoutersVrfInnerEcmpAlgorithm

# TODO update the JSON string below
json = "{}"
# create an instance of LogicalRoutersVrfInnerEcmpAlgorithm from a JSON string
logical_routers_vrf_inner_ecmp_algorithm_instance = LogicalRoutersVrfInnerEcmpAlgorithm.from_json(json)
# print the JSON string representation of the object
print(LogicalRoutersVrfInnerEcmpAlgorithm.to_json())

# convert the object into a dict
logical_routers_vrf_inner_ecmp_algorithm_dict = logical_routers_vrf_inner_ecmp_algorithm_instance.to_dict()
# create an instance of LogicalRoutersVrfInnerEcmpAlgorithm from a dict
logical_routers_vrf_inner_ecmp_algorithm_from_dict = LogicalRoutersVrfInnerEcmpAlgorithm.from_dict(logical_routers_vrf_inner_ecmp_algorithm_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


