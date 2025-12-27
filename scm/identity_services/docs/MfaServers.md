# MfaServers


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**device** | **str** | The device in which the resource is defined | [optional] 
**folder** | **str** | The folder in which the resource is defined | [optional] 
**id** | **str** | The UUID of the MFA server | [readonly] 
**mfa_cert_profile** | **str** | The MFA server certificate profile | 
**mfa_vendor_type** | [**MfaServersMfaVendorType**](MfaServersMfaVendorType.md) |  | [optional] 
**name** | **str** | The name of the MFA server profile | 
**snippet** | **str** | The snippet in which the resource is defined | [optional] 

## Example

```python
from scm.identity_services.models.mfa_servers import MfaServers

# TODO update the JSON string below
json = "{}"
# create an instance of MfaServers from a JSON string
mfa_servers_instance = MfaServers.from_json(json)
# print the JSON string representation of the object
print(MfaServers.to_json())

# convert the object into a dict
mfa_servers_dict = mfa_servers_instance.to_dict()
# create an instance of MfaServers from a dict
mfa_servers_from_dict = MfaServers.from_dict(mfa_servers_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


