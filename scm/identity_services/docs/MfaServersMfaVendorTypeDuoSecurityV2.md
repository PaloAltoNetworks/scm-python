# MfaServersMfaVendorTypeDuoSecurityV2

Integration with [Duo Security](https://duo.com/product) 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**duo_api_host** | **str** | Duo Security API hostname | 
**duo_baseuri** | **str** | Duo Security API base URI | [default to '/auth/v2']
**duo_integration_key** | **str** | Duo Security integration key | 
**duo_secret_key** | **str** | Duo Security secret key | 
**duo_timeout** | **int** | Duo Security timeout (seconds) | [default to 30]

## Example

```python
from scm_identity_services.models.mfa_servers_mfa_vendor_type_duo_security_v2 import MfaServersMfaVendorTypeDuoSecurityV2

# TODO update the JSON string below
json = "{}"
# create an instance of MfaServersMfaVendorTypeDuoSecurityV2 from a JSON string
mfa_servers_mfa_vendor_type_duo_security_v2_instance = MfaServersMfaVendorTypeDuoSecurityV2.from_json(json)
# print the JSON string representation of the object
print(MfaServersMfaVendorTypeDuoSecurityV2.to_json())

# convert the object into a dict
mfa_servers_mfa_vendor_type_duo_security_v2_dict = mfa_servers_mfa_vendor_type_duo_security_v2_instance.to_dict()
# create an instance of MfaServersMfaVendorTypeDuoSecurityV2 from a dict
mfa_servers_mfa_vendor_type_duo_security_v2_from_dict = MfaServersMfaVendorTypeDuoSecurityV2.from_dict(mfa_servers_mfa_vendor_type_duo_security_v2_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


