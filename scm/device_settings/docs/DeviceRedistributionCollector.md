# DeviceRedistributionCollector


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**device** | **str** | The device in which the resource is defined | [optional] 
**folder** | **str** | The folder in which the resource is defined | [optional] 
**id** | **str** | UUID of the resource | [optional] [readonly] 
**redistribution_collector** | [**DeviceRedistributionCollectorRedistributionCollector**](DeviceRedistributionCollectorRedistributionCollector.md) |  | [optional] 
**snippet** | **str** | The snippet in which the resource is defined | [optional] 

## Example

```python
from scm_device_settings.models.device_redistribution_collector import DeviceRedistributionCollector

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceRedistributionCollector from a JSON string
device_redistribution_collector_instance = DeviceRedistributionCollector.from_json(json)
# print the JSON string representation of the object
print(DeviceRedistributionCollector.to_json())

# convert the object into a dict
device_redistribution_collector_dict = device_redistribution_collector_instance.to_dict()
# create an instance of DeviceRedistributionCollector from a dict
device_redistribution_collector_from_dict = DeviceRedistributionCollector.from_dict(device_redistribution_collector_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


