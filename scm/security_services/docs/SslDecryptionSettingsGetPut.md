# SslDecryptionSettingsGetPut


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**device** | **str** | The device in which the resource is defined | [optional] 
**folder** | **str** | The folder in which the resource is defined | [optional] 
**snippet** | **str** | The snippet in which the resource is defined | [optional] 
**ssl_decrypt** | [**SslDecryptionSettingsGetPutSslDecrypt**](SslDecryptionSettingsGetPutSslDecrypt.md) |  | 

## Example

```python
from scm.security_services.models.ssl_decryption_settings_get_put import SslDecryptionSettingsGetPut

# TODO update the JSON string below
json = "{}"
# create an instance of SslDecryptionSettingsGetPut from a JSON string
ssl_decryption_settings_get_put_instance = SslDecryptionSettingsGetPut.from_json(json)
# print the JSON string representation of the object
print(SslDecryptionSettingsGetPut.to_json())

# convert the object into a dict
ssl_decryption_settings_get_put_dict = ssl_decryption_settings_get_put_instance.to_dict()
# create an instance of SslDecryptionSettingsGetPut from a dict
ssl_decryption_settings_get_put_from_dict = SslDecryptionSettingsGetPut.from_dict(ssl_decryption_settings_get_put_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


