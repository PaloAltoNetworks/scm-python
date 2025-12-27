# ExternalDynamicListsTypeImsiRecurringMonthly

Monthly interval settings for IMSI updates

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**at** | **str** | Monthly Time specification hh (e.g. 20) for IMSI | [default to '00']
**day_of_month** | **int** | Day of the month for monthly IMSI updates | 

## Example

```python
from scm_objects.models.external_dynamic_lists_type_imsi_recurring_monthly import ExternalDynamicListsTypeImsiRecurringMonthly

# TODO update the JSON string below
json = "{}"
# create an instance of ExternalDynamicListsTypeImsiRecurringMonthly from a JSON string
external_dynamic_lists_type_imsi_recurring_monthly_instance = ExternalDynamicListsTypeImsiRecurringMonthly.from_json(json)
# print the JSON string representation of the object
print(ExternalDynamicListsTypeImsiRecurringMonthly.to_json())

# convert the object into a dict
external_dynamic_lists_type_imsi_recurring_monthly_dict = external_dynamic_lists_type_imsi_recurring_monthly_instance.to_dict()
# create an instance of ExternalDynamicListsTypeImsiRecurringMonthly from a dict
external_dynamic_lists_type_imsi_recurring_monthly_from_dict = ExternalDynamicListsTypeImsiRecurringMonthly.from_dict(external_dynamic_lists_type_imsi_recurring_monthly_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


