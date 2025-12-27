# QosProfilesClassBandwidthType


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mbps** | [**QosProfilesClassBandwidthTypeMbps**](QosProfilesClassBandwidthTypeMbps.md) |  | [optional] 
**percentage** | [**QosProfilesClassBandwidthTypePercentage**](QosProfilesClassBandwidthTypePercentage.md) |  | [optional] 

## Example

```python
from scm_network_services.models.qos_profiles_class_bandwidth_type import QosProfilesClassBandwidthType

# TODO update the JSON string below
json = "{}"
# create an instance of QosProfilesClassBandwidthType from a JSON string
qos_profiles_class_bandwidth_type_instance = QosProfilesClassBandwidthType.from_json(json)
# print the JSON string representation of the object
print(QosProfilesClassBandwidthType.to_json())

# convert the object into a dict
qos_profiles_class_bandwidth_type_dict = qos_profiles_class_bandwidth_type_instance.to_dict()
# create an instance of QosProfilesClassBandwidthType from a dict
qos_profiles_class_bandwidth_type_from_dict = QosProfilesClassBandwidthType.from_dict(qos_profiles_class_bandwidth_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


