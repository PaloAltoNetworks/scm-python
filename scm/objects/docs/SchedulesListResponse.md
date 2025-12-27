# SchedulesListResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[Schedules]**](Schedules.md) |  | 
**limit** | **int** | The maximum number of results per page | [default to 200]
**offset** | **int** | The offset into the list of results returned | [default to 0]
**total** | **int** | The total count of results | 

## Example

```python
from scm_objects.models.schedules_list_response import SchedulesListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SchedulesListResponse from a JSON string
schedules_list_response_instance = SchedulesListResponse.from_json(json)
# print the JSON string representation of the object
print(SchedulesListResponse.to_json())

# convert the object into a dict
schedules_list_response_dict = schedules_list_response_instance.to_dict()
# create an instance of SchedulesListResponse from a dict
schedules_list_response_from_dict = SchedulesListResponse.from_dict(schedules_list_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


