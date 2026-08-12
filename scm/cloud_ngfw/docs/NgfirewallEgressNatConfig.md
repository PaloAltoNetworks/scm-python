# NgfirewallEgressNatConfig

Egress NAT configuration for outbound traffic.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | **bool** | Whether egress NAT is enabled on this firewall. | [optional] 
**settings** | [**NgfirewallEgressNatSettings**](NgfirewallEgressNatSettings.md) |  | [optional] 

## Example

```python
from scm.cloud_ngfw.models.ngfirewall_egress_nat_config import NgfirewallEgressNatConfig

# TODO update the JSON string below
json = "{}"
# create an instance of NgfirewallEgressNatConfig from a JSON string
ngfirewall_egress_nat_config_instance = NgfirewallEgressNatConfig.from_json(json)
# print the JSON string representation of the object
print(NgfirewallEgressNatConfig.to_json())

# convert the object into a dict
ngfirewall_egress_nat_config_dict = ngfirewall_egress_nat_config_instance.to_dict()
# create an instance of NgfirewallEgressNatConfig from a dict
ngfirewall_egress_nat_config_from_dict = NgfirewallEgressNatConfig.from_dict(ngfirewall_egress_nat_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


