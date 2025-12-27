# LogicalRoutersVrfInnerEcmp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**algorithm** | [**LogicalRoutersVrfInnerEcmpAlgorithm**](LogicalRoutersVrfInnerEcmpAlgorithm.md) |  | [optional] 
**enable** | **bool** |  | [optional] 
**max_path** | **int** |  | [optional] 
**strict_source_path** | **bool** |  | [optional] 
**symmetric_return** | **bool** |  | [optional] 

## Example

```python
from scm.network_services.models.logical_routers_vrf_inner_ecmp import LogicalRoutersVrfInnerEcmp

# TODO update the JSON string below
json = "{}"
# create an instance of LogicalRoutersVrfInnerEcmp from a JSON string
logical_routers_vrf_inner_ecmp_instance = LogicalRoutersVrfInnerEcmp.from_json(json)
# print the JSON string representation of the object
print(LogicalRoutersVrfInnerEcmp.to_json())

# convert the object into a dict
logical_routers_vrf_inner_ecmp_dict = logical_routers_vrf_inner_ecmp_instance.to_dict()
# create an instance of LogicalRoutersVrfInnerEcmp from a dict
logical_routers_vrf_inner_ecmp_from_dict = LogicalRoutersVrfInnerEcmp.from_dict(logical_routers_vrf_inner_ecmp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


