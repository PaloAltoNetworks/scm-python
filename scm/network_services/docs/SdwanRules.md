# SdwanRules


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | [**SdwanRulesAction**](SdwanRulesAction.md) |  | 
**application** | **List[str]** | List of applications | 
**description** | **str** | Rule description | [optional] 
**destination** | **List[str]** | List of destination addresses | 
**device** | **str** | The device in which the resource is defined | [optional] 
**disabled** | **bool** | Disable rule? | [optional] [default to False]
**error_correction_profile** | **str** | Error correction profile | [optional] 
**folder** | **str** | The folder in which the resource is defined | [optional] 
**var_from** | **List[str]** | List of source zones | 
**id** | **str** | UUID of the resource | [optional] [readonly] 
**name** | **str** | Rule name | 
**negate_destination** | **bool** | Negate destination address(es)? | [optional] [default to False]
**negate_source** | **bool** | Negate source address(es)? | [optional] [default to False]
**path_quality_profile** | **str** | Path quality profile | 
**position** | **str** | Rule postion relative to device rules | 
**saas_quality_profile** | **str** | SaaS quality profile | [optional] 
**service** | **List[str]** | List of services | 
**snippet** | **str** | The snippet in which the resource is defined | [optional] 
**source** | **List[str]** | List of source addresses | 
**source_user** | **List[str]** | List of source users | 
**tag** | **List[str]** | List of tags | [optional] 
**to** | **List[str]** | List of destination zones | 

## Example

```python
from scm_network_services.models.sdwan_rules import SdwanRules

# TODO update the JSON string below
json = "{}"
# create an instance of SdwanRules from a JSON string
sdwan_rules_instance = SdwanRules.from_json(json)
# print the JSON string representation of the object
print(SdwanRules.to_json())

# convert the object into a dict
sdwan_rules_dict = sdwan_rules_instance.to_dict()
# create an instance of SdwanRules from a dict
sdwan_rules_from_dict = SdwanRules.from_dict(sdwan_rules_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


