# ExternalDynamicListsType

Type configuration for External Dynamic List

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**domain** | [**ExternalDynamicListsTypeDomain**](ExternalDynamicListsTypeDomain.md) |  | [optional] 
**imei** | [**ExternalDynamicListsTypeImei**](ExternalDynamicListsTypeImei.md) |  | [optional] 
**imsi** | [**ExternalDynamicListsTypeImsi**](ExternalDynamicListsTypeImsi.md) |  | [optional] 
**ip** | [**ExternalDynamicListsTypeIp**](ExternalDynamicListsTypeIp.md) |  | [optional] 
**predefined_ip** | [**ExternalDynamicListsTypePredefinedIp**](ExternalDynamicListsTypePredefinedIp.md) |  | [optional] 
**predefined_url** | [**ExternalDynamicListsTypePredefinedUrl**](ExternalDynamicListsTypePredefinedUrl.md) |  | [optional] 
**url** | [**ExternalDynamicListsTypeUrl**](ExternalDynamicListsTypeUrl.md) |  | [optional] 

## Example

```python
from scm_objects.models.external_dynamic_lists_type import ExternalDynamicListsType

# TODO update the JSON string below
json = "{}"
# create an instance of ExternalDynamicListsType from a JSON string
external_dynamic_lists_type_instance = ExternalDynamicListsType.from_json(json)
# print the JSON string representation of the object
print(ExternalDynamicListsType.to_json())

# convert the object into a dict
external_dynamic_lists_type_dict = external_dynamic_lists_type_instance.to_dict()
# create an instance of ExternalDynamicListsType from a dict
external_dynamic_lists_type_from_dict = ExternalDynamicListsType.from_dict(external_dynamic_lists_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


