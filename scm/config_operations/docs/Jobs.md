# Jobs


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | A description provided by the administrator or service account | [optional] 
**details** | **str** | JSON string with detailed errors or info | [optional] 
**device_name** | **str** | The name of the device | 
**end_ts** | **str** | The timestamp indicating when the job was finished | 
**id** | **str** | The job ID | 
**job_result** | **str** | The job result | 
**job_status** | **str** | The current status of the job | 
**job_type** | **str** | The job type | 
**parent_id** | **str** | The parent job ID | 
**percent** | **str** | Job completion percentage | 
**result_str** | **str** | The result of the job | 
**start_ts** | **str** | The timestamp indicating when the job was created | 
**status_str** | **str** | The current status of the job | 
**summary** | **str** | The completion summary of the job | 
**type_str** | **str** | The job type | 
**uname** | **str** | The administrator or service account that created the job | 

## Example

```python
from scm.config_operations.models.jobs import Jobs

# TODO update the JSON string below
json = "{}"
# create an instance of Jobs from a JSON string
jobs_instance = Jobs.from_json(json)
# print the JSON string representation of the object
print(Jobs.to_json())

# convert the object into a dict
jobs_dict = jobs_instance.to_dict()
# create an instance of Jobs from a dict
jobs_from_dict = Jobs.from_dict(jobs_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


