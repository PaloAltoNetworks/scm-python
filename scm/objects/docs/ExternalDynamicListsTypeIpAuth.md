# ExternalDynamicListsTypeIpAuth

Authentication settings for Custom IP type

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**password** | **str** | Password for Custom IP authentication | 
**username** | **str** | Username for Custom IP authentication | 

## Example

```python
from scm_objects.models.external_dynamic_lists_type_ip_auth import ExternalDynamicListsTypeIpAuth

# TODO update the JSON string below
json = "{}"
# create an instance of ExternalDynamicListsTypeIpAuth from a JSON string
external_dynamic_lists_type_ip_auth_instance = ExternalDynamicListsTypeIpAuth.from_json(json)
# print the JSON string representation of the object
print(ExternalDynamicListsTypeIpAuth.to_json())

# convert the object into a dict
external_dynamic_lists_type_ip_auth_dict = external_dynamic_lists_type_ip_auth_instance.to_dict()
# create an instance of ExternalDynamicListsTypeIpAuth from a dict
external_dynamic_lists_type_ip_auth_from_dict = ExternalDynamicListsTypeIpAuth.from_dict(external_dynamic_lists_type_ip_auth_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


