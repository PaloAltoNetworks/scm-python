# CertificateProfiles


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**block_expired_cert** | **bool** | Block sessions with expired certificates? | [optional] 
**block_timeout_cert** | **bool** | Block session if certificate status cannot be retrieved within timeout? | [optional] 
**block_unauthenticated_cert** | **bool** | Block session if the certificate was not issued to the authenticating device? | [optional] 
**block_unknown_cert** | **bool** | Block session if certificate status is unknown? | [optional] 
**ca_certificates** | [**List[CertificateProfilesCaCertificatesInner]**](CertificateProfilesCaCertificatesInner.md) | An ordered list of CA certificates | 
**cert_status_timeout** | **str** | Certificate status timeout | [optional] 
**crl_receive_timeout** | **str** | CRL receive timeout (seconds) | [optional] 
**device** | **str** | The device in which the resource is defined | [optional] 
**domain** | **str** | User domain | [optional] 
**folder** | **str** | The folder in which the resource is defined | [optional] 
**id** | **str** | The UUID of the certificate profile | [optional] [readonly] 
**name** | **str** | The name of the certificate profile | 
**ocsp_receive_timeout** | **str** | OCSP receive timeout (seconds) | [optional] 
**snippet** | **str** | The snippet in which the resource is defined | [optional] 
**use_crl** | **bool** | Use CRL? | [optional] 
**use_ocsp** | **bool** | Use OCSP? | [optional] 
**username_field** | [**CertificateProfilesUsernameField**](CertificateProfilesUsernameField.md) |  | [optional] 

## Example

```python
from scm.identity_services.models.certificate_profiles import CertificateProfiles

# TODO update the JSON string below
json = "{}"
# create an instance of CertificateProfiles from a JSON string
certificate_profiles_instance = CertificateProfiles.from_json(json)
# print the JSON string representation of the object
print(CertificateProfiles.to_json())

# convert the object into a dict
certificate_profiles_dict = certificate_profiles_instance.to_dict()
# create an instance of CertificateProfiles from a dict
certificate_profiles_from_dict = CertificateProfiles.from_dict(certificate_profiles_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


