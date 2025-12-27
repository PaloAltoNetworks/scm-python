# BgpRedistributionProfiles


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**device** | **str** | The device in which the resource is defined | [optional] 
**folder** | **str** | The folder in which the resource is defined | [optional] 
**id** | **str** | UUID of the resource | [optional] [readonly] 
**ipv4** | [**BgpRedistributionProfilesIpv4**](BgpRedistributionProfilesIpv4.md) |  | 
**name** | **str** | Name | 
**snippet** | **str** | The snippet in which the resource is defined | [optional] 

## Example

```python
from scm_network_services.models.bgp_redistribution_profiles import BgpRedistributionProfiles

# TODO update the JSON string below
json = "{}"
# create an instance of BgpRedistributionProfiles from a JSON string
bgp_redistribution_profiles_instance = BgpRedistributionProfiles.from_json(json)
# print the JSON string representation of the object
print(BgpRedistributionProfiles.to_json())

# convert the object into a dict
bgp_redistribution_profiles_dict = bgp_redistribution_profiles_instance.to_dict()
# create an instance of BgpRedistributionProfiles from a dict
bgp_redistribution_profiles_from_dict = BgpRedistributionProfiles.from_dict(bgp_redistribution_profiles_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


