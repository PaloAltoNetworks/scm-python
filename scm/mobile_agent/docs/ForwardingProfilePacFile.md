# ForwardingProfilePacFile

PAC file-based forwarding profile configuration

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pac_file** | [**ForwardingProfilePacFilePacFile**](ForwardingProfilePacFilePacFile.md) |  | [optional] 

## Example

```python
from scm.mobile_agent.models.forwarding_profile_pac_file import ForwardingProfilePacFile

# TODO update the JSON string below
json = "{}"
# create an instance of ForwardingProfilePacFile from a JSON string
forwarding_profile_pac_file_instance = ForwardingProfilePacFile.from_json(json)
# print the JSON string representation of the object
print(ForwardingProfilePacFile.to_json())

# convert the object into a dict
forwarding_profile_pac_file_dict = forwarding_profile_pac_file_instance.to_dict()
# create an instance of ForwardingProfilePacFile from a dict
forwarding_profile_pac_file_from_dict = ForwardingProfilePacFile.from_dict(forwarding_profile_pac_file_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


