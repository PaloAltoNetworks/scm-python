# LogicalRoutersVrfInnerOspfAreaInnerTypeStub


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**abr** | [**LogicalRoutersVrfInnerOspfAreaInnerTypeNormalAbr**](LogicalRoutersVrfInnerOspfAreaInnerTypeNormalAbr.md) |  | [optional] 
**accept_summary** | **bool** |  | [optional] 
**default_route** | [**LogicalRoutersVrfInnerOspfAreaInnerTypeStubDefaultRoute**](LogicalRoutersVrfInnerOspfAreaInnerTypeStubDefaultRoute.md) |  | [optional] 
**default_route_metric** | **int** |  | [optional] 
**no_summary** | **bool** |  | [optional] 

## Example

```python
from scm_network_services.models.logical_routers_vrf_inner_ospf_area_inner_type_stub import LogicalRoutersVrfInnerOspfAreaInnerTypeStub

# TODO update the JSON string below
json = "{}"
# create an instance of LogicalRoutersVrfInnerOspfAreaInnerTypeStub from a JSON string
logical_routers_vrf_inner_ospf_area_inner_type_stub_instance = LogicalRoutersVrfInnerOspfAreaInnerTypeStub.from_json(json)
# print the JSON string representation of the object
print(LogicalRoutersVrfInnerOspfAreaInnerTypeStub.to_json())

# convert the object into a dict
logical_routers_vrf_inner_ospf_area_inner_type_stub_dict = logical_routers_vrf_inner_ospf_area_inner_type_stub_instance.to_dict()
# create an instance of LogicalRoutersVrfInnerOspfAreaInnerTypeStub from a dict
logical_routers_vrf_inner_ospf_area_inner_type_stub_from_dict = LogicalRoutersVrfInnerOspfAreaInnerTypeStub.from_dict(logical_routers_vrf_inner_ospf_area_inner_type_stub_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


