# InternetRuleTypeAllowWebApplicationInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**application_function** | **List[str]** |  | [optional] 
**dlp** | **str** |  | [optional] 
**file_control** | [**InternetRuleTypeAllowUrlCategoryInnerFileControl**](InternetRuleTypeAllowUrlCategoryInnerFileControl.md) |  | [optional] 
**name** | **str** |  | [optional] 
**saas_enterprise_control** | [**InternetRuleTypeAllowWebApplicationInnerSaasEnterpriseControl**](InternetRuleTypeAllowWebApplicationInnerSaasEnterpriseControl.md) |  | [optional] 
**saas_tenant_list** | **List[str]** |  | [optional] 
**saas_user_list** | **List[str]** |  | [optional] 
**tenant_control** | [**InternetRuleTypeAllowWebApplicationInnerTenantControl**](InternetRuleTypeAllowWebApplicationInnerTenantControl.md) |  | [optional] 
**type** | **str** |  | [optional] 

## Example

```python
from scm.security_services.models.internet_rule_type_allow_web_application_inner import InternetRuleTypeAllowWebApplicationInner

# TODO update the JSON string below
json = "{}"
# create an instance of InternetRuleTypeAllowWebApplicationInner from a JSON string
internet_rule_type_allow_web_application_inner_instance = InternetRuleTypeAllowWebApplicationInner.from_json(json)
# print the JSON string representation of the object
print(InternetRuleTypeAllowWebApplicationInner.to_json())

# convert the object into a dict
internet_rule_type_allow_web_application_inner_dict = internet_rule_type_allow_web_application_inner_instance.to_dict()
# create an instance of InternetRuleTypeAllowWebApplicationInner from a dict
internet_rule_type_allow_web_application_inner_from_dict = InternetRuleTypeAllowWebApplicationInner.from_dict(internet_rule_type_allow_web_application_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


