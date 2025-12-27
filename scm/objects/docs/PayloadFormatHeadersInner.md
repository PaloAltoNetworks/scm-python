# PayloadFormatHeadersInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Header name | [optional] 
**value** | **str** | Header value | [optional] 

## Example

```python
from scm.objects.models.payload_format_headers_inner import PayloadFormatHeadersInner

# TODO update the JSON string below
json = "{}"
# create an instance of PayloadFormatHeadersInner from a JSON string
payload_format_headers_inner_instance = PayloadFormatHeadersInner.from_json(json)
# print the JSON string representation of the object
print(PayloadFormatHeadersInner.to_json())

# convert the object into a dict
payload_format_headers_inner_dict = payload_format_headers_inner_instance.to_dict()
# create an instance of PayloadFormatHeadersInner from a dict
payload_format_headers_inner_from_dict = PayloadFormatHeadersInner.from_dict(payload_format_headers_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


