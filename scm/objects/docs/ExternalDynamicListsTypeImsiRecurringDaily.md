# ExternalDynamicListsTypeImsiRecurringDaily

Daily interval settings for IMSI updates

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**at** | **str** | Daily Time specification hh (e.g. 20) for IMSI | [default to '00']

## Example

```python
from scm.objects.models.external_dynamic_lists_type_imsi_recurring_daily import ExternalDynamicListsTypeImsiRecurringDaily

# TODO update the JSON string below
json = "{}"
# create an instance of ExternalDynamicListsTypeImsiRecurringDaily from a JSON string
external_dynamic_lists_type_imsi_recurring_daily_instance = ExternalDynamicListsTypeImsiRecurringDaily.from_json(json)
# print the JSON string representation of the object
print(ExternalDynamicListsTypeImsiRecurringDaily.to_json())

# convert the object into a dict
external_dynamic_lists_type_imsi_recurring_daily_dict = external_dynamic_lists_type_imsi_recurring_daily_instance.to_dict()
# create an instance of ExternalDynamicListsTypeImsiRecurringDaily from a dict
external_dynamic_lists_type_imsi_recurring_daily_from_dict = ExternalDynamicListsTypeImsiRecurringDaily.from_dict(external_dynamic_lists_type_imsi_recurring_daily_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


