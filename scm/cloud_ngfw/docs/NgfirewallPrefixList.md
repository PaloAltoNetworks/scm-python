# NgfirewallPrefixList

A list of CIDR prefixes.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cidrs** | **List[str]** | CIDR address blocks. | [optional] 

## Example

```python
from scm.cloud_ngfw.models.ngfirewall_prefix_list import NgfirewallPrefixList

# TODO update the JSON string below
json = "{}"
# create an instance of NgfirewallPrefixList from a JSON string
ngfirewall_prefix_list_instance = NgfirewallPrefixList.from_json(json)
# print the JSON string representation of the object
print(NgfirewallPrefixList.to_json())

# convert the object into a dict
ngfirewall_prefix_list_dict = ngfirewall_prefix_list_instance.to_dict()
# create an instance of NgfirewallPrefixList from a dict
ngfirewall_prefix_list_from_dict = NgfirewallPrefixList.from_dict(ngfirewall_prefix_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


