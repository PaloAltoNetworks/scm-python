# SecurityRuleType

A standard security rule for controlling traffic between zones.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **str** | The action to be taken when the rule is matched | 
**application** | **List[str]** | The application(s) being accessed | 
**category** | **List[str]** | The URL categories being accessed | 
**description** | **str** | The description of the security rule | [optional] 
**destination** | **List[str]** | The destination address(es) | 
**destination_hip** | **List[str]** | The destination Host Integrity Profile(s) | [optional] 
**disabled** | **bool** | Is the security rule disabled? | [optional] [default to False]
**var_from** | **List[str]** | The source security zone(s) | 
**id** | **str** | The UUID of the security rule | [optional] [readonly] 
**log_end** | **bool** | Log at session end? | [optional] 
**log_setting** | **str** | The external log forwarding profile | [optional] 
**log_start** | **bool** | Log at session start? | [optional] 
**name** | **str** | The name of the security rule | 
**negate_destination** | **bool** | Negate the destination addresses(es)? | [optional] [default to False]
**negate_source** | **bool** | Negate the source address(es)? | [optional] [default to False]
**policy_type** | **str** |  | [optional] [default to 'Security']
**profile_setting** | [**SecurityRuleTypeProfileSetting**](SecurityRuleTypeProfileSetting.md) |  | [optional] 
**schedule** | **str** | Schedule in which this rule will be applied | [optional] 
**service** | **List[str]** | The service(s) being accessed | 
**source** | **List[str]** | The source addresses(es) | 
**source_hip** | **List[str]** | The source Host Integrity Profile(s) | [optional] 
**source_user** | **List[str]** | List of source users and/or groups.  Reserved words include &#x60;any&#x60;, &#x60;pre-login&#x60;, &#x60;known-user&#x60;, and &#x60;unknown&#x60;. | 
**tag** | **List[str]** | The tags associated with the security rule | [optional] 
**tenant_restrictions** | **List[str]** |  | [optional] 
**to** | **List[str]** | The destination security zone(s) | 

## Example

```python
from scm_security_services.models.security_rule_type import SecurityRuleType

# TODO update the JSON string below
json = "{}"
# create an instance of SecurityRuleType from a JSON string
security_rule_type_instance = SecurityRuleType.from_json(json)
# print the JSON string representation of the object
print(SecurityRuleType.to_json())

# convert the object into a dict
security_rule_type_dict = security_rule_type_instance.to_dict()
# create an instance of SecurityRuleType from a dict
security_rule_type_from_dict = SecurityRuleType.from_dict(security_rule_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


