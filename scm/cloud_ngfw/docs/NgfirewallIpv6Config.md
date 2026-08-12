# NgfirewallIpv6Config

IPv6 configuration for the firewall.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | **bool** | Whether IPv6 is enabled on this firewall. | [optional] 

## Example

```python
from scm.cloud_ngfw.models.ngfirewall_ipv6_config import NgfirewallIpv6Config

# TODO update the JSON string below
json = "{}"
# create an instance of NgfirewallIpv6Config from a JSON string
ngfirewall_ipv6_config_instance = NgfirewallIpv6Config.from_json(json)
# print the JSON string representation of the object
print(NgfirewallIpv6Config.to_json())

# convert the object into a dict
ngfirewall_ipv6_config_dict = ngfirewall_ipv6_config_instance.to_dict()
# create an instance of NgfirewallIpv6Config from a dict
ngfirewall_ipv6_config_from_dict = NgfirewallIpv6Config.from_dict(ngfirewall_ipv6_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


