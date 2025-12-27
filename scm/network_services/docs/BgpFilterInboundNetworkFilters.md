# BgpFilterInboundNetworkFilters


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**distribute_list** | **str** |  | [optional] 
**prefix_list** | **str** |  | [optional] 

## Example

```python
from scm_network_services.models.bgp_filter_inbound_network_filters import BgpFilterInboundNetworkFilters

# TODO update the JSON string below
json = "{}"
# create an instance of BgpFilterInboundNetworkFilters from a JSON string
bgp_filter_inbound_network_filters_instance = BgpFilterInboundNetworkFilters.from_json(json)
# print the JSON string representation of the object
print(BgpFilterInboundNetworkFilters.to_json())

# convert the object into a dict
bgp_filter_inbound_network_filters_dict = bgp_filter_inbound_network_filters_instance.to_dict()
# create an instance of BgpFilterInboundNetworkFilters from a dict
bgp_filter_inbound_network_filters_from_dict = BgpFilterInboundNetworkFilters.from_dict(bgp_filter_inbound_network_filters_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


