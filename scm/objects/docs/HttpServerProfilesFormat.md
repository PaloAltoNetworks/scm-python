# HttpServerProfilesFormat


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**auth** | [**PayloadFormat**](PayloadFormat.md) |  | [optional] 
**config** | [**PayloadFormat**](PayloadFormat.md) |  | [optional] 
**correlation** | [**PayloadFormat**](PayloadFormat.md) |  | [optional] 
**data** | [**PayloadFormat**](PayloadFormat.md) |  | [optional] 
**decryption** | [**PayloadFormat**](PayloadFormat.md) |  | [optional] 
**globalprotect** | [**PayloadFormat**](PayloadFormat.md) |  | [optional] 
**gtp** | [**PayloadFormat**](PayloadFormat.md) |  | [optional] 
**hip_match** | [**PayloadFormat**](PayloadFormat.md) |  | [optional] 
**iptag** | [**PayloadFormat**](PayloadFormat.md) |  | [optional] 
**sctp** | [**PayloadFormat**](PayloadFormat.md) |  | [optional] 
**system** | [**PayloadFormat**](PayloadFormat.md) |  | [optional] 
**threat** | [**PayloadFormat**](PayloadFormat.md) |  | [optional] 
**traffic** | [**PayloadFormat**](PayloadFormat.md) |  | [optional] 
**tunnel** | [**PayloadFormat**](PayloadFormat.md) |  | [optional] 
**url** | [**PayloadFormat**](PayloadFormat.md) |  | [optional] 
**userid** | [**PayloadFormat**](PayloadFormat.md) |  | [optional] 
**wildfire** | [**PayloadFormat**](PayloadFormat.md) |  | [optional] 

## Example

```python
from scm_objects.models.http_server_profiles_format import HttpServerProfilesFormat

# TODO update the JSON string below
json = "{}"
# create an instance of HttpServerProfilesFormat from a JSON string
http_server_profiles_format_instance = HttpServerProfilesFormat.from_json(json)
# print the JSON string representation of the object
print(HttpServerProfilesFormat.to_json())

# convert the object into a dict
http_server_profiles_format_dict = http_server_profiles_format_instance.to_dict()
# create an instance of HttpServerProfilesFormat from a dict
http_server_profiles_format_from_dict = HttpServerProfilesFormat.from_dict(http_server_profiles_format_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


