# ExternalDynamicListsTypeIpRecurring

Update Schedule for Custom IP type

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**daily** | [**ExternalDynamicListsTypeIpRecurringDaily**](ExternalDynamicListsTypeIpRecurringDaily.md) |  | [optional] 
**five_minute** | **object** | Five minute settings for IP recurring | [optional] 
**hourly** | **object** | Hourly settings for IP recurring | [optional] 
**monthly** | [**ExternalDynamicListsTypeIpRecurringMonthly**](ExternalDynamicListsTypeIpRecurringMonthly.md) |  | [optional] 
**weekly** | [**ExternalDynamicListsTypeIpRecurringWeekly**](ExternalDynamicListsTypeIpRecurringWeekly.md) |  | [optional] 

## Example

```python
from scm.objects.models.external_dynamic_lists_type_ip_recurring import ExternalDynamicListsTypeIpRecurring

# TODO update the JSON string below
json = "{}"
# create an instance of ExternalDynamicListsTypeIpRecurring from a JSON string
external_dynamic_lists_type_ip_recurring_instance = ExternalDynamicListsTypeIpRecurring.from_json(json)
# print the JSON string representation of the object
print(ExternalDynamicListsTypeIpRecurring.to_json())

# convert the object into a dict
external_dynamic_lists_type_ip_recurring_dict = external_dynamic_lists_type_ip_recurring_instance.to_dict()
# create an instance of ExternalDynamicListsTypeIpRecurring from a dict
external_dynamic_lists_type_ip_recurring_from_dict = ExternalDynamicListsTypeIpRecurring.from_dict(external_dynamic_lists_type_ip_recurring_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


