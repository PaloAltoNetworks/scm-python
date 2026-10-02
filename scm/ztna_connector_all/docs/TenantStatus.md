# TenantStatus


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** | Tenant status | 

## Example

```python
from scm.ztna_connector_all.models.tenant_status import TenantStatus

# TODO update the JSON string below
json = "{}"
# create an instance of TenantStatus from a JSON string
tenant_status_instance = TenantStatus.from_json(json)
# print the JSON string representation of the object
print(TenantStatus.to_json())

# convert the object into a dict
tenant_status_dict = tenant_status_instance.to_dict()
# create an instance of TenantStatus from a dict
tenant_status_from_dict = TenantStatus.from_dict(tenant_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


