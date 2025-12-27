# BandwidthAllocationsListResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[BandwidthAllocations]**](BandwidthAllocations.md) |  | 
**limit** | **int** | The maximum number of results per page | [default to 200]
**offset** | **int** | The offset into the list of results returned | [default to 0]
**total** | **int** | The total count of results | 

## Example

```python
from scm_deployment_services.models.bandwidth_allocations_list_response import BandwidthAllocationsListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of BandwidthAllocationsListResponse from a JSON string
bandwidth_allocations_list_response_instance = BandwidthAllocationsListResponse.from_json(json)
# print the JSON string representation of the object
print(BandwidthAllocationsListResponse.to_json())

# convert the object into a dict
bandwidth_allocations_list_response_dict = bandwidth_allocations_list_response_instance.to_dict()
# create an instance of BandwidthAllocationsListResponse from a dict
bandwidth_allocations_list_response_from_dict = BandwidthAllocationsListResponse.from_dict(bandwidth_allocations_list_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


