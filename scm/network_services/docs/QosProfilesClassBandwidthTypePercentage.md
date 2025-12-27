# QosProfilesClassBandwidthTypePercentage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_class** | [**List[QosProfilesClassBandwidthTypePercentageClassInner]**](QosProfilesClassBandwidthTypePercentageClassInner.md) | QoS setting for traffic classes | [optional] 

## Example

```python
from scm_network_services.models.qos_profiles_class_bandwidth_type_percentage import QosProfilesClassBandwidthTypePercentage

# TODO update the JSON string below
json = "{}"
# create an instance of QosProfilesClassBandwidthTypePercentage from a JSON string
qos_profiles_class_bandwidth_type_percentage_instance = QosProfilesClassBandwidthTypePercentage.from_json(json)
# print the JSON string representation of the object
print(QosProfilesClassBandwidthTypePercentage.to_json())

# convert the object into a dict
qos_profiles_class_bandwidth_type_percentage_dict = qos_profiles_class_bandwidth_type_percentage_instance.to_dict()
# create an instance of QosProfilesClassBandwidthTypePercentage from a dict
qos_profiles_class_bandwidth_type_percentage_from_dict = QosProfilesClassBandwidthTypePercentage.from_dict(qos_profiles_class_bandwidth_type_percentage_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


