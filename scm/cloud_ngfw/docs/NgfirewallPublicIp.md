# NgfirewallPublicIp

A public IP address assigned to the firewall.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ip_address** | **str** | The public IP address. | [optional] 
**ip_source** | **str** | The source of the IP address allocation. | [optional] 
**ip_status** | **str** | The current status of this public IP. | [optional] 

## Example

```python
from scm.cloud_ngfw.models.ngfirewall_public_ip import NgfirewallPublicIp

# TODO update the JSON string below
json = "{}"
# create an instance of NgfirewallPublicIp from a JSON string
ngfirewall_public_ip_instance = NgfirewallPublicIp.from_json(json)
# print the JSON string representation of the object
print(NgfirewallPublicIp.to_json())

# convert the object into a dict
ngfirewall_public_ip_dict = ngfirewall_public_ip_instance.to_dict()
# create an instance of NgfirewallPublicIp from a dict
ngfirewall_public_ip_from_dict = NgfirewallPublicIp.from_dict(ngfirewall_public_ip_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


