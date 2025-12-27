# ExternalDynamicListsTypeUrlRecurringWeekly

Weekly settings for URL recurring

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**at** | **str** | Weekly Time specification hh (e.g. 20) for URL | [default to '00']
**day_of_week** | **str** |  | 

## Example

```python
from scm_objects.models.external_dynamic_lists_type_url_recurring_weekly import ExternalDynamicListsTypeUrlRecurringWeekly

# TODO update the JSON string below
json = "{}"
# create an instance of ExternalDynamicListsTypeUrlRecurringWeekly from a JSON string
external_dynamic_lists_type_url_recurring_weekly_instance = ExternalDynamicListsTypeUrlRecurringWeekly.from_json(json)
# print the JSON string representation of the object
print(ExternalDynamicListsTypeUrlRecurringWeekly.to_json())

# convert the object into a dict
external_dynamic_lists_type_url_recurring_weekly_dict = external_dynamic_lists_type_url_recurring_weekly_instance.to_dict()
# create an instance of ExternalDynamicListsTypeUrlRecurringWeekly from a dict
external_dynamic_lists_type_url_recurring_weekly_from_dict = ExternalDynamicListsTypeUrlRecurringWeekly.from_dict(external_dynamic_lists_type_url_recurring_weekly_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


