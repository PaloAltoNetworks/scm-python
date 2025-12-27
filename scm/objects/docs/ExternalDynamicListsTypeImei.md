# ExternalDynamicListsTypeImei

IMEI Configuration settings

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**auth** | [**ExternalDynamicListsTypeImeiAuth**](ExternalDynamicListsTypeImeiAuth.md) |  | [optional] 
**certificate_profile** | **str** | IMEI Certificate Profile for Custom IMEI type | [optional] [default to 'None']
**description** | **str** | IMEI Description for Custom IMEI type | [optional] 
**exception_list** | **List[str]** | IMEI Exception List for Custom IMEI type | [optional] 
**recurring** | [**ExternalDynamicListsTypeImeiRecurring**](ExternalDynamicListsTypeImeiRecurring.md) |  | 
**url** | **str** | IMEI URL for Custom IMEI type | [default to 'http://']

## Example

```python
from scm_objects.models.external_dynamic_lists_type_imei import ExternalDynamicListsTypeImei

# TODO update the JSON string below
json = "{}"
# create an instance of ExternalDynamicListsTypeImei from a JSON string
external_dynamic_lists_type_imei_instance = ExternalDynamicListsTypeImei.from_json(json)
# print the JSON string representation of the object
print(ExternalDynamicListsTypeImei.to_json())

# convert the object into a dict
external_dynamic_lists_type_imei_dict = external_dynamic_lists_type_imei_instance.to_dict()
# create an instance of ExternalDynamicListsTypeImei from a dict
external_dynamic_lists_type_imei_from_dict = ExternalDynamicListsTypeImei.from_dict(external_dynamic_lists_type_imei_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


