# InternetRuleType

A simplified security rule for controlling internet access.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **str** | The action to be taken when the rule is matched | [optional] 
**allow_url_category** | [**List[InternetRuleTypeAllowUrlCategoryInner]**](InternetRuleTypeAllowUrlCategoryInner.md) |  | [optional] 
**allow_web_application** | [**List[InternetRuleTypeAllowWebApplicationInner]**](InternetRuleTypeAllowWebApplicationInner.md) |  | [optional] 
**block_url_category** | **List[str]** |  | [optional] 
**block_web_application** | **List[str]** |  | [optional] 
**default_profile_settings** | [**InternetRuleTypeDefaultProfileSettings**](InternetRuleTypeDefaultProfileSettings.md) |  | [optional] 
**description** | **str** | The description of the security rule | [optional] 
**destination** | **List[str]** | The destination address(es) | [optional] 
**devices** | **List[str]** |  | [optional] [default to ["any"]]
**disabled** | **bool** | Is the security rule disabled? | [optional] [default to False]
**var_from** | **List[str]** | The source security zone(s) | [optional] 
**id** | **str** | The UUID of the security rule | [optional] [readonly] 
**log_settings** | [**InternetRuleTypeLogSettings**](InternetRuleTypeLogSettings.md) |  | [optional] 
**name** | **str** | The name of the security rule | 
**negate_source** | **bool** | Negate the source address(es)? | [optional] [default to False]
**negate_user** | **bool** |  | [optional] [default to False]
**policy_type** | **str** |  | [optional] [default to 'Security']
**schedule** | **str** | Schedule in which this rule will be applied | [optional] 
**security_settings** | [**InternetRuleTypeSecuritySettings**](InternetRuleTypeSecuritySettings.md) |  | [optional] 
**service** | **List[str]** | The service(s) being accessed | [optional] 
**source** | **List[str]** | The source addresses(es) | [optional] 
**source_user** | **List[str]** | List of source users and/or groups.  Reserved words include &#x60;any&#x60;, &#x60;pre-login&#x60;, &#x60;known-user&#x60;, and &#x60;unknown&#x60;. | [optional] 
**tag** | **List[str]** | The tags associated with the security rule | [optional] 
**to** | **List[str]** | The destination security zone(s) | [optional] 

## Example

```python
from scm.security_services.models.internet_rule_type import InternetRuleType

# TODO update the JSON string below
json = "{}"
# create an instance of InternetRuleType from a JSON string
internet_rule_type_instance = InternetRuleType.from_json(json)
# print the JSON string representation of the object
print(InternetRuleType.to_json())

# convert the object into a dict
internet_rule_type_dict = internet_rule_type_instance.to_dict()
# create an instance of InternetRuleType from a dict
internet_rule_type_from_dict = InternetRuleType.from_dict(internet_rule_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


