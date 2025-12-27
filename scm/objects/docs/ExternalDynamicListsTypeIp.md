# ExternalDynamicListsTypeIp

IP settings for Custom IP type

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**auth** | [**ExternalDynamicListsTypeIpAuth**](ExternalDynamicListsTypeIpAuth.md) |  | [optional] 
**certificate_profile** | **str** | Profile for authenticating client certificates | [optional] [default to 'None']
**description** | **str** |  | [optional] 
**exception_list** | **List[str]** | IP Exception List for Custom IP type | [optional] 
**recurring** | [**ExternalDynamicListsTypeIpRecurring**](ExternalDynamicListsTypeIpRecurring.md) |  | 
**url** | **str** | External URL for Custom IP type | [default to 'http://']

## Example

```python
from scm_objects.models.external_dynamic_lists_type_ip import ExternalDynamicListsTypeIp

# TODO update the JSON string below
json = "{}"
# create an instance of ExternalDynamicListsTypeIp from a JSON string
external_dynamic_lists_type_ip_instance = ExternalDynamicListsTypeIp.from_json(json)
# print the JSON string representation of the object
print(ExternalDynamicListsTypeIp.to_json())

# convert the object into a dict
external_dynamic_lists_type_ip_dict = external_dynamic_lists_type_ip_instance.to_dict()
# create an instance of ExternalDynamicListsTypeIp from a dict
external_dynamic_lists_type_ip_from_dict = ExternalDynamicListsTypeIp.from_dict(external_dynamic_lists_type_ip_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


