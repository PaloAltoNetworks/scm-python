# ExternalDynamicListsTypeImsiAuth

IMSI Auth Config for Custom IMSI type

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**password** | **str** | IMSI Auth Password for Custom IMSI type | 
**username** | **str** | IMSI Auth Username for Custom IMSI type | 

## Example

```python
from scm_objects.models.external_dynamic_lists_type_imsi_auth import ExternalDynamicListsTypeImsiAuth

# TODO update the JSON string below
json = "{}"
# create an instance of ExternalDynamicListsTypeImsiAuth from a JSON string
external_dynamic_lists_type_imsi_auth_instance = ExternalDynamicListsTypeImsiAuth.from_json(json)
# print the JSON string representation of the object
print(ExternalDynamicListsTypeImsiAuth.to_json())

# convert the object into a dict
external_dynamic_lists_type_imsi_auth_dict = external_dynamic_lists_type_imsi_auth_instance.to_dict()
# create an instance of ExternalDynamicListsTypeImsiAuth from a dict
external_dynamic_lists_type_imsi_auth_from_dict = ExternalDynamicListsTypeImsiAuth.from_dict(external_dynamic_lists_type_imsi_auth_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


