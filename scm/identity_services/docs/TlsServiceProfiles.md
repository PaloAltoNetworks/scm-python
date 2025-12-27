# TlsServiceProfiles


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**certificate** | **str** | Certificate name | 
**device** | **str** | The device in which the resource is defined | [optional] 
**folder** | **str** | The folder in which the resource is defined | [optional] 
**id** | **str** | The UUID of the TLS service profile | [readonly] 
**name** | **str** | TLS service profile name. The value is &#x60;muCustomDomainSSLProfile&#x60; when it is used on mobile-agent infra settings. | 
**protocol_settings** | [**TlsServiceProfilesProtocolSettings**](TlsServiceProfilesProtocolSettings.md) |  | 
**snippet** | **str** | The snippet in which the resource is defined | [optional] 

## Example

```python
from scm_identity_services.models.tls_service_profiles import TlsServiceProfiles

# TODO update the JSON string below
json = "{}"
# create an instance of TlsServiceProfiles from a JSON string
tls_service_profiles_instance = TlsServiceProfiles.from_json(json)
# print the JSON string representation of the object
print(TlsServiceProfiles.to_json())

# convert the object into a dict
tls_service_profiles_dict = tls_service_profiles_instance.to_dict()
# create an instance of TlsServiceProfiles from a dict
tls_service_profiles_from_dict = TlsServiceProfiles.from_dict(tls_service_profiles_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


