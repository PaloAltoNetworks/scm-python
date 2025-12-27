# QosProfilesClassBandwidthTypeMbpsClassInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**class_bandwidth** | [**QosProfilesClassBandwidthTypeMbpsClassInnerClassBandwidth**](QosProfilesClassBandwidthTypeMbpsClassInnerClassBandwidth.md) |  | [optional] 
**name** | **str** | Traffic class | [optional] 
**priority** | **str** | traffic class priority | [optional] [default to 'medium']

## Example

```python
from scm_network_services.models.qos_profiles_class_bandwidth_type_mbps_class_inner import QosProfilesClassBandwidthTypeMbpsClassInner

# TODO update the JSON string below
json = "{}"
# create an instance of QosProfilesClassBandwidthTypeMbpsClassInner from a JSON string
qos_profiles_class_bandwidth_type_mbps_class_inner_instance = QosProfilesClassBandwidthTypeMbpsClassInner.from_json(json)
# print the JSON string representation of the object
print(QosProfilesClassBandwidthTypeMbpsClassInner.to_json())

# convert the object into a dict
qos_profiles_class_bandwidth_type_mbps_class_inner_dict = qos_profiles_class_bandwidth_type_mbps_class_inner_instance.to_dict()
# create an instance of QosProfilesClassBandwidthTypeMbpsClassInner from a dict
qos_profiles_class_bandwidth_type_mbps_class_inner_from_dict = QosProfilesClassBandwidthTypeMbpsClassInner.from_dict(qos_profiles_class_bandwidth_type_mbps_class_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


