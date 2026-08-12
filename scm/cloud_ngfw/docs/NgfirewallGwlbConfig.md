# NgfirewallGwlbConfig

Gateway Load Balancer configuration.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**deregistration_delay** | **int** | Deregistration delay in seconds. | [optional] [default to 300]
**rejected_flow_count_alert_threshold** | **int** | Alert threshold for the total rejected flow count. | [optional] [default to 10]
**rejected_flow_count_tcp_alert_threshold** | **int** | Alert threshold for the TCP rejected flow count. | [optional] [default to 10]
**session_rebalance_enabled** | **bool** | Whether session rebalancing is enabled. | [optional] [default to False]
**tcp_idle_timeout** | **int** | TCP idle timeout in seconds. | [optional] [default to 350]

## Example

```python
from scm.cloud_ngfw.models.ngfirewall_gwlb_config import NgfirewallGwlbConfig

# TODO update the JSON string below
json = "{}"
# create an instance of NgfirewallGwlbConfig from a JSON string
ngfirewall_gwlb_config_instance = NgfirewallGwlbConfig.from_json(json)
# print the JSON string representation of the object
print(NgfirewallGwlbConfig.to_json())

# convert the object into a dict
ngfirewall_gwlb_config_dict = ngfirewall_gwlb_config_instance.to_dict()
# create an instance of NgfirewallGwlbConfig from a dict
ngfirewall_gwlb_config_from_dict = NgfirewallGwlbConfig.from_dict(ngfirewall_gwlb_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


