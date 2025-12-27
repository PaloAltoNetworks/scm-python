# QosProfilesClassBandwidthTypeMbps


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_class** | [**List[QosProfilesClassBandwidthTypeMbpsClassInner]**](QosProfilesClassBandwidthTypeMbpsClassInner.md) | QoS setting for traffic classes | [optional] 

## Example

```python
from scm.network_services.models.qos_profiles_class_bandwidth_type_mbps import QosProfilesClassBandwidthTypeMbps

# TODO update the JSON string below
json = "{}"
# create an instance of QosProfilesClassBandwidthTypeMbps from a JSON string
qos_profiles_class_bandwidth_type_mbps_instance = QosProfilesClassBandwidthTypeMbps.from_json(json)
# print the JSON string representation of the object
print(QosProfilesClassBandwidthTypeMbps.to_json())

# convert the object into a dict
qos_profiles_class_bandwidth_type_mbps_dict = qos_profiles_class_bandwidth_type_mbps_instance.to_dict()
# create an instance of QosProfilesClassBandwidthTypeMbps from a dict
qos_profiles_class_bandwidth_type_mbps_from_dict = QosProfilesClassBandwidthTypeMbps.from_dict(qos_profiles_class_bandwidth_type_mbps_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


