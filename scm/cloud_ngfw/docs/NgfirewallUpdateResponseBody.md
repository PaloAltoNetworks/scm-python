# NgfirewallUpdateResponseBody

Inner response body returned after updating a Cloud NGFW firewall.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allow_list_accounts** | **List[str]** | AWS account IDs permitted to access the firewall endpoint service. | [optional] 
**change_protection** | **List[str]** | List of attributes protected from change. | [optional] 
**customer_zone_id_list** | **List[str]** | List of customer-defined security zone IDs. | [optional] 
**deployment_update_token** | **str** | Updated deployment token for subsequent operations. | [optional] 
**description** | **str** | A human-readable description of the firewall. | [optional] 
**egress_nat** | [**NgfirewallEgressNatConfig**](NgfirewallEgressNatConfig.md) |  | [optional] 
**firewall_id** | **str** | The unique identifier of the firewall. | [optional] 
**gwlb** | [**NgfirewallGwlbConfig**](NgfirewallGwlbConfig.md) |  | [optional] 
**ipv6** | [**NgfirewallIpv6Config**](NgfirewallIpv6Config.md) |  | [optional] 
**mode** | **str** | The operational mode of the firewall. | [optional] 
**region** | **str** | The AWS region where the firewall is deployed. | [optional] 
**scm_labels** | **List[str]** | Strata Cloud Manager (SCM) labels applied to the firewall. | [optional] 
**tags** | [**List[NgfirewallTag]**](NgfirewallTag.md) | AWS resource tags applied to the firewall. | [optional] 
**tier** | **str** | The tier of the firewall. | [optional] 
**update_token** | **str** | Updated optimistic locking token for subsequent operations. | [optional] 

## Example

```python
from scm.cloud_ngfw.models.ngfirewall_update_response_body import NgfirewallUpdateResponseBody

# TODO update the JSON string below
json = "{}"
# create an instance of NgfirewallUpdateResponseBody from a JSON string
ngfirewall_update_response_body_instance = NgfirewallUpdateResponseBody.from_json(json)
# print the JSON string representation of the object
print(NgfirewallUpdateResponseBody.to_json())

# convert the object into a dict
ngfirewall_update_response_body_dict = ngfirewall_update_response_body_instance.to_dict()
# create an instance of NgfirewallUpdateResponseBody from a dict
ngfirewall_update_response_body_from_dict = NgfirewallUpdateResponseBody.from_dict(ngfirewall_update_response_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


