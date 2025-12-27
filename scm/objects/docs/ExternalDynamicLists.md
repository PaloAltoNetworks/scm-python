# ExternalDynamicLists

External Dynamic Lists

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**device** | **str** | The device in which the resource is defined | [optional] 
**folder** | **str** | The folder in which the resource is defined | [optional] 
**id** | **str** | The UUID of the external dynamic list | [optional] [readonly] 
**name** | **str** | The name of the external dynamic list | 
**snippet** | **str** | The snippet in which the resource is defined | [optional] 
**type** | [**ExternalDynamicListsType**](ExternalDynamicListsType.md) |  | [optional] 

## Example

```python
from scm_objects.models.external_dynamic_lists import ExternalDynamicLists

# TODO update the JSON string below
json = "{}"
# create an instance of ExternalDynamicLists from a JSON string
external_dynamic_lists_instance = ExternalDynamicLists.from_json(json)
# print the JSON string representation of the object
print(ExternalDynamicLists.to_json())

# convert the object into a dict
external_dynamic_lists_dict = external_dynamic_lists_instance.to_dict()
# create an instance of ExternalDynamicLists from a dict
external_dynamic_lists_from_dict = ExternalDynamicLists.from_dict(external_dynamic_lists_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


