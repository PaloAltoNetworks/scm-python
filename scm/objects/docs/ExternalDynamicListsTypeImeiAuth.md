# ExternalDynamicListsTypeImeiAuth

IMEI Auth Cnfig for Custom IMEI type

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**password** | **str** | IMEI Auth Password for Custom IMEI type | 
**username** | **str** | IMEI Auth username for Custom IMEI type | 

## Example

```python
from scm_objects.models.external_dynamic_lists_type_imei_auth import ExternalDynamicListsTypeImeiAuth

# TODO update the JSON string below
json = "{}"
# create an instance of ExternalDynamicListsTypeImeiAuth from a JSON string
external_dynamic_lists_type_imei_auth_instance = ExternalDynamicListsTypeImeiAuth.from_json(json)
# print the JSON string representation of the object
print(ExternalDynamicListsTypeImeiAuth.to_json())

# convert the object into a dict
external_dynamic_lists_type_imei_auth_dict = external_dynamic_lists_type_imei_auth_instance.to_dict()
# create an instance of ExternalDynamicListsTypeImeiAuth from a dict
external_dynamic_lists_type_imei_auth_from_dict = ExternalDynamicListsTypeImeiAuth.from_dict(external_dynamic_lists_type_imei_auth_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


