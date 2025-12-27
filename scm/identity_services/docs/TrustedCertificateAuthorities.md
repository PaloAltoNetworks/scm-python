# TrustedCertificateAuthorities


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**common_name** | **str** | The trusted certificate authority common name | [optional] 
**expiry_epoch** | **str** |  | [optional] 
**filename** | **str** | Certificate filename | [optional] 
**id** | **str** | The UUID of the trusted certificate authority | [optional] [readonly] 
**issuer** | **str** | Issuer | [optional] 
**name** | **str** | The trusted certificate authority name | [optional] 
**not_valid_after** | **str** | Not valid after this date | [optional] 
**not_valid_before** | **str** | Not valid before this date | [optional] 
**serial_number** | **str** | Serial number | [optional] 
**subject** | **str** | Subject | [optional] 

## Example

```python
from scm_identity_services.models.trusted_certificate_authorities import TrustedCertificateAuthorities

# TODO update the JSON string below
json = "{}"
# create an instance of TrustedCertificateAuthorities from a JSON string
trusted_certificate_authorities_instance = TrustedCertificateAuthorities.from_json(json)
# print the JSON string representation of the object
print(TrustedCertificateAuthorities.to_json())

# convert the object into a dict
trusted_certificate_authorities_dict = trusted_certificate_authorities_instance.to_dict()
# create an instance of TrustedCertificateAuthorities from a dict
trusted_certificate_authorities_from_dict = TrustedCertificateAuthorities.from_dict(trusted_certificate_authorities_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


