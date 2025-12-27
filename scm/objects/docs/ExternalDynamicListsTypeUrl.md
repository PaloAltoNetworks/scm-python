# ExternalDynamicListsTypeUrl

URL settings for Custom URL type

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**auth** | [**ExternalDynamicListsTypeUrlAuth**](ExternalDynamicListsTypeUrlAuth.md) |  | [optional] 
**certificate_profile** | **str** | Profile for authenticating client certificates | [optional] [default to 'None']
**description** | **str** |  | [optional] 
**exception_list** | **List[str]** | URL Exception List for Custom URL type | [optional] 
**recurring** | [**ExternalDynamicListsTypeUrlRecurring**](ExternalDynamicListsTypeUrlRecurring.md) |  | 
**url** | **str** | External URL for Custom URL type | [default to 'http://']

## Example

```python
from scm.objects.models.external_dynamic_lists_type_url import ExternalDynamicListsTypeUrl

# TODO update the JSON string below
json = "{}"
# create an instance of ExternalDynamicListsTypeUrl from a JSON string
external_dynamic_lists_type_url_instance = ExternalDynamicListsTypeUrl.from_json(json)
# print the JSON string representation of the object
print(ExternalDynamicListsTypeUrl.to_json())

# convert the object into a dict
external_dynamic_lists_type_url_dict = external_dynamic_lists_type_url_instance.to_dict()
# create an instance of ExternalDynamicListsTypeUrl from a dict
external_dynamic_lists_type_url_from_dict = ExternalDynamicListsTypeUrl.from_dict(external_dynamic_lists_type_url_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


