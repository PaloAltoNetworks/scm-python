# AntiSpywareSignatures


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bugtraq** | **List[str]** |  | [optional] 
**comment** | **str** |  | [optional] 
**cve** | **List[str]** |  | [optional] 
**default_action** | [**AntiSpywareSignaturesDefaultAction**](AntiSpywareSignaturesDefaultAction.md) |  | [optional] 
**device** | **str** | The device in which the resource is defined | [optional] 
**direction** | **str** |  | [optional] 
**folder** | **str** | The folder in which the resource is defined | [optional] 
**id** | **str** | UUID of the resource | [readonly] 
**reference** | **List[str]** |  | [optional] 
**severity** | **str** |  | [optional] 
**signature** | [**AntiSpywareSignaturesSignature**](AntiSpywareSignaturesSignature.md) |  | [optional] 
**snippet** | **str** | The snippet in which the resource is defined | [optional] 
**threat_id** | **str** | threat id range &lt;15000-18000&gt; and &lt;6900001-7000000&gt; | 
**threatname** | **str** |  | 
**vendor** | **List[str]** |  | [optional] 

## Example

```python
from scm_security_services.models.anti_spyware_signatures import AntiSpywareSignatures

# TODO update the JSON string below
json = "{}"
# create an instance of AntiSpywareSignatures from a JSON string
anti_spyware_signatures_instance = AntiSpywareSignatures.from_json(json)
# print the JSON string representation of the object
print(AntiSpywareSignatures.to_json())

# convert the object into a dict
anti_spyware_signatures_dict = anti_spyware_signatures_instance.to_dict()
# create an instance of AntiSpywareSignatures from a dict
anti_spyware_signatures_from_dict = AntiSpywareSignatures.from_dict(anti_spyware_signatures_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


