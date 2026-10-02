# BlockRuleBasicAllowUdp

UDP traffic allowlist configuration with location and destination support

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**destinations** | **str** | Destination addresses or networks allowed for UDP traffic | [optional] 
**enable_destinations** | **bool** | Enable destinations for allow-udp | [optional] 
**enable_locations** | **bool** | Enable locations for allow-udp | [optional] 
**locations** | **List[str]** | List of user locations allowed for UDP traffic | [optional] 

## Example

```python
from scm.mobile_agent.models.block_rule_basic_allow_udp import BlockRuleBasicAllowUdp

# TODO update the JSON string below
json = "{}"
# create an instance of BlockRuleBasicAllowUdp from a JSON string
block_rule_basic_allow_udp_instance = BlockRuleBasicAllowUdp.from_json(json)
# print the JSON string representation of the object
print(BlockRuleBasicAllowUdp.to_json())

# convert the object into a dict
block_rule_basic_allow_udp_dict = block_rule_basic_allow_udp_instance.to_dict()
# create an instance of BlockRuleBasicAllowUdp from a dict
block_rule_basic_allow_udp_from_dict = BlockRuleBasicAllowUdp.from_dict(block_rule_basic_allow_udp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


