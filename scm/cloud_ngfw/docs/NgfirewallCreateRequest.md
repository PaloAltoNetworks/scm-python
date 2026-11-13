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
**endpoints** | [**List[NgfirewallEndpoint]**](NgfirewallEndpoint.md) | Firewall endpoint configurations. Assigned by the service when the firewall is created; can be changed with an update. | [optional] 
**gwlb_tcp_idle_timeout** | **int** | GWLB TCP idle timeout in seconds. Defaults to 350; can be changed with an update. | [optional] 
**link_id** | **str** | The link ID to associate with the firewall. | [optional] 
**mode** | **str** | The operational mode of the firewall. Set when the firewall is created and cannot be changed afterward. | [optional] 
**private_access** | [**NgfirewallPrivateAccess**](NgfirewallPrivateAccess.md) |  | [optional] 
**scm_labels** | **List[str]** | Strata Cloud Manager (SCM) labels to apply to the firewall. | [optional] 
**source** | **str** | The source SDK or provider that created the firewall. Automatically set by the SDK or Terraform provider; do not set this field manually. | [optional] 
**tags** | [**List[NgfirewallTag]**](NgfirewallTag.md) | AWS resource tags to apply to the firewall. | [optional] 
**tier** | **str** | The service tier for the firewall, either standard or premium. | [optional] 
**user_id** | [**NgfirewallUserId**](NgfirewallUserId.md) |  | [optional] 

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


