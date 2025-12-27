# SslDecryptionSettingsForwardTrustCertificate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ecdsa** | **str** |  | [optional] 
**rsa** | **str** |  | [optional] 

## Example

```python
from scm_network_services.models.ssl_decryption_settings_forward_trust_certificate import SslDecryptionSettingsForwardTrustCertificate

# TODO update the JSON string below
json = "{}"
# create an instance of SslDecryptionSettingsForwardTrustCertificate from a JSON string
ssl_decryption_settings_forward_trust_certificate_instance = SslDecryptionSettingsForwardTrustCertificate.from_json(json)
# print the JSON string representation of the object
print(SslDecryptionSettingsForwardTrustCertificate.to_json())

# convert the object into a dict
ssl_decryption_settings_forward_trust_certificate_dict = ssl_decryption_settings_forward_trust_certificate_instance.to_dict()
# create an instance of SslDecryptionSettingsForwardTrustCertificate from a dict
ssl_decryption_settings_forward_trust_certificate_from_dict = SslDecryptionSettingsForwardTrustCertificate.from_dict(ssl_decryption_settings_forward_trust_certificate_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


