# SdwanPathQualityProfilesMetric


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**jitter** | [**SdwanPathQualityProfilesMetricJitter**](SdwanPathQualityProfilesMetricJitter.md) |  | 
**latency** | [**SdwanPathQualityProfilesMetricLatency**](SdwanPathQualityProfilesMetricLatency.md) |  | 
**pkt_loss** | [**SdwanPathQualityProfilesMetricPktLoss**](SdwanPathQualityProfilesMetricPktLoss.md) |  | [optional] 

## Example

```python
from scm_network_services.models.sdwan_path_quality_profiles_metric import SdwanPathQualityProfilesMetric

# TODO update the JSON string below
json = "{}"
# create an instance of SdwanPathQualityProfilesMetric from a JSON string
sdwan_path_quality_profiles_metric_instance = SdwanPathQualityProfilesMetric.from_json(json)
# print the JSON string representation of the object
print(SdwanPathQualityProfilesMetric.to_json())

# convert the object into a dict
sdwan_path_quality_profiles_metric_dict = sdwan_path_quality_profiles_metric_instance.to_dict()
# create an instance of SdwanPathQualityProfilesMetric from a dict
sdwan_path_quality_profiles_metric_from_dict = SdwanPathQualityProfilesMetric.from_dict(sdwan_path_quality_profiles_metric_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


