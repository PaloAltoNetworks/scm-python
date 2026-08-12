# NgfirewallEgressNatSettings

Settings for egress NAT IP address management.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ipam_pool_id** | **str** | The IPAM pool ID used for egress NAT IP allocation. | [optional] 
**ip_pool_type** | **str** | The IP pool type for egress NAT. | [optional] 

## Example

```python
from scm.cloud_ngfw.models.ngfirewall_egress_nat_settings import NgfirewallEgressNatSettings

# TODO update the JSON string below
json = "{}"
# create an instance of NgfirewallEgressNatSettings from a JSON string
ngfirewall_egress_nat_settings_instance = NgfirewallEgressNatSettings.from_json(json)
# print the JSON string representation of the object
print(NgfirewallEgressNatSettings.to_json())

# convert the object into a dict
ngfirewall_egress_nat_settings_dict = ngfirewall_egress_nat_settings_instance.to_dict()
# create an instance of NgfirewallEgressNatSettings from a dict
ngfirewall_egress_nat_settings_from_dict = NgfirewallEgressNatSettings.from_dict(ngfirewall_egress_nat_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


