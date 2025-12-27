# BgpFilteringProfilesIpv4Multicast


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**conditional_advertisement** | [**BgpFilterConditionalAdvertisement**](BgpFilterConditionalAdvertisement.md) |  | [optional] 
**filter_list** | [**BgpFilterFilterList**](BgpFilterFilterList.md) |  | [optional] 
**inbound_network_filters** | [**BgpFilterInboundNetworkFilters**](BgpFilterInboundNetworkFilters.md) |  | [optional] 
**inherit** | **bool** | Inherit from unicast | [optional] 
**outbound_network_filters** | [**BgpFilterInboundNetworkFilters**](BgpFilterInboundNetworkFilters.md) |  | [optional] 
**route_maps** | [**BgpFilterFilterList**](BgpFilterFilterList.md) |  | [optional] 
**unsuppress_map** | **str** |  | [optional] 

## Example

```python
from scm_network_services.models.bgp_filtering_profiles_ipv4_multicast import BgpFilteringProfilesIpv4Multicast

# TODO update the JSON string below
json = "{}"
# create an instance of BgpFilteringProfilesIpv4Multicast from a JSON string
bgp_filtering_profiles_ipv4_multicast_instance = BgpFilteringProfilesIpv4Multicast.from_json(json)
# print the JSON string representation of the object
print(BgpFilteringProfilesIpv4Multicast.to_json())

# convert the object into a dict
bgp_filtering_profiles_ipv4_multicast_dict = bgp_filtering_profiles_ipv4_multicast_instance.to_dict()
# create an instance of BgpFilteringProfilesIpv4Multicast from a dict
bgp_filtering_profiles_ipv4_multicast_from_dict = BgpFilteringProfilesIpv4Multicast.from_dict(bgp_filtering_profiles_ipv4_multicast_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


