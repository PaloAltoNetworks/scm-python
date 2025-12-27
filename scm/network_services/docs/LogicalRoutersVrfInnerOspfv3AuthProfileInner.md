# LogicalRoutersVrfInnerOspfv3AuthProfileInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ah** | [**LogicalRoutersVrfInnerOspfv3AuthProfileInnerAh**](LogicalRoutersVrfInnerOspfv3AuthProfileInnerAh.md) |  | [optional] 
**esp** | [**LogicalRoutersVrfInnerOspfv3AuthProfileInnerEsp**](LogicalRoutersVrfInnerOspfv3AuthProfileInnerEsp.md) |  | [optional] 
**name** | **str** |  | 
**spi** | **str** |  | [optional] 

## Example

```python
from scm_network_services.models.logical_routers_vrf_inner_ospfv3_auth_profile_inner import LogicalRoutersVrfInnerOspfv3AuthProfileInner

# TODO update the JSON string below
json = "{}"
# create an instance of LogicalRoutersVrfInnerOspfv3AuthProfileInner from a JSON string
logical_routers_vrf_inner_ospfv3_auth_profile_inner_instance = LogicalRoutersVrfInnerOspfv3AuthProfileInner.from_json(json)
# print the JSON string representation of the object
print(LogicalRoutersVrfInnerOspfv3AuthProfileInner.to_json())

# convert the object into a dict
logical_routers_vrf_inner_ospfv3_auth_profile_inner_dict = logical_routers_vrf_inner_ospfv3_auth_profile_inner_instance.to_dict()
# create an instance of LogicalRoutersVrfInnerOspfv3AuthProfileInner from a dict
logical_routers_vrf_inner_ospfv3_auth_profile_inner_from_dict = LogicalRoutersVrfInnerOspfv3AuthProfileInner.from_dict(logical_routers_vrf_inner_ospfv3_auth_profile_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


