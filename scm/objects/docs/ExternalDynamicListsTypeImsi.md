# ExternalDynamicListsTypeImsi

IMSI Config for Custom IMSI type

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**auth** | [**ExternalDynamicListsTypeImsiAuth**](ExternalDynamicListsTypeImsiAuth.md) |  | [optional] 
**certificate_profile** | **str** | IMSI Certificate Profile for Custom IMSI type | [optional] [default to 'None']
**description** | **str** | IMSI Description for Custom IMSI type | [optional] 
**exception_list** | **List[str]** | IMSI Exception List for Custom IMSI type | [optional] 
**recurring** | [**ExternalDynamicListsTypeImsiRecurring**](ExternalDynamicListsTypeImsiRecurring.md) |  | 
**url** | **str** | IMSI URL for Custom IMSI type | [default to 'http://']

## Example

```python
from scm_objects.models.external_dynamic_lists_type_imsi import ExternalDynamicListsTypeImsi

# TODO update the JSON string below
json = "{}"
# create an instance of ExternalDynamicListsTypeImsi from a JSON string
external_dynamic_lists_type_imsi_instance = ExternalDynamicListsTypeImsi.from_json(json)
# print the JSON string representation of the object
print(ExternalDynamicListsTypeImsi.to_json())

# convert the object into a dict
external_dynamic_lists_type_imsi_dict = external_dynamic_lists_type_imsi_instance.to_dict()
# create an instance of ExternalDynamicListsTypeImsi from a dict
external_dynamic_lists_type_imsi_from_dict = ExternalDynamicListsTypeImsi.from_dict(external_dynamic_lists_type_imsi_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


