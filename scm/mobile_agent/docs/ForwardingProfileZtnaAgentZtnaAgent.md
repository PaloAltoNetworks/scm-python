# ForwardingProfileZtnaAgentZtnaAgent

ZTNA agent-based forwarding configuration

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**block_rule** | [**BlockRuleZtna**](BlockRuleZtna.md) |  | [optional] 
**forwarding_rules** | [**List[ForwardingRuleZtna]**](ForwardingRuleZtna.md) | List of ZTNA agent-based forwarding rules | [optional] 
**pac_upload** | **bool** | User uploaded PAC file for a ZTNA agent-based forwarding configuration | [optional] [default to False]

## Example

```python
from scm.mobile_agent.models.forwarding_profile_ztna_agent_ztna_agent import ForwardingProfileZtnaAgentZtnaAgent

# TODO update the JSON string below
json = "{}"
# create an instance of ForwardingProfileZtnaAgentZtnaAgent from a JSON string
forwarding_profile_ztna_agent_ztna_agent_instance = ForwardingProfileZtnaAgentZtnaAgent.from_json(json)
# print the JSON string representation of the object
print(ForwardingProfileZtnaAgentZtnaAgent.to_json())

# convert the object into a dict
forwarding_profile_ztna_agent_ztna_agent_dict = forwarding_profile_ztna_agent_ztna_agent_instance.to_dict()
# create an instance of ForwardingProfileZtnaAgentZtnaAgent from a dict
forwarding_profile_ztna_agent_ztna_agent_from_dict = ForwardingProfileZtnaAgentZtnaAgent.from_dict(forwarding_profile_ztna_agent_ztna_agent_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


