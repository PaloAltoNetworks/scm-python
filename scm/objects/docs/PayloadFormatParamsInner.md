# PayloadFormatParamsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Parameter name | [optional] 
**value** | **str** | Parameter value | [optional] 

## Example

```python
from scm.objects.models.payload_format_params_inner import PayloadFormatParamsInner

# TODO update the JSON string below
json = "{}"
# create an instance of PayloadFormatParamsInner from a JSON string
payload_format_params_inner_instance = PayloadFormatParamsInner.from_json(json)
# print the JSON string representation of the object
print(PayloadFormatParamsInner.to_json())

# convert the object into a dict
payload_format_params_inner_dict = payload_format_params_inner_instance.to_dict()
# create an instance of PayloadFormatParamsInner from a dict
payload_format_params_inner_from_dict = PayloadFormatParamsInner.from_dict(payload_format_params_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


