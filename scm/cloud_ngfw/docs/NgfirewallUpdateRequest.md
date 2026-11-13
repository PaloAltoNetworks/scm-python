# NgfirewallUpdateRequest

Request body for updating an existing Cloud NGFW firewall.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allow_list_accounts** | **List[str]** | AWS account IDs permitted to access the firewall endpoint service. | [optional] 
**change_protection** | **List[str]** | List of attributes protected from change. | [optional] 
**customer_zone_id_list** | **List[str]** | List of customer-defined security zone IDs. | [optional] 
**deployment_update_token** | **str** | Deployment update token from the last GET response. Required for update operations. | 
**description** | **str** | A human-readable description of the firewall. | [optional] 
**egress_nat** | [**NgfirewallEgressNatConfig**](NgfirewallEgressNatConfig.md) |  | [optional] 
**endpoints** | [**List[NgfirewallEndpoint]**](NgfirewallEndpoint.md) | Firewall endpoint configurations. | [optional] 
**gwlb_tcp_idle_timeout** | **int** | GWLB TCP idle timeout in seconds. | [optional] 
**link_id** | **str** | The link ID to associate with the firewall. | [optional] 
**private_access** | [**NgfirewallPrivateAccess**](NgfirewallPrivateAccess.md) |  | [optional] 
**scm_labels** | **List[str]** | Strata Cloud Manager (SCM) labels for categorizing the firewall. | [optional] 
**tags** | [**List[NgfirewallTag]**](NgfirewallTag.md) | AWS resource tags to apply to the firewall. | [optional] 
**tier** | **str** | The tier of the firewall. Can only upgrade (standard to premium), cannot downgrade. | [optional] 
**update_token** | **str** | Optimistic locking token from the last GET response. Required for update operations. | 
**user_id** | [**NgfirewallUserId**](NgfirewallUserId.md) |  | [optional] 

## Example

```python
from scm.cloud_ngfw.models.ngfirewall_update_request import NgfirewallUpdateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of NgfirewallUpdateRequest from a JSON string
ngfirewall_update_request_instance = NgfirewallUpdateRequest.from_json(json)
# print the JSON string representation of the object
print(NgfirewallUpdateRequest.to_json())

# convert the object into a dict
ngfirewall_update_request_dict = ngfirewall_update_request_instance.to_dict()
# create an instance of NgfirewallUpdateRequest from a dict
ngfirewall_update_request_from_dict = NgfirewallUpdateRequest.from_dict(ngfirewall_update_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


