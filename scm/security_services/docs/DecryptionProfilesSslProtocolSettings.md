# DecryptionProfilesSslProtocolSettings


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**auth_algo_md5** | **bool** |  | [optional] [default to True]
**auth_algo_sha1** | **bool** |  | [optional] [default to True]
**auth_algo_sha256** | **bool** |  | [optional] [default to True]
**auth_algo_sha384** | **bool** |  | [optional] [default to True]
**enc_algo_3des** | **bool** |  | [optional] [default to True]
**enc_algo_aes_128_cbc** | **bool** |  | [optional] [default to True]
**enc_algo_aes_128_gcm** | **bool** |  | [optional] [default to True]
**enc_algo_aes_256_cbc** | **bool** |  | [optional] [default to True]
**enc_algo_aes_256_gcm** | **bool** |  | [optional] [default to True]
**enc_algo_chacha20_poly1305** | **bool** |  | [optional] [default to True]
**enc_algo_rc4** | **bool** |  | [optional] [default to True]
**keyxchg_algo_dhe** | **bool** |  | [optional] [default to True]
**keyxchg_algo_ecdhe** | **bool** |  | [optional] [default to True]
**keyxchg_algo_rsa** | **bool** |  | [optional] [default to True]
**max_version** | **str** |  | [optional] [default to 'tls1-2']
**min_version** | **str** |  | [optional] [default to 'tls1-0']

## Example

```python
from scm_security_services.models.decryption_profiles_ssl_protocol_settings import DecryptionProfilesSslProtocolSettings

# TODO update the JSON string below
json = "{}"
# create an instance of DecryptionProfilesSslProtocolSettings from a JSON string
decryption_profiles_ssl_protocol_settings_instance = DecryptionProfilesSslProtocolSettings.from_json(json)
# print the JSON string representation of the object
print(DecryptionProfilesSslProtocolSettings.to_json())

# convert the object into a dict
decryption_profiles_ssl_protocol_settings_dict = decryption_profiles_ssl_protocol_settings_instance.to_dict()
# create an instance of DecryptionProfilesSslProtocolSettings from a dict
decryption_profiles_ssl_protocol_settings_from_dict = DecryptionProfilesSslProtocolSettings.from_dict(decryption_profiles_ssl_protocol_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


