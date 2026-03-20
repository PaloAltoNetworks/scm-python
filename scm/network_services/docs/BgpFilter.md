# BgpFilter


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**conditional_advertisement** | [**BgpFilterConditionalAdvertisement**](BgpFilterConditionalAdvertisement.md) |  | [optional] 
**filter_list** | [**BgpFilterFilterList**](BgpFilterFilterList.md) |  | [optional] 
**inbound_network_filters** | [**BgpFilterInboundNetworkFilters**](BgpFilterInboundNetworkFilters.md) |  | [optional] 
**outbound_network_filters** | [**BgpFilterInboundNetworkFilters**](BgpFilterInboundNetworkFilters.md) |  | [optional] 
**route_maps** | [**BgpFilterFilterList**](BgpFilterFilterList.md) |  | [optional] 
**unsuppress_map** | **str** |  | [optional] 

## Example

```python
from scm.network_services.models.bgp_filter import BgpFilter

# TODO update the JSON string below
json = "{}"
# create an instance of BgpFilter from a JSON string
bgp_filter_instance = BgpFilter.from_json(json)
# print the JSON string representation of the object
print(BgpFilter.to_json())

# convert the object into a dict
bgp_filter_dict = bgp_filter_instance.to_dict()
# create an instance of BgpFilter from a dict
bgp_filter_from_dict = BgpFilter.from_dict(bgp_filter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


