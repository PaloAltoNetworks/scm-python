# TrustedTenantOverview


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**publisher** | [**TrustedTenantOverviewPublisher**](TrustedTenantOverviewPublisher.md) |  | [optional] 
**subscriber** | [**TrustedTenantOverviewPublisher**](TrustedTenantOverviewPublisher.md) |  | [optional] 

## Example

```python
from scm.config_setup.models.trusted_tenant_overview import TrustedTenantOverview

# TODO update the JSON string below
json = "{}"
# create an instance of TrustedTenantOverview from a JSON string
trusted_tenant_overview_instance = TrustedTenantOverview.from_json(json)
# print the JSON string representation of the object
print(TrustedTenantOverview.to_json())

# convert the object into a dict
trusted_tenant_overview_dict = trusted_tenant_overview_instance.to_dict()
# create an instance of TrustedTenantOverview from a dict
trusted_tenant_overview_from_dict = TrustedTenantOverview.from_dict(trusted_tenant_overview_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


