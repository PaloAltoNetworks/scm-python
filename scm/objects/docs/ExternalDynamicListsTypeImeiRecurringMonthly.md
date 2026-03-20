# ExternalDynamicListsTypeImeiRecurringMonthly

Monthly interval settings for IMEI updates

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**at** | **str** | Monthly Time specification hh (e.g. 20) for IMEI | [default to '00']
**day_of_month** | **int** | Day of month for IMEI updates | 

## Example

```python
from scm.objects.models.external_dynamic_lists_type_imei_recurring_monthly import ExternalDynamicListsTypeImeiRecurringMonthly

# TODO update the JSON string below
json = "{}"
# create an instance of ExternalDynamicListsTypeImeiRecurringMonthly from a JSON string
external_dynamic_lists_type_imei_recurring_monthly_instance = ExternalDynamicListsTypeImeiRecurringMonthly.from_json(json)
# print the JSON string representation of the object
print(ExternalDynamicListsTypeImeiRecurringMonthly.to_json())

# convert the object into a dict
external_dynamic_lists_type_imei_recurring_monthly_dict = external_dynamic_lists_type_imei_recurring_monthly_instance.to_dict()
# create an instance of ExternalDynamicListsTypeImeiRecurringMonthly from a dict
external_dynamic_lists_type_imei_recurring_monthly_from_dict = ExternalDynamicListsTypeImeiRecurringMonthly.from_dict(external_dynamic_lists_type_imei_recurring_monthly_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


