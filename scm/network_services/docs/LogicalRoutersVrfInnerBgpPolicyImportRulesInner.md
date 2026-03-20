# LogicalRoutersVrfInnerBgpPolicyImportRulesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | [**LogicalRoutersVrfInnerBgpPolicyImportRulesInnerAction**](LogicalRoutersVrfInnerBgpPolicyImportRulesInnerAction.md) |  | [optional] 
**enable** | **bool** |  | [optional] 
**match** | [**LogicalRoutersVrfInnerBgpPolicyAggregationAddressInnerAdvertiseFiltersInnerMatch**](LogicalRoutersVrfInnerBgpPolicyAggregationAddressInnerAdvertiseFiltersInnerMatch.md) |  | [optional] 
**name** | **str** |  | 
**used_by** | **List[str]** |  | [optional] 

## Example

```python
from scm.network_services.models.logical_routers_vrf_inner_bgp_policy_import_rules_inner import LogicalRoutersVrfInnerBgpPolicyImportRulesInner

# TODO update the JSON string below
json = "{}"
# create an instance of LogicalRoutersVrfInnerBgpPolicyImportRulesInner from a JSON string
logical_routers_vrf_inner_bgp_policy_import_rules_inner_instance = LogicalRoutersVrfInnerBgpPolicyImportRulesInner.from_json(json)
# print the JSON string representation of the object
print(LogicalRoutersVrfInnerBgpPolicyImportRulesInner.to_json())

# convert the object into a dict
logical_routers_vrf_inner_bgp_policy_import_rules_inner_dict = logical_routers_vrf_inner_bgp_policy_import_rules_inner_instance.to_dict()
# create an instance of LogicalRoutersVrfInnerBgpPolicyImportRulesInner from a dict
logical_routers_vrf_inner_bgp_policy_import_rules_inner_from_dict = LogicalRoutersVrfInnerBgpPolicyImportRulesInner.from_dict(logical_routers_vrf_inner_bgp_policy_import_rules_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


