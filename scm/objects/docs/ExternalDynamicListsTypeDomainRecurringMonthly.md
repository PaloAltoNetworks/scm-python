# ExternalDynamicListsTypeDomainRecurringMonthly

Monthly settings for Domain recurring

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**at** | **str** | Monthly Time specification hh (e.g. 20) for domain | [default to '00']
**day_of_month** | **int** | Day setting for monthly Domain updates | 

## Example

```python
from scm_objects.models.external_dynamic_lists_type_domain_recurring_monthly import ExternalDynamicListsTypeDomainRecurringMonthly

# TODO update the JSON string below
json = "{}"
# create an instance of ExternalDynamicListsTypeDomainRecurringMonthly from a JSON string
external_dynamic_lists_type_domain_recurring_monthly_instance = ExternalDynamicListsTypeDomainRecurringMonthly.from_json(json)
# print the JSON string representation of the object
print(ExternalDynamicListsTypeDomainRecurringMonthly.to_json())

# convert the object into a dict
external_dynamic_lists_type_domain_recurring_monthly_dict = external_dynamic_lists_type_domain_recurring_monthly_instance.to_dict()
# create an instance of ExternalDynamicListsTypeDomainRecurringMonthly from a dict
external_dynamic_lists_type_domain_recurring_monthly_from_dict = ExternalDynamicListsTypeDomainRecurringMonthly.from_dict(external_dynamic_lists_type_domain_recurring_monthly_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


