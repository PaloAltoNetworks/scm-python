# ForwardingProfilePacFilePacFile

PAC file based forwarding configuration

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**block_rule** | [**BlockRuleBasic**](BlockRuleBasic.md) |  | [optional] 
**forwarding_rules** | [**List[ForwardingRuleBasic]**](ForwardingRuleBasic.md) | List of PAC file-based forwarding rules | [optional] 
**pac_upload** | **bool** | User upload PAC file for PAC file based forwarding configuration | [optional] [default to False]

## Example

```python
from scm.mobile_agent.models.forwarding_profile_pac_file_pac_file import ForwardingProfilePacFilePacFile

# TODO update the JSON string below
json = "{}"
# create an instance of ForwardingProfilePacFilePacFile from a JSON string
forwarding_profile_pac_file_pac_file_instance = ForwardingProfilePacFilePacFile.from_json(json)
# print the JSON string representation of the object
print(ForwardingProfilePacFilePacFile.to_json())

# convert the object into a dict
forwarding_profile_pac_file_pac_file_dict = forwarding_profile_pac_file_pac_file_instance.to_dict()
# create an instance of ForwardingProfilePacFilePacFile from a dict
forwarding_profile_pac_file_pac_file_from_dict = ForwardingProfilePacFilePacFile.from_dict(forwarding_profile_pac_file_pac_file_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


