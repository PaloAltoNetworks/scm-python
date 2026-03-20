# SslDecryptionSettings


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**device** | **str** | The device in which the resource is defined | [optional] 
**disabled_ssl_exclude_cert_from_predefined** | **List[object]** |  | [optional] 
**folder** | **str** | The folder in which the resource is defined | [optional] 
**forward_trust_certificate** | [**SslDecryptionSettingsForwardTrustCertificate**](SslDecryptionSettingsForwardTrustCertificate.md) |  | [optional] 
**forward_untrust_certificate** | [**SslDecryptionSettingsForwardTrustCertificate**](SslDecryptionSettingsForwardTrustCertificate.md) |  | [optional] 
**root_ca_exclude_list** | **List[object]** |  | [optional] 
**snippet** | **str** | The snippet in which the resource is defined | [optional] 
**ssl_exclude_cert** | [**List[SslDecryptionSettingsSslExcludeCertInner]**](SslDecryptionSettingsSslExcludeCertInner.md) |  | [optional] 
**trusted_root_ca** | **List[object]** |  | [optional] 

## Example

```python
from scm.security_services.models.ssl_decryption_settings import SslDecryptionSettings

# TODO update the JSON string below
json = "{}"
# create an instance of SslDecryptionSettings from a JSON string
ssl_decryption_settings_instance = SslDecryptionSettings.from_json(json)
# print the JSON string representation of the object
print(SslDecryptionSettings.to_json())

# convert the object into a dict
ssl_decryption_settings_dict = ssl_decryption_settings_instance.to_dict()
# create an instance of SslDecryptionSettings from a dict
ssl_decryption_settings_from_dict = SslDecryptionSettings.from_dict(ssl_decryption_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


