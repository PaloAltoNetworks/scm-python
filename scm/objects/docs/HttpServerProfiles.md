# HttpServerProfiles


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**device** | **str** | The device in which the resource is defined | [optional] 
**folder** | **str** | The folder in which the resource is defined | [optional] 
**format** | [**HttpServerProfilesFormat**](HttpServerProfilesFormat.md) |  | [optional] 
**id** | **str** | The UUID of the HTTP server profile | [readonly] 
**name** | **str** | The name of the profile | 
**server** | [**List[HttpServerProfilesServerInner]**](HttpServerProfilesServerInner.md) |  | [optional] 
**snippet** | **str** | The snippet in which the resource is defined | [optional] 
**tag_registration** | **bool** | Register tags on match | [optional] 

## Example

```python
from scm.objects.models.http_server_profiles import HttpServerProfiles

# TODO update the JSON string below
json = "{}"
# create an instance of HttpServerProfiles from a JSON string
http_server_profiles_instance = HttpServerProfiles.from_json(json)
# print the JSON string representation of the object
print(HttpServerProfiles.to_json())

# convert the object into a dict
http_server_profiles_dict = http_server_profiles_instance.to_dict()
# create an instance of HttpServerProfiles from a dict
http_server_profiles_from_dict = HttpServerProfiles.from_dict(http_server_profiles_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


