# NgfirewallUserIdNetwork

A single custom include/exclude network entry for User-ID.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**discovery_include** | **bool** | Whether this network is included in User-ID discovery. | [optional] 
**enabled** | **bool** | Whether this network entry is active. | [optional] 
**name** | **str** | Name of the network entry. | [optional] 
**network_address** | **str** | The network address (CIDR) for this entry. | [optional] 

## Example

```python
from scm.cloud_ngfw.models.ngfirewall_user_id_network import NgfirewallUserIdNetwork

# TODO update the JSON string below
json = "{}"
# create an instance of NgfirewallUserIdNetwork from a JSON string
ngfirewall_user_id_network_instance = NgfirewallUserIdNetwork.from_json(json)
# print the JSON string representation of the object
print(NgfirewallUserIdNetwork.to_json())

# convert the object into a dict
ngfirewall_user_id_network_dict = ngfirewall_user_id_network_instance.to_dict()
# create an instance of NgfirewallUserIdNetwork from a dict
ngfirewall_user_id_network_from_dict = NgfirewallUserIdNetwork.from_dict(ngfirewall_user_id_network_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


