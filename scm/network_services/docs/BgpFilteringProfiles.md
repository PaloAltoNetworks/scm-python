# BgpFilteringProfiles


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** |  | [optional] 
**device** | **str** | The device in which the resource is defined | [optional] 
**folder** | **str** | The folder in which the resource is defined | [optional] 
**id** | **str** | UUID of the resource | [optional] [readonly] 
**ipv4** | [**BgpFilteringProfilesIpv4**](BgpFilteringProfilesIpv4.md) |  | [optional] 
**name** | **str** |  | 
**snippet** | **str** | The snippet in which the resource is defined | [optional] 

## Example

```python
from scm_network_services.models.bgp_filtering_profiles import BgpFilteringProfiles

# TODO update the JSON string below
json = "{}"
# create an instance of BgpFilteringProfiles from a JSON string
bgp_filtering_profiles_instance = BgpFilteringProfiles.from_json(json)
# print the JSON string representation of the object
print(BgpFilteringProfiles.to_json())

# convert the object into a dict
bgp_filtering_profiles_dict = bgp_filtering_profiles_instance.to_dict()
# create an instance of BgpFilteringProfiles from a dict
bgp_filtering_profiles_from_dict = BgpFilteringProfiles.from_dict(bgp_filtering_profiles_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


