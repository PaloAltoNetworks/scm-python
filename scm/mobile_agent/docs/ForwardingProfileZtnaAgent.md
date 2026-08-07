# ForwardingProfileZtnaAgent

ZTNA agent-based forwarding profile configuration

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ztna_agent** | [**ForwardingProfileZtnaAgentZtnaAgent**](ForwardingProfileZtnaAgentZtnaAgent.md) |  | [optional] 

## Example

```python
from scm.mobile_agent.models.forwarding_profile_ztna_agent import ForwardingProfileZtnaAgent

# TODO update the JSON string below
json = "{}"
# create an instance of ForwardingProfileZtnaAgent from a JSON string
forwarding_profile_ztna_agent_instance = ForwardingProfileZtnaAgent.from_json(json)
# print the JSON string representation of the object
print(ForwardingProfileZtnaAgent.to_json())

# convert the object into a dict
forwarding_profile_ztna_agent_dict = forwarding_profile_ztna_agent_instance.to_dict()
# create an instance of ForwardingProfileZtnaAgent from a dict
forwarding_profile_ztna_agent_from_dict = ForwardingProfileZtnaAgent.from_dict(forwarding_profile_ztna_agent_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


