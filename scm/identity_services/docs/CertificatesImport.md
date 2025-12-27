# CertificatesImport


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**certificate_file** | **str** | The Base64 encoded content of the certificate public key | 
**device** | **str** | The device in which the resource is defined | [optional] 
**folder** | **str** | The folder in which the resource is defined | [optional] 
**format** | **str** | Certificate format | [default to 'pem']
**key_file** | **str** | The Base64 encoded content of the certificate private key | [optional] 
**name** | **str** | The name of the certificate | 
**passphrase** | **str** | Passphrase to protect the certificate private key | [optional] 
**snippet** | **str** | The snippet in which the resource is defined | [optional] 

## Example

```python
from scm.identity_services.models.certificates_import import CertificatesImport

# TODO update the JSON string below
json = "{}"
# create an instance of CertificatesImport from a JSON string
certificates_import_instance = CertificatesImport.from_json(json)
# print the JSON string representation of the object
print(CertificatesImport.to_json())

# convert the object into a dict
certificates_import_dict = certificates_import_instance.to_dict()
# create an instance of CertificatesImport from a dict
certificates_import_from_dict = CertificatesImport.from_dict(certificates_import_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


