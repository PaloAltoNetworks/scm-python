# ExternalDynamicListsTypeUrlAuth

Authentication settings for Custom URL type

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**password** | **str** | Password for Custom URL authentication | 
**username** | **str** | Username for Custom URL authentication | 

## Example

```python
from scm_objects.models.external_dynamic_lists_type_url_auth import ExternalDynamicListsTypeUrlAuth

# TODO update the JSON string below
json = "{}"
# create an instance of ExternalDynamicListsTypeUrlAuth from a JSON string
external_dynamic_lists_type_url_auth_instance = ExternalDynamicListsTypeUrlAuth.from_json(json)
# print the JSON string representation of the object
print(ExternalDynamicListsTypeUrlAuth.to_json())

# convert the object into a dict
external_dynamic_lists_type_url_auth_dict = external_dynamic_lists_type_url_auth_instance.to_dict()
# create an instance of ExternalDynamicListsTypeUrlAuth from a dict
external_dynamic_lists_type_url_auth_from_dict = ExternalDynamicListsTypeUrlAuth.from_dict(external_dynamic_lists_type_url_auth_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


