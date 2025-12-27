# ExternalDynamicListsTypeUrlRecurring

Update Schedule for Custom URL type

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**daily** | [**ExternalDynamicListsTypeUrlRecurringDaily**](ExternalDynamicListsTypeUrlRecurringDaily.md) |  | [optional] 
**five_minute** | **object** | Five minute settings for URL recurring | [optional] 
**hourly** | **object** | Hourly settings for URL recurring | [optional] 
**monthly** | [**ExternalDynamicListsTypeUrlRecurringMonthly**](ExternalDynamicListsTypeUrlRecurringMonthly.md) |  | [optional] 
**weekly** | [**ExternalDynamicListsTypeUrlRecurringWeekly**](ExternalDynamicListsTypeUrlRecurringWeekly.md) |  | [optional] 

## Example

```python
from scm_objects.models.external_dynamic_lists_type_url_recurring import ExternalDynamicListsTypeUrlRecurring

# TODO update the JSON string below
json = "{}"
# create an instance of ExternalDynamicListsTypeUrlRecurring from a JSON string
external_dynamic_lists_type_url_recurring_instance = ExternalDynamicListsTypeUrlRecurring.from_json(json)
# print the JSON string representation of the object
print(ExternalDynamicListsTypeUrlRecurring.to_json())

# convert the object into a dict
external_dynamic_lists_type_url_recurring_dict = external_dynamic_lists_type_url_recurring_instance.to_dict()
# create an instance of ExternalDynamicListsTypeUrlRecurring from a dict
external_dynamic_lists_type_url_recurring_from_dict = ExternalDynamicListsTypeUrlRecurring.from_dict(external_dynamic_lists_type_url_recurring_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


