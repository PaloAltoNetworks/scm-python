# HttpHeaderProfilesHttpHeaderInsertionInnerTypeInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**domains** | **List[str]** | A list of DNS domains | 
**headers** | [**List[HttpHeaderProfilesHttpHeaderInsertionInnerTypeInnerHeadersInner]**](HttpHeaderProfilesHttpHeaderInsertionInnerTypeInnerHeadersInner.md) |  | 
**name** | **str** | The HTTP header insertion type | 

## Example

```python
from scm_security_services.models.http_header_profiles_http_header_insertion_inner_type_inner import HttpHeaderProfilesHttpHeaderInsertionInnerTypeInner

# TODO update the JSON string below
json = "{}"
# create an instance of HttpHeaderProfilesHttpHeaderInsertionInnerTypeInner from a JSON string
http_header_profiles_http_header_insertion_inner_type_inner_instance = HttpHeaderProfilesHttpHeaderInsertionInnerTypeInner.from_json(json)
# print the JSON string representation of the object
print(HttpHeaderProfilesHttpHeaderInsertionInnerTypeInner.to_json())

# convert the object into a dict
http_header_profiles_http_header_insertion_inner_type_inner_dict = http_header_profiles_http_header_insertion_inner_type_inner_instance.to_dict()
# create an instance of HttpHeaderProfilesHttpHeaderInsertionInnerTypeInner from a dict
http_header_profiles_http_header_insertion_inner_type_inner_from_dict = HttpHeaderProfilesHttpHeaderInsertionInnerTypeInner.from_dict(http_header_profiles_http_header_insertion_inner_type_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


