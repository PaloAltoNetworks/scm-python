# ExternalDynamicListsTypeIpRecurringMonthly

Monthly settings for IP recurring

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**at** | **str** | Monthly Time specification hh (e.g. 20) for IP | [default to '00']
**day_of_month** | **int** | Day setting for monthly IP updates | 

## Example

```python
from scm.objects.models.external_dynamic_lists_type_ip_recurring_monthly import ExternalDynamicListsTypeIpRecurringMonthly

# TODO update the JSON string below
json = "{}"
# create an instance of ExternalDynamicListsTypeIpRecurringMonthly from a JSON string
external_dynamic_lists_type_ip_recurring_monthly_instance = ExternalDynamicListsTypeIpRecurringMonthly.from_json(json)
# print the JSON string representation of the object
print(ExternalDynamicListsTypeIpRecurringMonthly.to_json())

# convert the object into a dict
external_dynamic_lists_type_ip_recurring_monthly_dict = external_dynamic_lists_type_ip_recurring_monthly_instance.to_dict()
# create an instance of ExternalDynamicListsTypeIpRecurringMonthly from a dict
external_dynamic_lists_type_ip_recurring_monthly_from_dict = ExternalDynamicListsTypeIpRecurringMonthly.from_dict(external_dynamic_lists_type_ip_recurring_monthly_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


