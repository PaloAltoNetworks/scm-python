# BlockRuleBasic

Basic block rule configuration for PAC file and GlobalProtect proxy profiles

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allow_tcp** | [**BlockRuleBasicAllowTcp**](BlockRuleBasicAllowTcp.md) |  | [optional] 
**allow_udp** | [**BlockRuleBasicAllowUdp**](BlockRuleBasicAllowUdp.md) |  | [optional] 
**enable** | **bool** | Enable block rule | [optional] 

## Example

```python
from scm.mobile_agent.models.block_rule_basic import BlockRuleBasic

# TODO update the JSON string below
json = "{}"
# create an instance of BlockRuleBasic from a JSON string
block_rule_basic_instance = BlockRuleBasic.from_json(json)
# print the JSON string representation of the object
print(BlockRuleBasic.to_json())

# convert the object into a dict
block_rule_basic_dict = block_rule_basic_instance.to_dict()
# create an instance of BlockRuleBasic from a dict
block_rule_basic_from_dict = BlockRuleBasic.from_dict(block_rule_basic_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


