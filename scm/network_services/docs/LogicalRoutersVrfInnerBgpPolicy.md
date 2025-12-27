# LogicalRoutersVrfInnerBgpPolicy


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**aggregation** | [**LogicalRoutersVrfInnerBgpPolicyAggregation**](LogicalRoutersVrfInnerBgpPolicyAggregation.md) |  | [optional] 
**conditional_advertisement** | [**LogicalRoutersVrfInnerBgpPolicyConditionalAdvertisement**](LogicalRoutersVrfInnerBgpPolicyConditionalAdvertisement.md) |  | [optional] 
**export** | [**LogicalRoutersVrfInnerBgpPolicyExport**](LogicalRoutersVrfInnerBgpPolicyExport.md) |  | [optional] 
**var_import** | [**LogicalRoutersVrfInnerBgpPolicyImport**](LogicalRoutersVrfInnerBgpPolicyImport.md) |  | [optional] 

## Example

```python
from scm_network_services.models.logical_routers_vrf_inner_bgp_policy import LogicalRoutersVrfInnerBgpPolicy

# TODO update the JSON string below
json = "{}"
# create an instance of LogicalRoutersVrfInnerBgpPolicy from a JSON string
logical_routers_vrf_inner_bgp_policy_instance = LogicalRoutersVrfInnerBgpPolicy.from_json(json)
# print the JSON string representation of the object
print(LogicalRoutersVrfInnerBgpPolicy.to_json())

# convert the object into a dict
logical_routers_vrf_inner_bgp_policy_dict = logical_routers_vrf_inner_bgp_policy_instance.to_dict()
# create an instance of LogicalRoutersVrfInnerBgpPolicy from a dict
logical_routers_vrf_inner_bgp_policy_from_dict = LogicalRoutersVrfInnerBgpPolicy.from_dict(logical_routers_vrf_inner_bgp_policy_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


