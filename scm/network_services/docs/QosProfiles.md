# QosProfiles


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**aggregate_bandwidth** | [**QosProfilesAggregateBandwidth**](QosProfilesAggregateBandwidth.md) |  | [optional] 
**class_bandwidth_type** | [**QosProfilesClassBandwidthType**](QosProfilesClassBandwidthType.md) |  | [optional] 
**device** | **str** | The device in which the resource is defined | [optional] 
**folder** | **str** | The folder in which the resource is defined | [optional] 
**id** | **str** | UUID of the resource | [optional] [readonly] 
**name** | **str** | Alphanumeric string begin with letter: [0-9a-zA-Z._-] | 
**snippet** | **str** | The snippet in which the resource is defined | [optional] 

## Example

```python
from scm_network_services.models.qos_profiles import QosProfiles

# TODO update the JSON string below
json = "{}"
# create an instance of QosProfiles from a JSON string
qos_profiles_instance = QosProfiles.from_json(json)
# print the JSON string representation of the object
print(QosProfiles.to_json())

# convert the object into a dict
qos_profiles_dict = qos_profiles_instance.to_dict()
# create an instance of QosProfiles from a dict
qos_profiles_from_dict = QosProfiles.from_dict(qos_profiles_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


