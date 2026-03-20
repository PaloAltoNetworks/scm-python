# LogicalRoutersVrfInnerBgpPolicyImport


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rules** | [**List[LogicalRoutersVrfInnerBgpPolicyImportRulesInner]**](LogicalRoutersVrfInnerBgpPolicyImportRulesInner.md) |  | [optional] 

## Example

```python
from scm.network_services.models.logical_routers_vrf_inner_bgp_policy_import import LogicalRoutersVrfInnerBgpPolicyImport

# TODO update the JSON string below
json = "{}"
# create an instance of LogicalRoutersVrfInnerBgpPolicyImport from a JSON string
logical_routers_vrf_inner_bgp_policy_import_instance = LogicalRoutersVrfInnerBgpPolicyImport.from_json(json)
# print the JSON string representation of the object
print(LogicalRoutersVrfInnerBgpPolicyImport.to_json())

# convert the object into a dict
logical_routers_vrf_inner_bgp_policy_import_dict = logical_routers_vrf_inner_bgp_policy_import_instance.to_dict()
# create an instance of LogicalRoutersVrfInnerBgpPolicyImport from a dict
logical_routers_vrf_inner_bgp_policy_import_from_dict = LogicalRoutersVrfInnerBgpPolicyImport.from_dict(logical_routers_vrf_inner_bgp_policy_import_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


