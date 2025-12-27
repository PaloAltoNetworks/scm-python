# SslDecryptionSettingsSslExcludeCertInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** |  | [optional] 
**exclude** | **bool** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from scm_network_services.models.ssl_decryption_settings_ssl_exclude_cert_inner import SslDecryptionSettingsSslExcludeCertInner

# TODO update the JSON string below
json = "{}"
# create an instance of SslDecryptionSettingsSslExcludeCertInner from a JSON string
ssl_decryption_settings_ssl_exclude_cert_inner_instance = SslDecryptionSettingsSslExcludeCertInner.from_json(json)
# print the JSON string representation of the object
print(SslDecryptionSettingsSslExcludeCertInner.to_json())

# convert the object into a dict
ssl_decryption_settings_ssl_exclude_cert_inner_dict = ssl_decryption_settings_ssl_exclude_cert_inner_instance.to_dict()
# create an instance of SslDecryptionSettingsSslExcludeCertInner from a dict
ssl_decryption_settings_ssl_exclude_cert_inner_from_dict = SslDecryptionSettingsSslExcludeCertInner.from_dict(ssl_decryption_settings_ssl_exclude_cert_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


