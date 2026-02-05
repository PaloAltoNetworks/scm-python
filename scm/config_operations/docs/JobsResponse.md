# JobsResponse

Response containing job data

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[Jobs]**](Jobs.md) |  | [optional] 

## Example

```python
from scm.config_operations.models.jobs_response import JobsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of JobsResponse from a JSON string
jobs_response_instance = JobsResponse.from_json(json)
# print the JSON string representation of the object
print(JobsResponse.to_json())

# convert the object into a dict
jobs_response_dict = jobs_response_instance.to_dict()
# create an instance of JobsResponse from a dict
jobs_response_from_dict = JobsResponse.from_dict(jobs_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


