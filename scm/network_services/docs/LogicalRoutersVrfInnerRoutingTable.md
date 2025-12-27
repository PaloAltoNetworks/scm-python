# LogicalRoutersVrfInnerRoutingTable


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ip** | [**LogicalRoutersVrfInnerRoutingTableIp**](LogicalRoutersVrfInnerRoutingTableIp.md) |  | [optional] 
**ipv6** | [**LogicalRoutersVrfInnerRoutingTableIpv6**](LogicalRoutersVrfInnerRoutingTableIpv6.md) |  | [optional] 

## Example

```python
from scm.network_services.models.logical_routers_vrf_inner_routing_table import LogicalRoutersVrfInnerRoutingTable

# TODO update the JSON string below
json = "{}"
# create an instance of LogicalRoutersVrfInnerRoutingTable from a JSON string
logical_routers_vrf_inner_routing_table_instance = LogicalRoutersVrfInnerRoutingTable.from_json(json)
# print the JSON string representation of the object
print(LogicalRoutersVrfInnerRoutingTable.to_json())

# convert the object into a dict
logical_routers_vrf_inner_routing_table_dict = logical_routers_vrf_inner_routing_table_instance.to_dict()
# create an instance of LogicalRoutersVrfInnerRoutingTable from a dict
logical_routers_vrf_inner_routing_table_from_dict = LogicalRoutersVrfInnerRoutingTable.from_dict(logical_routers_vrf_inner_routing_table_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


