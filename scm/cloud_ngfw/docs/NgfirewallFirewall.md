# NgfirewallFirewall

Core firewall configuration and identity fields.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**advanced_threat_log** | **bool** | Whether advanced threat logging is enabled. | [optional] 
**allow_list_accounts** | **List[str]** | AWS account IDs permitted to access the firewall endpoint service. | [optional] 
**change_protection** | **List[str]** | List of attributes protected from change. | [optional] 
**cloudwatch_metrics** | [**NgfirewallCloudwatchMetrics**](NgfirewallCloudwatchMetrics.md) |  | [optional] 
**customer_zone_id_list** | **List[str]** | List of customer-defined security zone IDs. | [optional] 
**deployment_update_token** | **str** | Token used for deployment update sequencing. | [optional] 
**description** | **str** | A human-readable description of the firewall. | [optional] 
**device_rule_stack_commit_status** | **str** | Commit status of the device rulestack on the firewall. | [optional] 
**egress_nat** | [**NgfirewallEgressNatConfig**](NgfirewallEgressNatConfig.md) |  | [optional] 
**endpoint_service_name** | **str** | The VPC endpoint service name (only populated in ServiceManaged mode). | [optional] 
**endpoints** | [**List[NgfirewallEndpoint]**](NgfirewallEndpoint.md) | VPC endpoint configurations created for this firewall. | [optional] 
**firewall_id** | **str** | The unique identifier of the firewall. | [optional] 
**gwlb** | [**NgfirewallGwlbConfig**](NgfirewallGwlbConfig.md) |  | [optional] 
**global_rule_stack_name** | **str** | The name of the global rulestack associated with the firewall. | [optional] 
**ipv6** | [**NgfirewallIpv6Config**](NgfirewallIpv6Config.md) |  | [optional] 
**link_id** | **str** | The link ID associated with the firewall. | [optional] 
**link_status** | **str** | The current link status of the firewall. | [optional] 
**log_config** | [**NgfirewallLogConfig**](NgfirewallLogConfig.md) |  | [optional] 
**notifications** | [**List[NgfirewallNotification]**](NgfirewallNotification.md) | Notifications associated with this firewall. | [optional] 
**private_access** | [**NgfirewallPrivateAccess**](NgfirewallPrivateAccess.md) |  | [optional] 
**region** | **str** | The AWS region where the firewall is deployed. | [optional] 
**rule_stack_name** | **str** | The name of the local rulestack associated with the firewall. | [optional] 
**software_version** | **str** | The PAN-OS software version currently running on the firewall. | [optional] 
**tags** | [**List[NgfirewallTag]**](NgfirewallTag.md) | AWS resource tags applied to the firewall. | [optional] 
**tier** | **str** | The service tier of the firewall (e.g. base, premium). | [optional] 
**update_token** | **str** | Optimistic locking token; must be supplied on update operations. | [optional] 
**user_id** | [**NgfirewallUserId**](NgfirewallUserId.md) |  | [optional] 

## Example

```python
from scm.cloud_ngfw.models.ngfirewall_firewall import NgfirewallFirewall

# TODO update the JSON string below
json = "{}"
# create an instance of NgfirewallFirewall from a JSON string
ngfirewall_firewall_instance = NgfirewallFirewall.from_json(json)
# print the JSON string representation of the object
print(NgfirewallFirewall.to_json())

# convert the object into a dict
ngfirewall_firewall_dict = ngfirewall_firewall_instance.to_dict()
# create an instance of NgfirewallFirewall from a dict
ngfirewall_firewall_from_dict = NgfirewallFirewall.from_dict(ngfirewall_firewall_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


