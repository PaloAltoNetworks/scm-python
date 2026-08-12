# NgfirewallSummary

Cloud NGFW firewall summary schema. This is used as part of list response when describe is not requested. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**firewall_id** | **str** | The unique identifier of the firewall (present in summary list items). | [optional] 

## Example

```python
from scm.cloud_ngfw.models.ngfirewall_summary import NgfirewallSummary

# TODO update the JSON string below
json = "{}"
# create an instance of NgfirewallSummary from a JSON string
ngfirewall_summary_instance = NgfirewallSummary.from_json(json)
# print the JSON string representation of the object
print(NgfirewallSummary.to_json())

# convert the object into a dict
ngfirewall_summary_dict = ngfirewall_summary_instance.to_dict()
# create an instance of NgfirewallSummary from a dict
ngfirewall_summary_from_dict = NgfirewallSummary.from_dict(ngfirewall_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


