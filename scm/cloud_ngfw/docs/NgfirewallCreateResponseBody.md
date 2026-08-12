# NgfirewallCreateResponseBody

Inner response body returned after creating a Cloud NGFW firewall.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allow_list_accounts** | **List[str]** | AWS account IDs permitted to access the firewall endpoint service. | [optional] 
**change_protection** | **List[str]** | List of attributes protected from change. | [optional] 
**customer_zone_id_list** | **List[str]** | List of customer-defined security zone IDs. | [optional] 
**description** | **str** | A human-readable description of the firewall. | [optional] 
**egress_nat** | [**NgfirewallEgressNatConfig**](NgfirewallEgressNatConfig.md) |  | [optional] 
**firewall_id** | **str** | The unique identifier of the created firewall. | [optional] 
**global_rule_stack_name** | **str** | The name of the global rulestack associated with the firewall. | [optional] 
**link_id** | **str** | The link ID associated with the firewall. | [optional] 
**mode** | **object** | The operational mode of the firewall. | [optional] 
**rule_stack_name** | **str** | The name of the local rulestack associated with the firewall. | [optional] 
**scm_labels** | **List[str]** | SCM labels applied to the firewall. | [optional] 
**tags** | [**List[NgfirewallTag]**](NgfirewallTag.md) | AWS resource tags applied to the firewall. | [optional] 
**tier** | **object** | The service tier of the firewall. | [optional] 
**update_token** | **str** | Optimistic locking token for subsequent update operations. | [optional] 

## Example

```python
from scm.cloud_ngfw.models.ngfirewall_create_response_body import NgfirewallCreateResponseBody

# TODO update the JSON string below
json = "{}"
# create an instance of NgfirewallCreateResponseBody from a JSON string
ngfirewall_create_response_body_instance = NgfirewallCreateResponseBody.from_json(json)
# print the JSON string representation of the object
print(NgfirewallCreateResponseBody.to_json())

# convert the object into a dict
ngfirewall_create_response_body_dict = ngfirewall_create_response_body_instance.to_dict()
# create an instance of NgfirewallCreateResponseBody from a dict
ngfirewall_create_response_body_from_dict = NgfirewallCreateResponseBody.from_dict(ngfirewall_create_response_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


