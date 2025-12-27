# SdwanPathQualityProfilesMetricLatency


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sensitivity** | **str** | Latency sensitivity | [default to 'medium']
**threshold** | **int** | Latency threshold (ms) | [default to 100]

## Example

```python
from scm.network_services.models.sdwan_path_quality_profiles_metric_latency import SdwanPathQualityProfilesMetricLatency

# TODO update the JSON string below
json = "{}"
# create an instance of SdwanPathQualityProfilesMetricLatency from a JSON string
sdwan_path_quality_profiles_metric_latency_instance = SdwanPathQualityProfilesMetricLatency.from_json(json)
# print the JSON string representation of the object
print(SdwanPathQualityProfilesMetricLatency.to_json())

# convert the object into a dict
sdwan_path_quality_profiles_metric_latency_dict = sdwan_path_quality_profiles_metric_latency_instance.to_dict()
# create an instance of SdwanPathQualityProfilesMetricLatency from a dict
sdwan_path_quality_profiles_metric_latency_from_dict = SdwanPathQualityProfilesMetricLatency.from_dict(sdwan_path_quality_profiles_metric_latency_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


