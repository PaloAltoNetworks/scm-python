# HaConfigurations


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**device** | **str** | The device in which the resource is defined | [optional] 
**enabled** | **bool** |  | [optional] [default to True]
**folder** | **str** | The folder in which the resource is defined | [optional] 
**group** | [**HaConfigurationsGroup**](HaConfigurationsGroup.md) |  | 
**interface** | [**HaConfigurationsInterface**](HaConfigurationsInterface.md) |  | 
**snippet** | **str** | The snippet in which the resource is defined | [optional] 

## Example

```python
from scm.device_settings.models.ha_configurations import HaConfigurations

# TODO update the JSON string below
json = "{}"
# create an instance of HaConfigurations from a JSON string
ha_configurations_instance = HaConfigurations.from_json(json)
# print the JSON string representation of the object
print(HaConfigurations.to_json())

# convert the object into a dict
ha_configurations_dict = ha_configurations_instance.to_dict()
# create an instance of HaConfigurations from a dict
ha_configurations_from_dict = HaConfigurations.from_dict(ha_configurations_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


