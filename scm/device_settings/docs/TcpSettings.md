# TcpSettings


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**device** | **str** | The device in which the resource is defined | [optional] 
**folder** | **str** | The folder in which the resource is defined | [optional] 
**id** | **str** | UUID of the resource | [optional] [readonly] 
**snippet** | **str** | The snippet in which the resource is defined | [optional] 
**tcp** | [**TcpSettingsTcp**](TcpSettingsTcp.md) |  | [optional] 

## Example

```python
from scm.device_settings.models.tcp_settings import TcpSettings

# TODO update the JSON string below
json = "{}"
# create an instance of TcpSettings from a JSON string
tcp_settings_instance = TcpSettings.from_json(json)
# print the JSON string representation of the object
print(TcpSettings.to_json())

# convert the object into a dict
tcp_settings_dict = tcp_settings_instance.to_dict()
# create an instance of TcpSettings from a dict
tcp_settings_from_dict = TcpSettings.from_dict(tcp_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


