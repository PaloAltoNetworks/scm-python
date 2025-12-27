# NatRules


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**active_active_device_binding** | **str** |  | [optional] 
**description** | **str** | NAT rule description | [optional] 
**destination** | **List[str]** | Destination address(es) of the original packet | 
**destination_translation** | [**NatRulesDestinationTranslation**](NatRulesDestinationTranslation.md) |  | [optional] 
**device** | **str** | The device in which the resource is defined | [optional] 
**disabled** | **bool** | Disable NAT rule? | [optional] [default to False]
**dynamic_destination_translation** | [**NatRulesDynamicDestinationTranslation**](NatRulesDynamicDestinationTranslation.md) |  | [optional] 
**folder** | **str** | The folder in which the resource is defined | [optional] 
**var_from** | **List[str]** | Source zone(s) of the original packet | 
**id** | **str** | UUID of the resource | [readonly] 
**name** | **str** | NAT rule name | 
**nat_type** | **str** | NAT type | [optional] [default to 'ipv4']
**service** | **str** | The service of the original packet | 
**snippet** | **str** | The snippet in which the resource is defined | [optional] 
**source** | **List[str]** | Source address(es) of the original packet | 
**source_translation** | [**NatRulesSourceTranslation**](NatRulesSourceTranslation.md) |  | [optional] 
**tag** | **List[str]** | NAT rule tags | [optional] 
**to** | **List[str]** | Destination zone of the original packet | 
**to_interface** | **str** | Destination interface of the original packet | [optional] 

## Example

```python
from scm_network_services.models.nat_rules import NatRules

# TODO update the JSON string below
json = "{}"
# create an instance of NatRules from a JSON string
nat_rules_instance = NatRules.from_json(json)
# print the JSON string representation of the object
print(NatRules.to_json())

# convert the object into a dict
nat_rules_dict = nat_rules_instance.to_dict()
# create an instance of NatRules from a dict
nat_rules_from_dict = NatRules.from_dict(nat_rules_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


