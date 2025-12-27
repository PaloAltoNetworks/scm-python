# DecryptionRules


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **str** | The action to be taken | 
**category** | **List[str]** | The destination URL category | 
**description** | **str** | The description of the decryption rule | [optional] 
**destination** | **List[str]** | The destination addresses | 
**destination_hip** | **List[str]** | The Host Integrity Profile of the destination host | [optional] 
**device** | **str** | The device in which the resource is defined | [optional] 
**disabled** | **bool** | Is the rule disabled? | [optional] 
**folder** | **str** | The folder in which the resource is defined | [optional] 
**var_from** | **List[str]** | The source security zone | 
**id** | **str** | The UUID of the decryption rule | [optional] [readonly] 
**log_fail** | **bool** | Log failed decryption events? | [optional] 
**log_setting** | **str** | The log settings of the decryption rule | [optional] 
**log_success** | **bool** | Log successful decryption events? | [optional] 
**name** | **str** | The name of the decryption rule | 
**negate_destination** | **bool** | Negate the destination addresses? | [optional] 
**negate_source** | **bool** | Negate the source addresses? | [optional] 
**profile** | **str** | The decryption profile associated with the decryption rule | [optional] 
**service** | **List[str]** | The destination services and/or service groups | 
**snippet** | **str** | The snippet in which the resource is defined | [optional] 
**source** | **List[str]** | The source addresses | 
**source_hip** | **List[str]** |  | [optional] 
**source_user** | **List[str]** | List of source users and/or groups.  Reserved words include &#x60;any&#x60;, &#x60;pre-login&#x60;, &#x60;known-user&#x60;, and &#x60;unknown&#x60;. | 
**tag** | **List[str]** | The tags associated with the decryption rule | [optional] 
**to** | **List[str]** | The destination security zone | 
**type** | [**DecryptionRulesType**](DecryptionRulesType.md) |  | [optional] 

## Example

```python
from scm_security_services.models.decryption_rules import DecryptionRules

# TODO update the JSON string below
json = "{}"
# create an instance of DecryptionRules from a JSON string
decryption_rules_instance = DecryptionRules.from_json(json)
# print the JSON string representation of the object
print(DecryptionRules.to_json())

# convert the object into a dict
decryption_rules_dict = decryption_rules_instance.to_dict()
# create an instance of DecryptionRules from a dict
decryption_rules_from_dict = DecryptionRules.from_dict(decryption_rules_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


