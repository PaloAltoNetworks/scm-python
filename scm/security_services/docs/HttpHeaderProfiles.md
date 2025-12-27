# HttpHeaderProfiles


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | The description of the HTTP header profile | [optional] 
**device** | **str** | The device in which the resource is defined | [optional] 
**folder** | **str** | The folder in which the resource is defined | [optional] 
**http_header_insertion** | [**List[HttpHeaderProfilesHttpHeaderInsertionInner]**](HttpHeaderProfilesHttpHeaderInsertionInner.md) | A list of HTTP header profile rules | [optional] 
**id** | **str** | The UUID of the HTTP header profile | [optional] [readonly] 
**name** | **str** | The name of the HTTP header profile | 
**snippet** | **str** | The snippet in which the resource is defined | [optional] 

## Example

```python
from scm.security_services.models.http_header_profiles import HttpHeaderProfiles

# TODO update the JSON string below
json = "{}"
# create an instance of HttpHeaderProfiles from a JSON string
http_header_profiles_instance = HttpHeaderProfiles.from_json(json)
# print the JSON string representation of the object
print(HttpHeaderProfiles.to_json())

# convert the object into a dict
http_header_profiles_dict = http_header_profiles_instance.to_dict()
# create an instance of HttpHeaderProfiles from a dict
http_header_profiles_from_dict = HttpHeaderProfiles.from_dict(http_header_profiles_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


