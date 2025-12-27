# SaasTenantRestrictionsHeadersInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**header** | **str** | Header string associated with the tenant restriction (example - Restrict-Access-To-Tenants, Restrict-Access-Context, X-Dropbox-allowed-Team-Ids, YouTube-Restrict, X-GooGApps-Allowed-Domains) | [optional] 
**name** | **str** | Header name associated with tenant restrictions (example - Permitted Tenant List, Tenant Directory ID) | [optional] 
**value** | **str** | Header value associated with tenant restriction (example - tenant1,tenant2,strict etc.) | [optional] 

## Example

```python
from scm.security_services.models.saas_tenant_restrictions_headers_inner import SaasTenantRestrictionsHeadersInner

# TODO update the JSON string below
json = "{}"
# create an instance of SaasTenantRestrictionsHeadersInner from a JSON string
saas_tenant_restrictions_headers_inner_instance = SaasTenantRestrictionsHeadersInner.from_json(json)
# print the JSON string representation of the object
print(SaasTenantRestrictionsHeadersInner.to_json())

# convert the object into a dict
saas_tenant_restrictions_headers_inner_dict = saas_tenant_restrictions_headers_inner_instance.to_dict()
# create an instance of SaasTenantRestrictionsHeadersInner from a dict
saas_tenant_restrictions_headers_inner_from_dict = SaasTenantRestrictionsHeadersInner.from_dict(saas_tenant_restrictions_headers_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


