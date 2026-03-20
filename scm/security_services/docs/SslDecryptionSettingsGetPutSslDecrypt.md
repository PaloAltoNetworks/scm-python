# SslDecryptionSettingsGetPutSslDecrypt


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**disabled_ssl_exclude_cert_from_predefined** | **List[object]** |  | [optional] 
**forward_trust_certificate** | [**SslDecryptionSettingsForwardTrustCertificate**](SslDecryptionSettingsForwardTrustCertificate.md) |  | [optional] 
**forward_untrust_certificate** | [**SslDecryptionSettingsForwardTrustCertificate**](SslDecryptionSettingsForwardTrustCertificate.md) |  | [optional] 
**root_ca_exclude_list** | **List[object]** |  | [optional] 
**ssl_exclude_cert** | [**List[SslDecryptionSettingsSslExcludeCertInner]**](SslDecryptionSettingsSslExcludeCertInner.md) |  | [optional] 
**trusted_root_ca** | **List[object]** |  | [optional] 

## Example

```python
from scm.security_services.models.ssl_decryption_settings_get_put_ssl_decrypt import SslDecryptionSettingsGetPutSslDecrypt

# TODO update the JSON string below
json = "{}"
# create an instance of SslDecryptionSettingsGetPutSslDecrypt from a JSON string
ssl_decryption_settings_get_put_ssl_decrypt_instance = SslDecryptionSettingsGetPutSslDecrypt.from_json(json)
# print the JSON string representation of the object
print(SslDecryptionSettingsGetPutSslDecrypt.to_json())

# convert the object into a dict
ssl_decryption_settings_get_put_ssl_decrypt_dict = ssl_decryption_settings_get_put_ssl_decrypt_instance.to_dict()
# create an instance of SslDecryptionSettingsGetPutSslDecrypt from a dict
ssl_decryption_settings_get_put_ssl_decrypt_from_dict = SslDecryptionSettingsGetPutSslDecrypt.from_dict(ssl_decryption_settings_get_put_ssl_decrypt_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


