# JobsListResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[Jobs]**](Jobs.md) |  | 
**limit** | **int** | The maximum number of results per page | [default to 200]
**offset** | **int** | The offset into the list of results returned | [default to 0]
**total** | **int** | The total count of results | 

## Example

```python
from scm.config_operations.models.jobs_list_response import JobsListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of JobsListResponse from a JSON string
jobs_list_response_instance = JobsListResponse.from_json(json)
# print the JSON string representation of the object
print(JobsListResponse.to_json())

# convert the object into a dict
jobs_list_response_dict = jobs_list_response_instance.to_dict()
# create an instance of JobsListResponse from a dict
jobs_list_response_from_dict = JobsListResponse.from_dict(jobs_list_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


