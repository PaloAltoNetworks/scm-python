# MfaServersMfaVendorType

The MFA vendor type

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**duo_security_v2** | [**MfaServersMfaVendorTypeDuoSecurityV2**](MfaServersMfaVendorTypeDuoSecurityV2.md) |  | [optional] 
**okta_adaptive_v1** | [**MfaServersMfaVendorTypeOktaAdaptiveV1**](MfaServersMfaVendorTypeOktaAdaptiveV1.md) |  | [optional] 
**ping_identity_v1** | [**MfaServersMfaVendorTypePingIdentityV1**](MfaServersMfaVendorTypePingIdentityV1.md) |  | [optional] 
**rsa_securid_access_v1** | [**MfaServersMfaVendorTypeRsaSecuridAccessV1**](MfaServersMfaVendorTypeRsaSecuridAccessV1.md) |  | [optional] 

## Example

```python
from scm.identity_services.models.mfa_servers_mfa_vendor_type import MfaServersMfaVendorType

# TODO update the JSON string below
json = "{}"
# create an instance of MfaServersMfaVendorType from a JSON string
mfa_servers_mfa_vendor_type_instance = MfaServersMfaVendorType.from_json(json)
# print the JSON string representation of the object
print(MfaServersMfaVendorType.to_json())

# convert the object into a dict
mfa_servers_mfa_vendor_type_dict = mfa_servers_mfa_vendor_type_instance.to_dict()
# create an instance of MfaServersMfaVendorType from a dict
mfa_servers_mfa_vendor_type_from_dict = MfaServersMfaVendorType.from_dict(mfa_servers_mfa_vendor_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


