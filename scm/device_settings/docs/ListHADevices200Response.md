# ListHADevices200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[HaDevices]**](HaDevices.md) |  | [optional] 

## Example

```python
from scm_device_settings.models.list_ha_devices200_response import ListHADevices200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ListHADevices200Response from a JSON string
list_ha_devices200_response_instance = ListHADevices200Response.from_json(json)
# print the JSON string representation of the object
print(ListHADevices200Response.to_json())

# convert the object into a dict
list_ha_devices200_response_dict = list_ha_devices200_response_instance.to_dict()
# create an instance of ListHADevices200Response from a dict
list_ha_devices200_response_from_dict = ListHADevices200Response.from_dict(list_ha_devices200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


