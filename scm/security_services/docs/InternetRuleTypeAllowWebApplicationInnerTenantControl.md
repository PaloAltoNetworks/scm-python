# InternetRuleTypeAllowWebApplicationInnerTenantControl


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allowed_activities** | **List[str]** |  | [optional] 
**blocked_activities** | **List[str]** |  | [optional] 
**parent_application** | **str** |  | [optional] 
**tenants** | **List[str]** |  | [optional] 

## Example

```python
from scm.security_services.models.internet_rule_type_allow_web_application_inner_tenant_control import InternetRuleTypeAllowWebApplicationInnerTenantControl

# TODO update the JSON string below
json = "{}"
# create an instance of InternetRuleTypeAllowWebApplicationInnerTenantControl from a JSON string
internet_rule_type_allow_web_application_inner_tenant_control_instance = InternetRuleTypeAllowWebApplicationInnerTenantControl.from_json(json)
# print the JSON string representation of the object
print(InternetRuleTypeAllowWebApplicationInnerTenantControl.to_json())

# convert the object into a dict
internet_rule_type_allow_web_application_inner_tenant_control_dict = internet_rule_type_allow_web_application_inner_tenant_control_instance.to_dict()
# create an instance of InternetRuleTypeAllowWebApplicationInnerTenantControl from a dict
internet_rule_type_allow_web_application_inner_tenant_control_from_dict = InternetRuleTypeAllowWebApplicationInnerTenantControl.from_dict(internet_rule_type_allow_web_application_inner_tenant_control_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


