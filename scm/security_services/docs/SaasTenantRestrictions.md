# SaasTenantRestrictions


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | Description associated with the tenant restriction (example - Microsoft 365 SaaS Security Restrictions, Dropbox SaaS Security Restrictions, YouTube Safe Search Restrictions, Google Apps SaaS Security Restrictions) | [optional] 
**domains** | **List[str]** | List of domains associated with tenant restrictions | [optional] 
**headers** | [**List[SaasTenantRestrictionsHeadersInner]**](SaasTenantRestrictionsHeadersInner.md) | List of headers associated with tenant restrictions | [optional] 
**name** | **str** | Name of the tenant restriction (example - Microsoft 365, Dropbox, YouTube Safe Search, Google Apps) | [optional] 
**saas_edl** | **List[str]** | List of EDL associated with tenant restrictions | [optional] 

## Example

```python
from scm_security_services.models.saas_tenant_restrictions import SaasTenantRestrictions

# TODO update the JSON string below
json = "{}"
# create an instance of SaasTenantRestrictions from a JSON string
saas_tenant_restrictions_instance = SaasTenantRestrictions.from_json(json)
# print the JSON string representation of the object
print(SaasTenantRestrictions.to_json())

# convert the object into a dict
saas_tenant_restrictions_dict = saas_tenant_restrictions_instance.to_dict()
# create an instance of SaasTenantRestrictions from a dict
saas_tenant_restrictions_from_dict = SaasTenantRestrictions.from_dict(saas_tenant_restrictions_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


