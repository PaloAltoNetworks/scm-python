# BaseRuleProperties


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **str** | The action to be taken when the rule is matched | [optional] 
**description** | **str** | The description of the security rule | [optional] 
**destination** | **List[str]** | The destination address(es) | [optional] 
**disabled** | **bool** | Is the security rule disabled? | [optional] [default to False]
**var_from** | **List[str]** | The source security zone(s) | [optional] 
**id** | **str** | The UUID of the security rule | [optional] [readonly] 
**name** | **str** | The name of the security rule | 
**negate_source** | **bool** | Negate the source address(es)? | [optional] [default to False]
**policy_type** | **str** |  | [optional] [default to 'Security']
**schedule** | **str** | Schedule in which this rule will be applied | [optional] 
**service** | **List[str]** | The service(s) being accessed | [optional] 
**source** | **List[str]** | The source addresses(es) | [optional] 
**source_user** | **List[str]** | List of source users and/or groups.  Reserved words include &#x60;any&#x60;, &#x60;pre-login&#x60;, &#x60;known-user&#x60;, and &#x60;unknown&#x60;. | [optional] 
**tag** | **List[str]** | The tags associated with the security rule | [optional] 
**to** | **List[str]** | The destination security zone(s) | [optional] 

## Example

```python
from scm.security_services.models.base_rule_properties import BaseRuleProperties

# TODO update the JSON string below
json = "{}"
# create an instance of BaseRuleProperties from a JSON string
base_rule_properties_instance = BaseRuleProperties.from_json(json)
# print the JSON string representation of the object
print(BaseRuleProperties.to_json())

# convert the object into a dict
base_rule_properties_dict = base_rule_properties_instance.to_dict()
# create an instance of BaseRuleProperties from a dict
base_rule_properties_from_dict = BaseRuleProperties.from_dict(base_rule_properties_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


