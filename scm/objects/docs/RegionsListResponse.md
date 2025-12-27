# RegionsListResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[Regions]**](Regions.md) |  | 
**limit** | **int** | The maximum number of results per page | [default to 200]
**offset** | **int** | The offset into the list of results returned | [default to 0]
**total** | **int** | The total count of results | 

## Example

```python
from scm_objects.models.regions_list_response import RegionsListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of RegionsListResponse from a JSON string
regions_list_response_instance = RegionsListResponse.from_json(json)
# print the JSON string representation of the object
print(RegionsListResponse.to_json())

# convert the object into a dict
regions_list_response_dict = regions_list_response_instance.to_dict()
# create an instance of RegionsListResponse from a dict
regions_list_response_from_dict = RegionsListResponse.from_dict(regions_list_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


