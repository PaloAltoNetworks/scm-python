# NgfirewallCreateRequest

Request body for creating a new Cloud NGFW firewall.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allow_list_accounts** | **List[str]** | AWS account IDs permitted to access the firewall endpoint service. | [optional] 
**change_protection** | **List[str]** | List of attributes protected from change. | [optional] 
**customer_zone_id_list** | **List[str]** | List of customer-defined security zone IDs. Required. | 
**description** | **str** | A human-readable description of the firewall. | [optional] 
**egress_nat** | [**NgfirewallEgressNatConfig**](NgfirewallEgressNatConfig.md) |  | [optional] 
**firewall_name** | **str** | The name for the new Cloud NGFW firewall. | 
**global_rule_stack_name** | **str** | The name of the global rulestack to associate with the firewall. | [optional] 
**link_id** | **str** | The link ID to associate with the firewall. | [optional] 
**mode** | **object** | The operational mode of the firewall. | [optional] 
**rule_stack_name** | **str** | The name of the local rulestack to associate with the firewall. | [optional] 
**scm_labels** | **List[str]** | SCM labels to apply to the firewall. | [optional] 
**tags** | [**List[NgfirewallTag]**](NgfirewallTag.md) | AWS resource tags to apply to the firewall. | [optional] 
**tier** | **object** | The service tier for the firewall. | [optional] 

## Example

```python
from scm.cloud_ngfw.models.ngfirewall_create_request import NgfirewallCreateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of NgfirewallCreateRequest from a JSON string
ngfirewall_create_request_instance = NgfirewallCreateRequest.from_json(json)
# print the JSON string representation of the object
print(NgfirewallCreateRequest.to_json())

# convert the object into a dict
ngfirewall_create_request_dict = ngfirewall_create_request_instance.to_dict()
# create an instance of NgfirewallCreateRequest from a dict
ngfirewall_create_request_from_dict = NgfirewallCreateRequest.from_dict(ngfirewall_create_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


