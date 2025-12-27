# DecryptionProfilesSslForwardProxy


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**auto_include_altname** | **bool** |  | [optional] [default to False]
**block_client_cert** | **bool** |  | [optional] [default to False]
**block_expired_certificate** | **bool** |  | [optional] [default to False]
**block_timeout_cert** | **bool** |  | [optional] [default to False]
**block_tls13_downgrade_no_resource** | **bool** |  | [optional] [default to False]
**block_unknown_cert** | **bool** |  | [optional] [default to False]
**block_unsupported_cipher** | **bool** |  | [optional] [default to False]
**block_unsupported_version** | **bool** |  | [optional] [default to False]
**block_untrusted_issuer** | **bool** |  | [optional] [default to False]
**restrict_cert_exts** | **bool** |  | [optional] [default to False]
**strip_alpn** | **bool** |  | [optional] [default to False]

## Example

```python
from scm_security_services.models.decryption_profiles_ssl_forward_proxy import DecryptionProfilesSslForwardProxy

# TODO update the JSON string below
json = "{}"
# create an instance of DecryptionProfilesSslForwardProxy from a JSON string
decryption_profiles_ssl_forward_proxy_instance = DecryptionProfilesSslForwardProxy.from_json(json)
# print the JSON string representation of the object
print(DecryptionProfilesSslForwardProxy.to_json())

# convert the object into a dict
decryption_profiles_ssl_forward_proxy_dict = decryption_profiles_ssl_forward_proxy_instance.to_dict()
# create an instance of DecryptionProfilesSslForwardProxy from a dict
decryption_profiles_ssl_forward_proxy_from_dict = DecryptionProfilesSslForwardProxy.from_dict(decryption_profiles_ssl_forward_proxy_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


