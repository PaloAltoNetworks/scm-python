# HttpHeaderProfilesHttpHeaderInsertionInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the HTTP header insertion rule | 
**type** | [**List[HttpHeaderProfilesHttpHeaderInsertionInnerTypeInner]**](HttpHeaderProfilesHttpHeaderInsertionInnerTypeInner.md) | A list of HTTP header insertion definitions | 

## Example

```python
from scm_security_services.models.http_header_profiles_http_header_insertion_inner import HttpHeaderProfilesHttpHeaderInsertionInner

# TODO update the JSON string below
json = "{}"
# create an instance of HttpHeaderProfilesHttpHeaderInsertionInner from a JSON string
http_header_profiles_http_header_insertion_inner_instance = HttpHeaderProfilesHttpHeaderInsertionInner.from_json(json)
# print the JSON string representation of the object
print(HttpHeaderProfilesHttpHeaderInsertionInner.to_json())

# convert the object into a dict
http_header_profiles_http_header_insertion_inner_dict = http_header_profiles_http_header_insertion_inner_instance.to_dict()
# create an instance of HttpHeaderProfilesHttpHeaderInsertionInner from a dict
http_header_profiles_http_header_insertion_inner_from_dict = HttpHeaderProfilesHttpHeaderInsertionInner.from_dict(http_header_profiles_http_header_insertion_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


