# NgfirewallStatus

Operational status of the firewall.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**device_rule_stack_commit_info** | [**NgfirewallCommitInfo**](NgfirewallCommitInfo.md) |  | [optional] 
**device_rule_stack_commit_state** | **str** | The commit state of the device rulestack. | [optional] 
**device_rule_stack_commit_status** | **str** | The commit status of the device rulestack. | [optional] 
**failure_reason** | **str** | Human-readable reason for a firewall failure, if any. | [optional] 
**firewall_status** | **str** | The operational lifecycle status of the firewall. | [optional] 
**global_rule_stack_commit_info** | [**NgfirewallCommitInfo**](NgfirewallCommitInfo.md) |  | [optional] 
**global_rule_stack_status** | **str** | The commit status of the global rulestack. | [optional] 
**public_ips** | [**List[NgfirewallPublicIp]**](NgfirewallPublicIp.md) | Public IP addresses assigned to the firewall. | [optional] 
**rule_stack_commit_info** | [**NgfirewallCommitInfo**](NgfirewallCommitInfo.md) |  | [optional] 
**rule_stack_status** | **str** | The commit status of the local rulestack. | [optional] 
**scm_assoc_status** | **bool** | Whether the firewall is associated with Strata Cloud Manager. | [optional] 

## Example

```python
from scm.cloud_ngfw.models.ngfirewall_status import NgfirewallStatus

# TODO update the JSON string below
json = "{}"
# create an instance of NgfirewallStatus from a JSON string
ngfirewall_status_instance = NgfirewallStatus.from_json(json)
# print the JSON string representation of the object
print(NgfirewallStatus.to_json())

# convert the object into a dict
ngfirewall_status_dict = ngfirewall_status_instance.to_dict()
# create an instance of NgfirewallStatus from a dict
ngfirewall_status_from_dict = NgfirewallStatus.from_dict(ngfirewall_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


