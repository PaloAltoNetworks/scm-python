# ExternalDynamicListsTypeImeiRecurringDaily

Daily interval settings for IMEI updates

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**at** | **str** | Daily Time specification hh (e.g. 20) for IMEI | [default to '00']

## Example

```python
from scm.objects.models.external_dynamic_lists_type_imei_recurring_daily import ExternalDynamicListsTypeImeiRecurringDaily

# TODO update the JSON string below
json = "{}"
# create an instance of ExternalDynamicListsTypeImeiRecurringDaily from a JSON string
external_dynamic_lists_type_imei_recurring_daily_instance = ExternalDynamicListsTypeImeiRecurringDaily.from_json(json)
# print the JSON string representation of the object
print(ExternalDynamicListsTypeImeiRecurringDaily.to_json())

# convert the object into a dict
external_dynamic_lists_type_imei_recurring_daily_dict = external_dynamic_lists_type_imei_recurring_daily_instance.to_dict()
# create an instance of ExternalDynamicListsTypeImeiRecurringDaily from a dict
external_dynamic_lists_type_imei_recurring_daily_from_dict = ExternalDynamicListsTypeImeiRecurringDaily.from_dict(external_dynamic_lists_type_imei_recurring_daily_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


