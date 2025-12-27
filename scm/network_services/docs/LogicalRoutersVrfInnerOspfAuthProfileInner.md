# LogicalRoutersVrfInnerOspfAuthProfileInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**md5** | [**List[LogicalRoutersVrfInnerOspfAuthProfileInnerMd5Inner]**](LogicalRoutersVrfInnerOspfAuthProfileInnerMd5Inner.md) |  | [optional] 
**name** | **str** |  | 
**password** | **str** |  | [optional] 

## Example

```python
from scm_network_services.models.logical_routers_vrf_inner_ospf_auth_profile_inner import LogicalRoutersVrfInnerOspfAuthProfileInner

# TODO update the JSON string below
json = "{}"
# create an instance of LogicalRoutersVrfInnerOspfAuthProfileInner from a JSON string
logical_routers_vrf_inner_ospf_auth_profile_inner_instance = LogicalRoutersVrfInnerOspfAuthProfileInner.from_json(json)
# print the JSON string representation of the object
print(LogicalRoutersVrfInnerOspfAuthProfileInner.to_json())

# convert the object into a dict
logical_routers_vrf_inner_ospf_auth_profile_inner_dict = logical_routers_vrf_inner_ospf_auth_profile_inner_instance.to_dict()
# create an instance of LogicalRoutersVrfInnerOspfAuthProfileInner from a dict
logical_routers_vrf_inner_ospf_auth_profile_inner_from_dict = LogicalRoutersVrfInnerOspfAuthProfileInner.from_dict(logical_routers_vrf_inner_ospf_auth_profile_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


