# DosProtectionRules


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | [**DosProtectionRulesAction**](DosProtectionRulesAction.md) |  | [optional] 
**description** | **str** | Description | [optional] 
**destination** | **List[str]** | List of destination addresses | [optional] 
**device** | **str** | The device in which the resource is defined | [optional] 
**disabled** | **bool** | Rule disabled? | [optional] [default to False]
**folder** | **str** | The folder in which the resource is defined | [optional] 
**var_from** | **List[str]** | List of source zones | [optional] 
**id** | **str** | The UUID of the DNS security profile | [optional] [readonly] 
**log_setting** | **str** | Log forwarding profile name | [optional] [default to 'Cortex Data Lake']
**name** | **str** | Rule name | 
**position** | **str** | Position relative to local device rules | [optional] [default to 'pre']
**protection** | [**DosProtectionRulesProtection**](DosProtectionRulesProtection.md) |  | [optional] 
**schedule** | **str** | Schedule on which to enforce the rule | [optional] 
**service** | **List[str]** | List of services | [optional] 
**snippet** | **str** | The snippet in which the resource is defined | [optional] 
**source** | **List[str]** | List of source addresses | [optional] 
**source_user** | **List[str]** | List of source users and/or groups.  Reserved words include &#x60;any&#x60;, &#x60;pre-login&#x60;, &#x60;known-user&#x60;, and &#x60;unknown&#x60;. | [optional] 
**tag** | **List[str]** | List of tags | [optional] 
**to** | **List[str]** | List of destination zones | [optional] 

## Example

```python
from scm_security_services.models.dos_protection_rules import DosProtectionRules

# TODO update the JSON string below
json = "{}"
# create an instance of DosProtectionRules from a JSON string
dos_protection_rules_instance = DosProtectionRules.from_json(json)
# print the JSON string representation of the object
print(DosProtectionRules.to_json())

# convert the object into a dict
dos_protection_rules_dict = dos_protection_rules_instance.to_dict()
# create an instance of DosProtectionRules from a dict
dos_protection_rules_from_dict = DosProtectionRules.from_dict(dos_protection_rules_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


