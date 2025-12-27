# AntiSpywareSignaturesDefaultAction

anti spyware signature default action

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**alert** | **object** |  | [optional] 
**allow** | **object** |  | [optional] 
**block_ip** | [**AntiSpywareSignaturesDefaultActionBlockIp**](AntiSpywareSignaturesDefaultActionBlockIp.md) |  | [optional] 
**drop** | **object** |  | [optional] 
**reset_both** | **object** |  | [optional] 
**reset_client** | **object** |  | [optional] 
**reset_server** | **object** |  | [optional] 

## Example

```python
from scm_security_services.models.anti_spyware_signatures_default_action import AntiSpywareSignaturesDefaultAction

# TODO update the JSON string below
json = "{}"
# create an instance of AntiSpywareSignaturesDefaultAction from a JSON string
anti_spyware_signatures_default_action_instance = AntiSpywareSignaturesDefaultAction.from_json(json)
# print the JSON string representation of the object
print(AntiSpywareSignaturesDefaultAction.to_json())

# convert the object into a dict
anti_spyware_signatures_default_action_dict = anti_spyware_signatures_default_action_instance.to_dict()
# create an instance of AntiSpywareSignaturesDefaultAction from a dict
anti_spyware_signatures_default_action_from_dict = AntiSpywareSignaturesDefaultAction.from_dict(anti_spyware_signatures_default_action_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


