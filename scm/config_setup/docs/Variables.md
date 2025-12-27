# Variables


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | The description of the variable | [optional] 
**device** | **str** | The device in which the resource is defined | [optional] 
**folder** | **str** | The folder in which the resource is defined | [optional] 
**id** | **str** | UUID of the variable | [readonly] 
**name** | **str** | The name of the variable | 
**overridden** | **bool** | Is the variable overridden? | [optional] [readonly] 
**snippet** | **str** | The snippet in which the resource is defined | [optional] 
**type** | **str** | The variable type | 
**value** | **object** | The value of the variable | 

## Example

```python
from scm.config_setup.models.variables import Variables

# TODO update the JSON string below
json = "{}"
# create an instance of Variables from a JSON string
variables_instance = Variables.from_json(json)
# print the JSON string representation of the object
print(Variables.to_json())

# convert the object into a dict
variables_dict = variables_instance.to_dict()
# create an instance of Variables from a dict
variables_from_dict = Variables.from_dict(variables_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


