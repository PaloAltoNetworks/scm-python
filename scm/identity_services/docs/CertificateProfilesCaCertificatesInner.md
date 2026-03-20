# CertificateProfilesCaCertificatesInner

CA certificate

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**default_ocsp_url** | **str** | Default OCSP URL | [optional] 
**name** | **str** | CA certificate name | 
**ocsp_verify_cert** | **str** | OCSP verify certificate | [optional] 
**template_name** | **str** | Template name/OID | [optional] 

## Example

```python
from scm.identity_services.models.certificate_profiles_ca_certificates_inner import CertificateProfilesCaCertificatesInner

# TODO update the JSON string below
json = "{}"
# create an instance of CertificateProfilesCaCertificatesInner from a JSON string
certificate_profiles_ca_certificates_inner_instance = CertificateProfilesCaCertificatesInner.from_json(json)
# print the JSON string representation of the object
print(CertificateProfilesCaCertificatesInner.to_json())

# convert the object into a dict
certificate_profiles_ca_certificates_inner_dict = certificate_profiles_ca_certificates_inner_instance.to_dict()
# create an instance of CertificateProfilesCaCertificatesInner from a dict
certificate_profiles_ca_certificates_inner_from_dict = CertificateProfilesCaCertificatesInner.from_dict(certificate_profiles_ca_certificates_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


