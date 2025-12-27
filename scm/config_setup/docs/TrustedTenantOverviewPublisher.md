# TrustedTenantOverviewPublisher


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pending** | **int** |  | [optional] [readonly] 
**total** | **int** |  | [optional] [readonly] 

## Example

```python
from scm.config_setup.models.trusted_tenant_overview_publisher import TrustedTenantOverviewPublisher

# TODO update the JSON string below
json = "{}"
# create an instance of TrustedTenantOverviewPublisher from a JSON string
trusted_tenant_overview_publisher_instance = TrustedTenantOverviewPublisher.from_json(json)
# print the JSON string representation of the object
print(TrustedTenantOverviewPublisher.to_json())

# convert the object into a dict
trusted_tenant_overview_publisher_dict = trusted_tenant_overview_publisher_instance.to_dict()
# create an instance of TrustedTenantOverviewPublisher from a dict
trusted_tenant_overview_publisher_from_dict = TrustedTenantOverviewPublisher.from_dict(trusted_tenant_overview_publisher_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


