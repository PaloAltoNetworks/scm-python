# SecurityRules

Represents a Security or Internet security rule. A rule must be one of the policy types AND exist in one scope (folder, snippet, or device).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **str** | The action to be taken when the rule is matched | [optional] 
**allow_url_category** | [**List[InternetRuleTypeAllowUrlCategoryInner]**](InternetRuleTypeAllowUrlCategoryInner.md) |  | [optional] 
**allow_web_application** | [**List[InternetRuleTypeAllowWebApplicationInner]**](InternetRuleTypeAllowWebApplicationInner.md) |  | [optional] 
**application** | **List[str]** | The application(s) being accessed | [optional] 
**block_url_category** | **List[str]** |  | [optional] 
**block_web_application** | **List[str]** |  | [optional] 
**category** | **List[str]** | The URL categories being accessed | [optional] 
**default_profile_settings** | [**InternetRuleTypeDefaultProfileSettings**](InternetRuleTypeDefaultProfileSettings.md) |  | [optional] 
**description** | **str** | The description of the security rule | [optional] 
**destination** | **List[str]** | The destination address(es) | [optional] 
**destination_hip** | **List[str]** | The destination Host Integrity Profile(s) | [optional] 
**device** | **str** | The device in which the resource is defined | [optional] 
**devices** | **List[str]** |  | [optional] [default to ["any"]]
**disabled** | **bool** | Is the security rule disabled? | [optional] [default to False]
**folder** | **str** | The folder in which the resource is defined | [optional] 
**var_from** | **List[str]** | The source security zone(s) | [optional] 
**id** | **str** | The UUID of the security rule | [optional] [readonly] 
**log_end** | **bool** | Log at session end? | [optional] 
**log_setting** | **str** | The external log forwarding profile | [optional] 
**log_settings** | [**InternetRuleTypeLogSettings**](InternetRuleTypeLogSettings.md) |  | [optional] 
**log_start** | **bool** | Log at session start? | [optional] 
**name** | **str** | The name of the security rule | [optional] 
**negate_destination** | **bool** | Negate the destination addresses(es)? | [optional] [default to False]
**negate_source** | **bool** | Negate the source address(es)? | [optional] [default to False]
**negate_user** | **bool** |  | [optional] 
**policy_type** | **str** |  | [optional] [default to 'Security']
**profile_setting** | [**SecurityRuleTypeProfileSetting**](SecurityRuleTypeProfileSetting.md) |  | [optional] 
**schedule** | **str** | Schedule in which this rule will be applied | [optional] 
**security_settings** | [**InternetRuleTypeSecuritySettings**](InternetRuleTypeSecuritySettings.md) |  | [optional] 
**service** | **List[str]** | The service(s) being accessed | [optional] 
**snippet** | **str** | The snippet in which the resource is defined | [optional] 
**source** | **List[str]** | The source addresses(es) | [optional] 
**source_hip** | **List[str]** | The source Host Integrity Profile(s) | [optional] 
**source_user** | **List[str]** | List of source users and/or groups.  Reserved words include &#x60;any&#x60;, &#x60;pre-login&#x60;, &#x60;known-user&#x60;, and &#x60;unknown&#x60;. | [optional] 
**tag** | **List[str]** | The tags associated with the security rule | [optional] 
**tenant_restrictions** | **List[str]** |  | [optional] 
**to** | **List[str]** | The destination security zone(s) | [optional] 

## Example

```python
from scm.security_services.models.security_rules import SecurityRules

# TODO update the JSON string below
json = "{}"
# create an instance of SecurityRules from a JSON string
security_rules_instance = SecurityRules.from_json(json)
# print the JSON string representation of the object
print(SecurityRules.to_json())

# convert the object into a dict
security_rules_dict = security_rules_instance.to_dict()
# create an instance of SecurityRules from a dict
security_rules_from_dict = SecurityRules.from_dict(security_rules_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


