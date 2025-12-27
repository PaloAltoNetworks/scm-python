# LogicalRoutersVrfInnerEcmpAlgorithmIpHash


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hash_seed** | **int** |  | [optional] 
**src_only** | **bool** |  | [optional] 
**use_port** | **bool** |  | [optional] 

## Example

```python
from scm_network_services.models.logical_routers_vrf_inner_ecmp_algorithm_ip_hash import LogicalRoutersVrfInnerEcmpAlgorithmIpHash

# TODO update the JSON string below
json = "{}"
# create an instance of LogicalRoutersVrfInnerEcmpAlgorithmIpHash from a JSON string
logical_routers_vrf_inner_ecmp_algorithm_ip_hash_instance = LogicalRoutersVrfInnerEcmpAlgorithmIpHash.from_json(json)
# print the JSON string representation of the object
print(LogicalRoutersVrfInnerEcmpAlgorithmIpHash.to_json())

# convert the object into a dict
logical_routers_vrf_inner_ecmp_algorithm_ip_hash_dict = logical_routers_vrf_inner_ecmp_algorithm_ip_hash_instance.to_dict()
# create an instance of LogicalRoutersVrfInnerEcmpAlgorithmIpHash from a dict
logical_routers_vrf_inner_ecmp_algorithm_ip_hash_from_dict = LogicalRoutersVrfInnerEcmpAlgorithmIpHash.from_dict(logical_routers_vrf_inner_ecmp_algorithm_ip_hash_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


