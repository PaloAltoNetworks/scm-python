# ExternalDynamicListsTypeDomainRecurring

Update Schedule for Custom Domain type

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**daily** | [**ExternalDynamicListsTypeDomainRecurringDaily**](ExternalDynamicListsTypeDomainRecurringDaily.md) |  | [optional] 
**five_minute** | **object** | Five minute settings for Domain recurring | [optional] 
**hourly** | **object** | Hourly settings for Domain recurring | [optional] 
**monthly** | [**ExternalDynamicListsTypeDomainRecurringMonthly**](ExternalDynamicListsTypeDomainRecurringMonthly.md) |  | [optional] 
**weekly** | [**ExternalDynamicListsTypeDomainRecurringWeekly**](ExternalDynamicListsTypeDomainRecurringWeekly.md) |  | [optional] 

## Example

```python
from scm.objects.models.external_dynamic_lists_type_domain_recurring import ExternalDynamicListsTypeDomainRecurring

# TODO update the JSON string below
json = "{}"
# create an instance of ExternalDynamicListsTypeDomainRecurring from a JSON string
external_dynamic_lists_type_domain_recurring_instance = ExternalDynamicListsTypeDomainRecurring.from_json(json)
# print the JSON string representation of the object
print(ExternalDynamicListsTypeDomainRecurring.to_json())

# convert the object into a dict
external_dynamic_lists_type_domain_recurring_dict = external_dynamic_lists_type_domain_recurring_instance.to_dict()
# create an instance of ExternalDynamicListsTypeDomainRecurring from a dict
external_dynamic_lists_type_domain_recurring_from_dict = ExternalDynamicListsTypeDomainRecurring.from_dict(external_dynamic_lists_type_domain_recurring_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


