# ExternalDynamicListsTypeImsiRecurring

IMSI Recuring Config for Custom IMSI type

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**daily** | [**ExternalDynamicListsTypeImsiRecurringDaily**](ExternalDynamicListsTypeImsiRecurringDaily.md) |  | [optional] 
**five_minute** | **object** | Five-minute interval settings for IMSI updates | [optional] 
**hourly** | **object** | Hourly interval settings for IMSI updates | [optional] 
**monthly** | [**ExternalDynamicListsTypeImsiRecurringMonthly**](ExternalDynamicListsTypeImsiRecurringMonthly.md) |  | [optional] 
**weekly** | [**ExternalDynamicListsTypeImsiRecurringWeekly**](ExternalDynamicListsTypeImsiRecurringWeekly.md) |  | [optional] 

## Example

```python
from scm_objects.models.external_dynamic_lists_type_imsi_recurring import ExternalDynamicListsTypeImsiRecurring

# TODO update the JSON string below
json = "{}"
# create an instance of ExternalDynamicListsTypeImsiRecurring from a JSON string
external_dynamic_lists_type_imsi_recurring_instance = ExternalDynamicListsTypeImsiRecurring.from_json(json)
# print the JSON string representation of the object
print(ExternalDynamicListsTypeImsiRecurring.to_json())

# convert the object into a dict
external_dynamic_lists_type_imsi_recurring_dict = external_dynamic_lists_type_imsi_recurring_instance.to_dict()
# create an instance of ExternalDynamicListsTypeImsiRecurring from a dict
external_dynamic_lists_type_imsi_recurring_from_dict = ExternalDynamicListsTypeImsiRecurring.from_dict(external_dynamic_lists_type_imsi_recurring_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


