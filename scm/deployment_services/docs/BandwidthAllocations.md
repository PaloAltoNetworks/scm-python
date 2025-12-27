# BandwidthAllocations


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allocated_bandwidth** | **int** | bandwidth to allocate in Mbps | 
**name** | **str** | name of the aggregated bandwidth region | 
**qos** | [**BandwidthAllocationsQos**](BandwidthAllocationsQos.md) |  | [optional] 
**spn_name_list** | **List[str]** |  | [optional] [default to []]

## Example

```python
from scm_deployment_services.models.bandwidth_allocations import BandwidthAllocations

# TODO update the JSON string below
json = "{}"
# create an instance of BandwidthAllocations from a JSON string
bandwidth_allocations_instance = BandwidthAllocations.from_json(json)
# print the JSON string representation of the object
print(BandwidthAllocations.to_json())

# convert the object into a dict
bandwidth_allocations_dict = bandwidth_allocations_instance.to_dict()
# create an instance of BandwidthAllocations from a dict
bandwidth_allocations_from_dict = BandwidthAllocations.from_dict(bandwidth_allocations_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


