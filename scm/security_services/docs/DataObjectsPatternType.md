# DataObjectsPatternType


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**file_properties** | [**DataObjectsPatternTypeFileProperties**](DataObjectsPatternTypeFileProperties.md) |  | [optional] 
**predefined** | [**DataObjectsPatternTypePredefined**](DataObjectsPatternTypePredefined.md) |  | [optional] 
**regex** | [**DataObjectsPatternTypeRegex**](DataObjectsPatternTypeRegex.md) |  | [optional] 

## Example

```python
from scm.security_services.models.data_objects_pattern_type import DataObjectsPatternType

# TODO update the JSON string below
json = "{}"
# create an instance of DataObjectsPatternType from a JSON string
data_objects_pattern_type_instance = DataObjectsPatternType.from_json(json)
# print the JSON string representation of the object
print(DataObjectsPatternType.to_json())

# convert the object into a dict
data_objects_pattern_type_dict = data_objects_pattern_type_instance.to_dict()
# create an instance of DataObjectsPatternType from a dict
data_objects_pattern_type_from_dict = DataObjectsPatternType.from_dict(data_objects_pattern_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


