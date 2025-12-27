# ExternalDynamicListsTypeDomainAuth

Authentication settings for Custom Domain type

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**password** | **str** | Password for Custom Domain authentication | 
**username** | **str** | Username for Custom Domain authentication | 

## Example

```python
from scm.objects.models.external_dynamic_lists_type_domain_auth import ExternalDynamicListsTypeDomainAuth

# TODO update the JSON string below
json = "{}"
# create an instance of ExternalDynamicListsTypeDomainAuth from a JSON string
external_dynamic_lists_type_domain_auth_instance = ExternalDynamicListsTypeDomainAuth.from_json(json)
# print the JSON string representation of the object
print(ExternalDynamicListsTypeDomainAuth.to_json())

# convert the object into a dict
external_dynamic_lists_type_domain_auth_dict = external_dynamic_lists_type_domain_auth_instance.to_dict()
# create an instance of ExternalDynamicListsTypeDomainAuth from a dict
external_dynamic_lists_type_domain_auth_from_dict = ExternalDynamicListsTypeDomainAuth.from_dict(external_dynamic_lists_type_domain_auth_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


