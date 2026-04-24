# BlockRuleBasicAllowTcp

TCP traffic allowlist configuration

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enable_locations** | **bool** | Enable locations for allow-tcp | [optional] 
**locations** | **List[str]** | List of user locations allowed for TCP traffic | [optional] 

## Example

```python
from scm.mobile_agent.models.block_rule_basic_allow_tcp import BlockRuleBasicAllowTcp

# TODO update the JSON string below
json = "{}"
# create an instance of BlockRuleBasicAllowTcp from a JSON string
block_rule_basic_allow_tcp_instance = BlockRuleBasicAllowTcp.from_json(json)
# print the JSON string representation of the object
print(BlockRuleBasicAllowTcp.to_json())

# convert the object into a dict
block_rule_basic_allow_tcp_dict = block_rule_basic_allow_tcp_instance.to_dict()
# create an instance of BlockRuleBasicAllowTcp from a dict
block_rule_basic_allow_tcp_from_dict = BlockRuleBasicAllowTcp.from_dict(block_rule_basic_allow_tcp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


