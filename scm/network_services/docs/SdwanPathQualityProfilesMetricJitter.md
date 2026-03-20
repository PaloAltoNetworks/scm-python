# SdwanPathQualityProfilesMetricJitter


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sensitivity** | **str** | Jitter sensitivity | [default to 'medium']
**threshold** | **int** | Jitter threshold (ms) | [default to 100]

## Example

```python
from scm.network_services.models.sdwan_path_quality_profiles_metric_jitter import SdwanPathQualityProfilesMetricJitter

# TODO update the JSON string below
json = "{}"
# create an instance of SdwanPathQualityProfilesMetricJitter from a JSON string
sdwan_path_quality_profiles_metric_jitter_instance = SdwanPathQualityProfilesMetricJitter.from_json(json)
# print the JSON string representation of the object
print(SdwanPathQualityProfilesMetricJitter.to_json())

# convert the object into a dict
sdwan_path_quality_profiles_metric_jitter_dict = sdwan_path_quality_profiles_metric_jitter_instance.to_dict()
# create an instance of SdwanPathQualityProfilesMetricJitter from a dict
sdwan_path_quality_profiles_metric_jitter_from_dict = SdwanPathQualityProfilesMetricJitter.from_dict(sdwan_path_quality_profiles_metric_jitter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


