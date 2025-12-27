# MfaServersMfaVendorTypePingIdentityV1

Integation with [Ping Identity](https://www.pingidentity.com/en/platform.html)

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ping_api_host** | **str** | Ping Identity API hostname | [default to 'idpxny3lm.pingidentity.com']
**ping_baseuri** | **str** | Ping Identity API base URI | [default to '/pingid/rest/4']
**ping_org_alias** | **str** | Ping Identity client organization ID | [optional] 
**ping_timeout** | **int** | Ping Identity timeout (seconds) | [default to 30]
**ping_token** | **str** | Ping Identity API token | 
**ping_use_base64_key** | **str** | Ping Identity Base64 key | 

## Example

```python
from scm.identity_services.models.mfa_servers_mfa_vendor_type_ping_identity_v1 import MfaServersMfaVendorTypePingIdentityV1

# TODO update the JSON string below
json = "{}"
# create an instance of MfaServersMfaVendorTypePingIdentityV1 from a JSON string
mfa_servers_mfa_vendor_type_ping_identity_v1_instance = MfaServersMfaVendorTypePingIdentityV1.from_json(json)
# print the JSON string representation of the object
print(MfaServersMfaVendorTypePingIdentityV1.to_json())

# convert the object into a dict
mfa_servers_mfa_vendor_type_ping_identity_v1_dict = mfa_servers_mfa_vendor_type_ping_identity_v1_instance.to_dict()
# create an instance of MfaServersMfaVendorTypePingIdentityV1 from a dict
mfa_servers_mfa_vendor_type_ping_identity_v1_from_dict = MfaServersMfaVendorTypePingIdentityV1.from_dict(mfa_servers_mfa_vendor_type_ping_identity_v1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


