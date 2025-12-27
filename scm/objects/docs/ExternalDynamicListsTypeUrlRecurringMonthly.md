# ExternalDynamicListsTypeUrlRecurringMonthly

Monthly settings for URL recurring

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**at** | **str** | Monthly Time specification hh (e.g. 20) for URL | [default to '00']
**day_of_month** | **int** | Day setting for monthly URL updates | 

## Example

```python
from scm.objects.models.external_dynamic_lists_type_url_recurring_monthly import ExternalDynamicListsTypeUrlRecurringMonthly

# TODO update the JSON string below
json = "{}"
# create an instance of ExternalDynamicListsTypeUrlRecurringMonthly from a JSON string
external_dynamic_lists_type_url_recurring_monthly_instance = ExternalDynamicListsTypeUrlRecurringMonthly.from_json(json)
# print the JSON string representation of the object
print(ExternalDynamicListsTypeUrlRecurringMonthly.to_json())

# convert the object into a dict
external_dynamic_lists_type_url_recurring_monthly_dict = external_dynamic_lists_type_url_recurring_monthly_instance.to_dict()
# create an instance of ExternalDynamicListsTypeUrlRecurringMonthly from a dict
external_dynamic_lists_type_url_recurring_monthly_from_dict = ExternalDynamicListsTypeUrlRecurringMonthly.from_dict(external_dynamic_lists_type_url_recurring_monthly_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


