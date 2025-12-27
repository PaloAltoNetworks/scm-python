# SdwanPathQualityProfilesMetricPktLoss


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sensitivity** | **str** | Packet loss sensitivity | [default to 'medium']
**threshold** | **int** | Packet loss threshold (percentage) | [default to 1]

## Example

```python
from scm.network_services.models.sdwan_path_quality_profiles_metric_pkt_loss import SdwanPathQualityProfilesMetricPktLoss

# TODO update the JSON string below
json = "{}"
# create an instance of SdwanPathQualityProfilesMetricPktLoss from a JSON string
sdwan_path_quality_profiles_metric_pkt_loss_instance = SdwanPathQualityProfilesMetricPktLoss.from_json(json)
# print the JSON string representation of the object
print(SdwanPathQualityProfilesMetricPktLoss.to_json())

# convert the object into a dict
sdwan_path_quality_profiles_metric_pkt_loss_dict = sdwan_path_quality_profiles_metric_pkt_loss_instance.to_dict()
# create an instance of SdwanPathQualityProfilesMetricPktLoss from a dict
sdwan_path_quality_profiles_metric_pkt_loss_from_dict = SdwanPathQualityProfilesMetricPktLoss.from_dict(sdwan_path_quality_profiles_metric_pkt_loss_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


