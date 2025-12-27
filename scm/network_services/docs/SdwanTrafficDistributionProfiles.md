# SdwanTrafficDistributionProfiles


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**device** | **str** | The device in which the resource is defined | [optional] 
**folder** | **str** | The folder in which the resource is defined | [optional] 
**id** | **str** | UUID of the resource | [optional] [readonly] 
**link_tags** | [**List[SdwanTrafficDistributionProfilesLinkTagsInner]**](SdwanTrafficDistributionProfilesLinkTagsInner.md) | Link-Tags for interfaces identified by defined tags | [optional] 
**name** | **str** | Profile name | 
**snippet** | **str** | The snippet in which the resource is defined | [optional] 
**traffic_distribution** | **str** | Traffic distribution | [optional] [default to 'Best Available Path']

## Example

```python
from scm.network_services.models.sdwan_traffic_distribution_profiles import SdwanTrafficDistributionProfiles

# TODO update the JSON string below
json = "{}"
# create an instance of SdwanTrafficDistributionProfiles from a JSON string
sdwan_traffic_distribution_profiles_instance = SdwanTrafficDistributionProfiles.from_json(json)
# print the JSON string representation of the object
print(SdwanTrafficDistributionProfiles.to_json())

# convert the object into a dict
sdwan_traffic_distribution_profiles_dict = sdwan_traffic_distribution_profiles_instance.to_dict()
# create an instance of SdwanTrafficDistributionProfiles from a dict
sdwan_traffic_distribution_profiles_from_dict = SdwanTrafficDistributionProfiles.from_dict(sdwan_traffic_distribution_profiles_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


