# BGPRouteMapRedistributionsListResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[BgpRouteMapRedistributions]**](BgpRouteMapRedistributions.md) |  | 
**limit** | **int** | The maximum number of results per page | [default to 200]
**offset** | **int** | The offset into the list of results returned | [default to 0]
**total** | **int** | The total count of results | 

## Example

```python
from scm.network_services.models.bgp_route_map_redistributions_list_response import BGPRouteMapRedistributionsListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of BGPRouteMapRedistributionsListResponse from a JSON string
bgp_route_map_redistributions_list_response_instance = BGPRouteMapRedistributionsListResponse.from_json(json)
# print the JSON string representation of the object
print(BGPRouteMapRedistributionsListResponse.to_json())

# convert the object into a dict
bgp_route_map_redistributions_list_response_dict = bgp_route_map_redistributions_list_response_instance.to_dict()
# create an instance of BGPRouteMapRedistributionsListResponse from a dict
bgp_route_map_redistributions_list_response_from_dict = BGPRouteMapRedistributionsListResponse.from_dict(bgp_route_map_redistributions_list_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


