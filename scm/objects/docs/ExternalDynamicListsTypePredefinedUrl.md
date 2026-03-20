# ExternalDynamicListsTypePredefinedUrl

Predefined URL settings for EDL type

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** |  | [optional] 
**exception_list** | **List[str]** | URL Exception List for Predefined URL type | [optional] 
**url** | **str** | URL source for Predefined URL type | 

## Example

```python
from scm.objects.models.external_dynamic_lists_type_predefined_url import ExternalDynamicListsTypePredefinedUrl

# TODO update the JSON string below
json = "{}"
# create an instance of ExternalDynamicListsTypePredefinedUrl from a JSON string
external_dynamic_lists_type_predefined_url_instance = ExternalDynamicListsTypePredefinedUrl.from_json(json)
# print the JSON string representation of the object
print(ExternalDynamicListsTypePredefinedUrl.to_json())

# convert the object into a dict
external_dynamic_lists_type_predefined_url_dict = external_dynamic_lists_type_predefined_url_instance.to_dict()
# create an instance of ExternalDynamicListsTypePredefinedUrl from a dict
external_dynamic_lists_type_predefined_url_from_dict = ExternalDynamicListsTypePredefinedUrl.from_dict(external_dynamic_lists_type_predefined_url_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


