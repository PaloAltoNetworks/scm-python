# NgfirewallLogConfig

Log destination configuration for the firewall.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_id** | **str** | The AWS account ID where logs are sent. | [optional] 
**log_destination** | **str** | The ARN or name of the log destination resource. | [optional] 
**log_destination_region** | **str** | The AWS region of the log destination. | [optional] 
**log_destination_type** | **str** | The type of log destination. | [optional] 
**log_type** | **List[str]** | The types of logs to send to this destination. | [optional] 
**role_type** | **str** | The IAM role type used to publish logs. | [optional] 

## Example

```python
from scm.cloud_ngfw.models.ngfirewall_log_config import NgfirewallLogConfig

# TODO update the JSON string below
json = "{}"
# create an instance of NgfirewallLogConfig from a JSON string
ngfirewall_log_config_instance = NgfirewallLogConfig.from_json(json)
# print the JSON string representation of the object
print(NgfirewallLogConfig.to_json())

# convert the object into a dict
ngfirewall_log_config_dict = ngfirewall_log_config_instance.to_dict()
# create an instance of NgfirewallLogConfig from a dict
ngfirewall_log_config_from_dict = NgfirewallLogConfig.from_dict(ngfirewall_log_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


