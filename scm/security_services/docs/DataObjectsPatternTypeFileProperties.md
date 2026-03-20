# DataObjectsPatternTypeFileProperties


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pattern** | [**List[DataObjectsPatternTypeFilePropertiesPatternInner]**](DataObjectsPatternTypeFilePropertiesPatternInner.md) |  | [optional] 

## Example

```python
from scm.security_services.models.data_objects_pattern_type_file_properties import DataObjectsPatternTypeFileProperties

# TODO update the JSON string below
json = "{}"
# create an instance of DataObjectsPatternTypeFileProperties from a JSON string
data_objects_pattern_type_file_properties_instance = DataObjectsPatternTypeFileProperties.from_json(json)
# print the JSON string representation of the object
print(DataObjectsPatternTypeFileProperties.to_json())

# convert the object into a dict
data_objects_pattern_type_file_properties_dict = data_objects_pattern_type_file_properties_instance.to_dict()
# create an instance of DataObjectsPatternTypeFileProperties from a dict
data_objects_pattern_type_file_properties_from_dict = DataObjectsPatternTypeFileProperties.from_dict(data_objects_pattern_type_file_properties_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


