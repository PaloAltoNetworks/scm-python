# MfaServersMfaVendorTypeRsaSecuridAccessV1

Integration with [RSA SecurID](https://www.rsa.com/products/securid/)

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rsa_accessid** | **str** | RSA SecurID access ID | [optional] 
**rsa_accesskey** | **str** | RSA SecurID access key | [optional] 
**rsa_api_host** | **str** | RSA SecurID hostname | [optional] 
**rsa_assurancepolicyid** | **str** | RSA SecurID assurance level | [optional] 
**rsa_baseuri** | **str** | RSA SecurID API base URI | [optional] [default to '/mfa/v1_1']
**rsa_timeout** | **int** | RSA SecurID timeout (seconds) | [optional] [default to 30]

## Example

```python
from scm_identity_services.models.mfa_servers_mfa_vendor_type_rsa_securid_access_v1 import MfaServersMfaVendorTypeRsaSecuridAccessV1

# TODO update the JSON string below
json = "{}"
# create an instance of MfaServersMfaVendorTypeRsaSecuridAccessV1 from a JSON string
mfa_servers_mfa_vendor_type_rsa_securid_access_v1_instance = MfaServersMfaVendorTypeRsaSecuridAccessV1.from_json(json)
# print the JSON string representation of the object
print(MfaServersMfaVendorTypeRsaSecuridAccessV1.to_json())

# convert the object into a dict
mfa_servers_mfa_vendor_type_rsa_securid_access_v1_dict = mfa_servers_mfa_vendor_type_rsa_securid_access_v1_instance.to_dict()
# create an instance of MfaServersMfaVendorTypeRsaSecuridAccessV1 from a dict
mfa_servers_mfa_vendor_type_rsa_securid_access_v1_from_dict = MfaServersMfaVendorTypeRsaSecuridAccessV1.from_dict(mfa_servers_mfa_vendor_type_rsa_securid_access_v1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


