# ExternalDynamicListsTypeIpRecurringWeekly

Weekly settings for IP recurring

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**at** | **str** | Weekly Time specification hh (e.g. 20) for IP | [default to '00']
**day_of_week** | **str** |  | 

## Example

```python
from scm.objects.models.external_dynamic_lists_type_ip_recurring_weekly import ExternalDynamicListsTypeIpRecurringWeekly

# TODO update the JSON string below
json = "{}"
# create an instance of ExternalDynamicListsTypeIpRecurringWeekly from a JSON string
external_dynamic_lists_type_ip_recurring_weekly_instance = ExternalDynamicListsTypeIpRecurringWeekly.from_json(json)
# print the JSON string representation of the object
print(ExternalDynamicListsTypeIpRecurringWeekly.to_json())

# convert the object into a dict
external_dynamic_lists_type_ip_recurring_weekly_dict = external_dynamic_lists_type_ip_recurring_weekly_instance.to_dict()
# create an instance of ExternalDynamicListsTypeIpRecurringWeekly from a dict
external_dynamic_lists_type_ip_recurring_weekly_from_dict = ExternalDynamicListsTypeIpRecurringWeekly.from_dict(external_dynamic_lists_type_ip_recurring_weekly_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


