# NgfirewallCommitInfo

Commit information for a rulestack.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**commit_messages** | **List[str]** | Messages produced during the commit operation. | [optional] 
**commit_ts** | **str** | Timestamp of the last commit operation. | [optional] 

## Example

```python
from scm.cloud_ngfw.models.ngfirewall_commit_info import NgfirewallCommitInfo

# TODO update the JSON string below
json = "{}"
# create an instance of NgfirewallCommitInfo from a JSON string
ngfirewall_commit_info_instance = NgfirewallCommitInfo.from_json(json)
# print the JSON string representation of the object
print(NgfirewallCommitInfo.to_json())

# convert the object into a dict
ngfirewall_commit_info_dict = ngfirewall_commit_info_instance.to_dict()
# create an instance of NgfirewallCommitInfo from a dict
ngfirewall_commit_info_from_dict = NgfirewallCommitInfo.from_dict(ngfirewall_commit_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


