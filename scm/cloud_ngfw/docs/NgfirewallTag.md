# NgfirewallTag

A key-value tag applied to the firewall AWS resource.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | The tag key. | [optional] 
**value** | **str** | The tag value. | [optional] 

## Example

```python
from scm.cloud_ngfw.models.ngfirewall_tag import NgfirewallTag

# TODO update the JSON string below
json = "{}"
# create an instance of NgfirewallTag from a JSON string
ngfirewall_tag_instance = NgfirewallTag.from_json(json)
# print the JSON string representation of the object
print(NgfirewallTag.to_json())

# convert the object into a dict
ngfirewall_tag_dict = ngfirewall_tag_instance.to_dict()
# create an instance of NgfirewallTag from a dict
ngfirewall_tag_from_dict = NgfirewallTag.from_dict(ngfirewall_tag_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


