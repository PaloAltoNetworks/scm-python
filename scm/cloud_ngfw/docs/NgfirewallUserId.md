# NgfirewallUserId

User-ID configuration for user-based policy enforcement.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**agent_name** | **str** | The name of the User-ID agent. | [optional] 
**cfturl_link** | **str** | CloudFormation template URL link for User-ID setup. | [optional] 
**collector_name** | **str** | The name of the log collector used by User-ID. | [optional] 
**custom_include_exclude_network** | [**List[NgfirewallUserIdNetwork]**](NgfirewallUserIdNetwork.md) | Custom include/exclude network definitions for User-ID. | [optional] 
**enabled** | **bool** | Whether User-ID is enabled. | [optional] 
**endpoint_dns** | **str** | DNS name of the User-ID endpoint. | [optional] 
**port** | **int** | Port used by the User-ID agent. | [optional] 
**secret_key_arn** | **str** | ARN of the AWS Secrets Manager secret for User-ID credentials. | [optional] 
**user_id_status** | **str** | The operational status of the User-ID feature. | [optional] 

## Example

```python
from scm.cloud_ngfw.models.ngfirewall_user_id import NgfirewallUserId

# TODO update the JSON string below
json = "{}"
# create an instance of NgfirewallUserId from a JSON string
ngfirewall_user_id_instance = NgfirewallUserId.from_json(json)
# print the JSON string representation of the object
print(NgfirewallUserId.to_json())

# convert the object into a dict
ngfirewall_user_id_dict = ngfirewall_user_id_instance.to_dict()
# create an instance of NgfirewallUserId from a dict
ngfirewall_user_id_from_dict = NgfirewallUserId.from_dict(ngfirewall_user_id_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


