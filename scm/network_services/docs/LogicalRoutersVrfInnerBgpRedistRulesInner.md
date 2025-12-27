# LogicalRoutersVrfInnerBgpRedistRulesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address_family_identifier** | **str** |  | [optional] 
**enable** | **bool** |  | [optional] 
**metric** | **int** |  | [optional] 
**name** | **str** |  | 
**route_table** | **str** |  | [optional] 
**set_as_path_limit** | **int** |  | [optional] 
**set_community** | **List[str]** |  | [optional] 
**set_extended_community** | **List[str]** |  | [optional] 
**set_local_preference** | **int** |  | [optional] 
**set_med** | **int** |  | [optional] 
**set_origin** | **str** |  | [optional] 

## Example

```python
from scm_network_services.models.logical_routers_vrf_inner_bgp_redist_rules_inner import LogicalRoutersVrfInnerBgpRedistRulesInner

# TODO update the JSON string below
json = "{}"
# create an instance of LogicalRoutersVrfInnerBgpRedistRulesInner from a JSON string
logical_routers_vrf_inner_bgp_redist_rules_inner_instance = LogicalRoutersVrfInnerBgpRedistRulesInner.from_json(json)
# print the JSON string representation of the object
print(LogicalRoutersVrfInnerBgpRedistRulesInner.to_json())

# convert the object into a dict
logical_routers_vrf_inner_bgp_redist_rules_inner_dict = logical_routers_vrf_inner_bgp_redist_rules_inner_instance.to_dict()
# create an instance of LogicalRoutersVrfInnerBgpRedistRulesInner from a dict
logical_routers_vrf_inner_bgp_redist_rules_inner_from_dict = LogicalRoutersVrfInnerBgpRedistRulesInner.from_dict(logical_routers_vrf_inner_bgp_redist_rules_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


