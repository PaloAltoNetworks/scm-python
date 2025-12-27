# DecryptionProfiles


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**device** | **str** | The device in which the resource is defined | [optional] 
**folder** | **str** | The folder in which the resource is defined | [optional] 
**id** | **str** | UUID of the resource | [optional] [readonly] 
**name** | **str** | Must start with alphanumeric char and should contain only alphanemeric, underscore, hyphen, dot or space | 
**snippet** | **str** | The snippet in which the resource is defined | [optional] 
**ssl_forward_proxy** | [**DecryptionProfilesSslForwardProxy**](DecryptionProfilesSslForwardProxy.md) |  | [optional] 
**ssl_inbound_proxy** | [**DecryptionProfilesSslInboundProxy**](DecryptionProfilesSslInboundProxy.md) |  | [optional] 
**ssl_no_proxy** | [**DecryptionProfilesSslNoProxy**](DecryptionProfilesSslNoProxy.md) |  | [optional] 
**ssl_protocol_settings** | [**DecryptionProfilesSslProtocolSettings**](DecryptionProfilesSslProtocolSettings.md) |  | [optional] 

## Example

```python
from scm_security_services.models.decryption_profiles import DecryptionProfiles

# TODO update the JSON string below
json = "{}"
# create an instance of DecryptionProfiles from a JSON string
decryption_profiles_instance = DecryptionProfiles.from_json(json)
# print the JSON string representation of the object
print(DecryptionProfiles.to_json())

# convert the object into a dict
decryption_profiles_dict = decryption_profiles_instance.to_dict()
# create an instance of DecryptionProfiles from a dict
decryption_profiles_from_dict = DecryptionProfiles.from_dict(decryption_profiles_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


