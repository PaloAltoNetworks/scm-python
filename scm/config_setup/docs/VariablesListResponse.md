# VariablesListResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[Variables]**](Variables.md) |  | 
**limit** | **int** | The maximum number of results per page | [default to 200]
**offset** | **int** | The offset into the list of results returned | [default to 0]
**total** | **int** | The total count of results | 

## Example

```python
from scm.config_setup.models.variables_list_response import VariablesListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of VariablesListResponse from a JSON string
variables_list_response_instance = VariablesListResponse.from_json(json)
# print the JSON string representation of the object
print(VariablesListResponse.to_json())

# convert the object into a dict
variables_list_response_dict = variables_list_response_instance.to_dict()
# create an instance of VariablesListResponse from a dict
variables_list_response_from_dict = VariablesListResponse.from_dict(variables_list_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


