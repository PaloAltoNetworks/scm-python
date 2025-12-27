# BgpAddressFamilyProfiles


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**device** | **str** | The device in which the resource is defined | [optional] 
**folder** | **str** | The folder in which the resource is defined | [optional] 
**id** | **str** | UUID of the resource | [optional] [readonly] 
**ipv4** | [**BgpAddressFamilyProfilesIpv4**](BgpAddressFamilyProfilesIpv4.md) |  | [optional] 
**name** | **str** | Name | 
**snippet** | **str** | The snippet in which the resource is defined | [optional] 

## Example

```python
from scm_network_services.models.bgp_address_family_profiles import BgpAddressFamilyProfiles

# TODO update the JSON string below
json = "{}"
# create an instance of BgpAddressFamilyProfiles from a JSON string
bgp_address_family_profiles_instance = BgpAddressFamilyProfiles.from_json(json)
# print the JSON string representation of the object
print(BgpAddressFamilyProfiles.to_json())

# convert the object into a dict
bgp_address_family_profiles_dict = bgp_address_family_profiles_instance.to_dict()
# create an instance of BgpAddressFamilyProfiles from a dict
bgp_address_family_profiles_from_dict = BgpAddressFamilyProfiles.from_dict(bgp_address_family_profiles_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


