# QosProfilesAggregateBandwidth


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**egress_guaranteed** | **int** | guaranteed sending bandwidth in mbps | [optional] 
**egress_max** | **int** | max sending bandwidth in mbps | [optional] 

## Example

```python
from scm.network_services.models.qos_profiles_aggregate_bandwidth import QosProfilesAggregateBandwidth

# TODO update the JSON string below
json = "{}"
# create an instance of QosProfilesAggregateBandwidth from a JSON string
qos_profiles_aggregate_bandwidth_instance = QosProfilesAggregateBandwidth.from_json(json)
# print the JSON string representation of the object
print(QosProfilesAggregateBandwidth.to_json())

# convert the object into a dict
qos_profiles_aggregate_bandwidth_dict = qos_profiles_aggregate_bandwidth_instance.to_dict()
# create an instance of QosProfilesAggregateBandwidth from a dict
qos_profiles_aggregate_bandwidth_from_dict = QosProfilesAggregateBandwidth.from_dict(qos_profiles_aggregate_bandwidth_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


