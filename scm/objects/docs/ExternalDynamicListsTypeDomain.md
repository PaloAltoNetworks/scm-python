# ExternalDynamicListsTypeDomain

Domain settings for Custom Domain type

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**auth** | [**ExternalDynamicListsTypeDomainAuth**](ExternalDynamicListsTypeDomainAuth.md) |  | [optional] 
**certificate_profile** | **str** | Profile for authenticating client certificates | [optional] [default to 'None']
**description** | **str** |  | [optional] 
**exception_list** | **List[str]** | Domain Exception List for Custom Domain type | [optional] 
**expand_domain** | **bool** | Enable/Disable expand domain | [optional] [default to False]
**recurring** | [**ExternalDynamicListsTypeDomainRecurring**](ExternalDynamicListsTypeDomainRecurring.md) |  | 
**url** | **str** | External URL for Custom Domain type | [default to 'http://']

## Example

```python
from scm_objects.models.external_dynamic_lists_type_domain import ExternalDynamicListsTypeDomain

# TODO update the JSON string below
json = "{}"
# create an instance of ExternalDynamicListsTypeDomain from a JSON string
external_dynamic_lists_type_domain_instance = ExternalDynamicListsTypeDomain.from_json(json)
# print the JSON string representation of the object
print(ExternalDynamicListsTypeDomain.to_json())

# convert the object into a dict
external_dynamic_lists_type_domain_dict = external_dynamic_lists_type_domain_instance.to_dict()
# create an instance of ExternalDynamicListsTypeDomain from a dict
external_dynamic_lists_type_domain_from_dict = ExternalDynamicListsTypeDomain.from_dict(external_dynamic_lists_type_domain_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


