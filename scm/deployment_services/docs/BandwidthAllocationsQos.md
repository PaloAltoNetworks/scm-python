# BandwidthAllocationsQos


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**customized** | **bool** |  | [optional] [default to False]
**enabled** | **bool** |  | [optional] [default to False]
**guaranteed_ratio** | **float** |  | [optional] [default to 0]
**profile** | **str** |  | [optional] [default to '']

## Example

```python
from scm.deployment_services.models.bandwidth_allocations_qos import BandwidthAllocationsQos

# TODO update the JSON string below
json = "{}"
# create an instance of BandwidthAllocationsQos from a JSON string
bandwidth_allocations_qos_instance = BandwidthAllocationsQos.from_json(json)
# print the JSON string representation of the object
print(BandwidthAllocationsQos.to_json())

# convert the object into a dict
bandwidth_allocations_qos_dict = bandwidth_allocations_qos_instance.to_dict()
# create an instance of BandwidthAllocationsQos from a dict
bandwidth_allocations_qos_from_dict = BandwidthAllocationsQos.from_dict(bandwidth_allocations_qos_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


