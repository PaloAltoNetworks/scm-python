# RunningConfigVersionsResponse

Paginated response containing running configuration versions

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[RunningVersions]**](RunningVersions.md) |  | [optional] 
**limit** | **int** |  | [optional] 
**offset** | **int** |  | [optional] 
**total** | **int** |  | [optional] 

## Example

```python
from scm.config_operations.models.running_config_versions_response import RunningConfigVersionsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of RunningConfigVersionsResponse from a JSON string
running_config_versions_response_instance = RunningConfigVersionsResponse.from_json(json)
# print the JSON string representation of the object
print(RunningConfigVersionsResponse.to_json())

# convert the object into a dict
running_config_versions_response_dict = running_config_versions_response_instance.to_dict()
# create an instance of RunningConfigVersionsResponse from a dict
running_config_versions_response_from_dict = RunningConfigVersionsResponse.from_dict(running_config_versions_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


