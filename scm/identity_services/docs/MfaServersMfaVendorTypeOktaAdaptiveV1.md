# MfaServersMfaVendorTypeOktaAdaptiveV1

Integration with [Okta Adaptive MFA](https://www.okta.com/products/adaptive-multi-factor-authentication)

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**okta_api_host** | **str** | Okta API hostname | 
**okta_baseuri** | **str** |  | [default to '/api/v1']
**okta_org** | **str** | Okta organization | 
**okta_timeout** | **int** | Okta timeout (seconds) | [default to 30]
**okta_token** | **str** | Okta API token | 

## Example

```python
from scm.identity_services.models.mfa_servers_mfa_vendor_type_okta_adaptive_v1 import MfaServersMfaVendorTypeOktaAdaptiveV1

# TODO update the JSON string below
json = "{}"
# create an instance of MfaServersMfaVendorTypeOktaAdaptiveV1 from a JSON string
mfa_servers_mfa_vendor_type_okta_adaptive_v1_instance = MfaServersMfaVendorTypeOktaAdaptiveV1.from_json(json)
# print the JSON string representation of the object
print(MfaServersMfaVendorTypeOktaAdaptiveV1.to_json())

# convert the object into a dict
mfa_servers_mfa_vendor_type_okta_adaptive_v1_dict = mfa_servers_mfa_vendor_type_okta_adaptive_v1_instance.to_dict()
# create an instance of MfaServersMfaVendorTypeOktaAdaptiveV1 from a dict
mfa_servers_mfa_vendor_type_okta_adaptive_v1_from_dict = MfaServersMfaVendorTypeOktaAdaptiveV1.from_dict(mfa_servers_mfa_vendor_type_okta_adaptive_v1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


