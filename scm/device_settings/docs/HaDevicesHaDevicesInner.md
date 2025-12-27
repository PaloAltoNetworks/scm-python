# HaDevicesHaDevicesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**primary_device_name** | **str** | Primary device name | [optional] 
**primary_serial_number** | **str** | Primary device serial number | [optional] 
**secondary_device_name** | **str** | Secondary device name | [optional] 
**secondary_serial_number** | **str** | Secondary device serial number | [optional] 

## Example

```python
from scm_device_settings.models.ha_devices_ha_devices_inner import HaDevicesHaDevicesInner

# TODO update the JSON string below
json = "{}"
# create an instance of HaDevicesHaDevicesInner from a JSON string
ha_devices_ha_devices_inner_instance = HaDevicesHaDevicesInner.from_json(json)
# print the JSON string representation of the object
print(HaDevicesHaDevicesInner.to_json())

# convert the object into a dict
ha_devices_ha_devices_inner_dict = ha_devices_ha_devices_inner_instance.to_dict()
# create an instance of HaDevicesHaDevicesInner from a dict
ha_devices_ha_devices_inner_from_dict = HaDevicesHaDevicesInner.from_dict(ha_devices_ha_devices_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


