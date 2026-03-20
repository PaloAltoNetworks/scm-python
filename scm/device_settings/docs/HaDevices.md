# HaDevices


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**device** | **str** | The device in which the resource is defined | [optional] 
**folder** | **str** | The folder in which the resource is defined | [optional] 
**ha_devices** | [**List[HaDevicesHaDevicesInner]**](HaDevicesHaDevicesInner.md) | HA devices | [optional] 
**snippet** | **str** | The snippet in which the resource is defined | [optional] 

## Example

```python
from scm.device_settings.models.ha_devices import HaDevices

# TODO update the JSON string below
json = "{}"
# create an instance of HaDevices from a JSON string
ha_devices_instance = HaDevices.from_json(json)
# print the JSON string representation of the object
print(HaDevices.to_json())

# convert the object into a dict
ha_devices_dict = ha_devices_instance.to_dict()
# create an instance of HaDevices from a dict
ha_devices_from_dict = HaDevices.from_dict(ha_devices_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


