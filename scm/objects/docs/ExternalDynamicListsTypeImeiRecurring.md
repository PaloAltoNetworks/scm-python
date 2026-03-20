# ExternalDynamicListsTypeImeiRecurring

Recurring interval for IMEI updates

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**daily** | [**ExternalDynamicListsTypeImeiRecurringDaily**](ExternalDynamicListsTypeImeiRecurringDaily.md) |  | [optional] 
**five_minute** | **object** | Five-minute interval settings for IMEI updates | [optional] 
**hourly** | **object** | Hourly interval settings for IMEI updates | [optional] 
**monthly** | [**ExternalDynamicListsTypeImeiRecurringMonthly**](ExternalDynamicListsTypeImeiRecurringMonthly.md) |  | [optional] 
**weekly** | [**ExternalDynamicListsTypeImeiRecurringWeekly**](ExternalDynamicListsTypeImeiRecurringWeekly.md) |  | [optional] 

## Example

```python
from scm.objects.models.external_dynamic_lists_type_imei_recurring import ExternalDynamicListsTypeImeiRecurring

# TODO update the JSON string below
json = "{}"
# create an instance of ExternalDynamicListsTypeImeiRecurring from a JSON string
external_dynamic_lists_type_imei_recurring_instance = ExternalDynamicListsTypeImeiRecurring.from_json(json)
# print the JSON string representation of the object
print(ExternalDynamicListsTypeImeiRecurring.to_json())

# convert the object into a dict
external_dynamic_lists_type_imei_recurring_dict = external_dynamic_lists_type_imei_recurring_instance.to_dict()
# create an instance of ExternalDynamicListsTypeImeiRecurring from a dict
external_dynamic_lists_type_imei_recurring_from_dict = ExternalDynamicListsTypeImeiRecurring.from_dict(external_dynamic_lists_type_imei_recurring_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


