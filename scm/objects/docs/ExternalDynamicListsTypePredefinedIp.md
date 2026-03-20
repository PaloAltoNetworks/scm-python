# ExternalDynamicListsTypePredefinedIp

Predefined IP settings for EDL type

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** |  | [optional] 
**exception_list** | **List[str]** | IP Exception List for Predefined IP type | [optional] 
**url** | **str** | URL source for Predefined IP type | 

## Example

```python
from scm.objects.models.external_dynamic_lists_type_predefined_ip import ExternalDynamicListsTypePredefinedIp

# TODO update the JSON string below
json = "{}"
# create an instance of ExternalDynamicListsTypePredefinedIp from a JSON string
external_dynamic_lists_type_predefined_ip_instance = ExternalDynamicListsTypePredefinedIp.from_json(json)
# print the JSON string representation of the object
print(ExternalDynamicListsTypePredefinedIp.to_json())

# convert the object into a dict
external_dynamic_lists_type_predefined_ip_dict = external_dynamic_lists_type_predefined_ip_instance.to_dict()
# create an instance of ExternalDynamicListsTypePredefinedIp from a dict
external_dynamic_lists_type_predefined_ip_from_dict = ExternalDynamicListsTypePredefinedIp.from_dict(external_dynamic_lists_type_predefined_ip_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


