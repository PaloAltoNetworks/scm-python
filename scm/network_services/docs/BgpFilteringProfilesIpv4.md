# BgpFilteringProfilesIpv4


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**multicast** | [**BgpFilteringProfilesIpv4Multicast**](BgpFilteringProfilesIpv4Multicast.md) |  | [optional] 
**unicast** | [**BgpFilter**](BgpFilter.md) |  | [optional] 

## Example

```python
from scm_network_services.models.bgp_filtering_profiles_ipv4 import BgpFilteringProfilesIpv4

# TODO update the JSON string below
json = "{}"
# create an instance of BgpFilteringProfilesIpv4 from a JSON string
bgp_filtering_profiles_ipv4_instance = BgpFilteringProfilesIpv4.from_json(json)
# print the JSON string representation of the object
print(BgpFilteringProfilesIpv4.to_json())

# convert the object into a dict
bgp_filtering_profiles_ipv4_dict = bgp_filtering_profiles_ipv4_instance.to_dict()
# create an instance of BgpFilteringProfilesIpv4 from a dict
bgp_filtering_profiles_ipv4_from_dict = BgpFilteringProfilesIpv4.from_dict(bgp_filtering_profiles_ipv4_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


