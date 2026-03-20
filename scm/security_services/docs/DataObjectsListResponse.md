# DataObjectsListResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[DataObjects]**](DataObjects.md) |  | 
**limit** | **int** | The maximum number of results per page | [default to 200]
**offset** | **int** | The offset into the list of results returned | [default to 0]
**total** | **int** | The total count of results | 

## Example

```python
from scm.security_services.models.data_objects_list_response import DataObjectsListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DataObjectsListResponse from a JSON string
data_objects_list_response_instance = DataObjectsListResponse.from_json(json)
# print the JSON string representation of the object
print(DataObjectsListResponse.to_json())

# convert the object into a dict
data_objects_list_response_dict = data_objects_list_response_instance.to_dict()
# create an instance of DataObjectsListResponse from a dict
data_objects_list_response_from_dict = DataObjectsListResponse.from_dict(data_objects_list_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


