# HttpHeaderProfilesHttpHeaderInsertionInnerTypeInnerHeadersInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**header** | **str** | The HTTP header string | 
**log** | **bool** | Log the use of this HTTP header insertion? | [optional] [default to False]
**name** | **str** | The name of the HTTP header | 
**value** | **str** | The value associated with the HTTP header | 

## Example

```python
from scm_security_services.models.http_header_profiles_http_header_insertion_inner_type_inner_headers_inner import HttpHeaderProfilesHttpHeaderInsertionInnerTypeInnerHeadersInner

# TODO update the JSON string below
json = "{}"
# create an instance of HttpHeaderProfilesHttpHeaderInsertionInnerTypeInnerHeadersInner from a JSON string
http_header_profiles_http_header_insertion_inner_type_inner_headers_inner_instance = HttpHeaderProfilesHttpHeaderInsertionInnerTypeInnerHeadersInner.from_json(json)
# print the JSON string representation of the object
print(HttpHeaderProfilesHttpHeaderInsertionInnerTypeInnerHeadersInner.to_json())

# convert the object into a dict
http_header_profiles_http_header_insertion_inner_type_inner_headers_inner_dict = http_header_profiles_http_header_insertion_inner_type_inner_headers_inner_instance.to_dict()
# create an instance of HttpHeaderProfilesHttpHeaderInsertionInnerTypeInnerHeadersInner from a dict
http_header_profiles_http_header_insertion_inner_type_inner_headers_inner_from_dict = HttpHeaderProfilesHttpHeaderInsertionInnerTypeInnerHeadersInner.from_dict(http_header_profiles_http_header_insertion_inner_type_inner_headers_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


