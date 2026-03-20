# DecryptionProfilesSslInboundProxy


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**block_if_hsm_unavailable** | **bool** |  | [optional] [default to False]
**block_if_no_resource** | **bool** |  | [optional] [default to False]
**block_unsupported_cipher** | **bool** |  | [optional] [default to False]
**block_unsupported_version** | **bool** |  | [optional] [default to False]

## Example

```python
from scm.security_services.models.decryption_profiles_ssl_inbound_proxy import DecryptionProfilesSslInboundProxy

# TODO update the JSON string below
json = "{}"
# create an instance of DecryptionProfilesSslInboundProxy from a JSON string
decryption_profiles_ssl_inbound_proxy_instance = DecryptionProfilesSslInboundProxy.from_json(json)
# print the JSON string representation of the object
print(DecryptionProfilesSslInboundProxy.to_json())

# convert the object into a dict
decryption_profiles_ssl_inbound_proxy_dict = decryption_profiles_ssl_inbound_proxy_instance.to_dict()
# create an instance of DecryptionProfilesSslInboundProxy from a dict
decryption_profiles_ssl_inbound_proxy_from_dict = DecryptionProfilesSslInboundProxy.from_dict(decryption_profiles_ssl_inbound_proxy_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


