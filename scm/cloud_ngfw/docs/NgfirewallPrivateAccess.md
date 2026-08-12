# NgfirewallPrivateAccess

Private access configuration for the firewall.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**resource_id** | **str** | The resource ID of the private access endpoint. | [optional] 
**type** | **str** | The type of private access resource. | [optional] 

## Example

```python
from scm.cloud_ngfw.models.ngfirewall_private_access import NgfirewallPrivateAccess

# TODO update the JSON string below
json = "{}"
# create an instance of NgfirewallPrivateAccess from a JSON string
ngfirewall_private_access_instance = NgfirewallPrivateAccess.from_json(json)
# print the JSON string representation of the object
print(NgfirewallPrivateAccess.to_json())

# convert the object into a dict
ngfirewall_private_access_dict = ngfirewall_private_access_instance.to_dict()
# create an instance of NgfirewallPrivateAccess from a dict
ngfirewall_private_access_from_dict = NgfirewallPrivateAccess.from_dict(ngfirewall_private_access_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


