# NgfirewallCloudwatchMetrics

CloudWatch metrics configuration.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_id** | **str** | The AWS account ID where CloudWatch metrics are published. | [optional] 
**cloud_watch_metric_namespace** | **str** | The CloudWatch metric namespace. | [optional] 
**cloud_watch_metrics_fields** | **List[str]** | The CloudWatch metric field names to publish. | [optional] 

## Example

```python
from scm.cloud_ngfw.models.ngfirewall_cloudwatch_metrics import NgfirewallCloudwatchMetrics

# TODO update the JSON string below
json = "{}"
# create an instance of NgfirewallCloudwatchMetrics from a JSON string
ngfirewall_cloudwatch_metrics_instance = NgfirewallCloudwatchMetrics.from_json(json)
# print the JSON string representation of the object
print(NgfirewallCloudwatchMetrics.to_json())

# convert the object into a dict
ngfirewall_cloudwatch_metrics_dict = ngfirewall_cloudwatch_metrics_instance.to_dict()
# create an instance of NgfirewallCloudwatchMetrics from a dict
ngfirewall_cloudwatch_metrics_from_dict = NgfirewallCloudwatchMetrics.from_dict(ngfirewall_cloudwatch_metrics_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


