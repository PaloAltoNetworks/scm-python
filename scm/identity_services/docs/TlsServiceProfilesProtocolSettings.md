# TlsServiceProfilesProtocolSettings

Protocol settings

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**auth_algo_sha1** | **bool** | Allow SHA1 authentication? | [optional] 
**auth_algo_sha256** | **bool** | Allow SHA256 authentication? | [optional] 
**auth_algo_sha384** | **bool** | Allow SHA384 authentication? | [optional] 
**enc_algo_aes_128_cbc** | **bool** | Allow AES-128-CBC algorithm? | [optional] 
**enc_algo_aes_128_gcm** | **bool** | Allow AES-128-GCM algorithm? | [optional] 
**enc_algo_aes_256_cbc** | **bool** | Allow AES-256-CBC algorithm? | [optional] 
**enc_algo_aes_256_gcm** | **bool** | Allow algorithm AES-256-GCM | [optional] 
**keyxchg_algo_dhe** | **bool** | Allow DHE algorithm? | [optional] 
**keyxchg_algo_ecdhe** | **bool** | Allow ECDHE algorithm? | [optional] 
**keyxchg_algo_rsa** | **bool** | Allow RSA algorithm? | [optional] 
**max_version** | **str** | Maximum TLS version | [optional] [default to '3']
**min_version** | **str** | Minimum TLS version | [optional] [default to '2']

## Example

```python
from scm.identity_services.models.tls_service_profiles_protocol_settings import TlsServiceProfilesProtocolSettings

# TODO update the JSON string below
json = "{}"
# create an instance of TlsServiceProfilesProtocolSettings from a JSON string
tls_service_profiles_protocol_settings_instance = TlsServiceProfilesProtocolSettings.from_json(json)
# print the JSON string representation of the object
print(TlsServiceProfilesProtocolSettings.to_json())

# convert the object into a dict
tls_service_profiles_protocol_settings_dict = tls_service_profiles_protocol_settings_instance.to_dict()
# create an instance of TlsServiceProfilesProtocolSettings from a dict
tls_service_profiles_protocol_settings_from_dict = TlsServiceProfilesProtocolSettings.from_dict(tls_service_profiles_protocol_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


