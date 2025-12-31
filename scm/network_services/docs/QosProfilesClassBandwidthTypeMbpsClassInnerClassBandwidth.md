# QosProfilesClassBandwidthTypeMbpsClassInnerClassBandwidth


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**egress_guaranteed** | **int** | guaranteed sending bandwidth in mbps | [optional] [default to 0]
**egress_max** | **int** | max sending bandwidth in mbps | [optional] [default to 0]

## Example

```python
from scm.network_services.models.qos_profiles_class_bandwidth_type_mbps_class_inner_class_bandwidth import QosProfilesClassBandwidthTypeMbpsClassInnerClassBandwidth

# TODO update the JSON string below
json = "{}"
# create an instance of QosProfilesClassBandwidthTypeMbpsClassInnerClassBandwidth from a JSON string
qos_profiles_class_bandwidth_type_mbps_class_inner_class_bandwidth_instance = QosProfilesClassBandwidthTypeMbpsClassInnerClassBandwidth.from_json(json)
# print the JSON string representation of the object
print(QosProfilesClassBandwidthTypeMbpsClassInnerClassBandwidth.to_json())

# convert the object into a dict
qos_profiles_class_bandwidth_type_mbps_class_inner_class_bandwidth_dict = qos_profiles_class_bandwidth_type_mbps_class_inner_class_bandwidth_instance.to_dict()
# create an instance of QosProfilesClassBandwidthTypeMbpsClassInnerClassBandwidth from a dict
qos_profiles_class_bandwidth_type_mbps_class_inner_class_bandwidth_from_dict = QosProfilesClassBandwidthTypeMbpsClassInnerClassBandwidth.from_dict(qos_profiles_class_bandwidth_type_mbps_class_inner_class_bandwidth_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


