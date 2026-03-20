# DataObjects


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | The description of the data object | [optional] 
**device** | **str** | The device in which the resource is defined | [optional] 
**disable_override** | **str** |  | [optional] 
**folder** | **str** | The folder in which the resource is defined | [optional] 
**id** | **str** | The UUID of the data object | [optional] [readonly] 
**name** | **str** | The name of the data object | [optional] 
**pattern_type** | [**DataObjectsPatternType**](DataObjectsPatternType.md) |  | [optional] 
**snippet** | **str** | The snippet in which the resource is defined | [optional] 

## Example

```python
from scm.security_services.models.data_objects import DataObjects

# TODO update the JSON string below
json = "{}"
# create an instance of DataObjects from a JSON string
data_objects_instance = DataObjects.from_json(json)
# print the JSON string representation of the object
print(DataObjects.to_json())

# convert the object into a dict
data_objects_dict = data_objects_instance.to_dict()
# create an instance of DataObjects from a dict
data_objects_from_dict = DataObjects.from_dict(data_objects_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


