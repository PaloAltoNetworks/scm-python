# CertificatesGet


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**algorithm** | **str** | Algorithm | [optional] 
**ca** | **bool** | CA certificate? | [optional] 
**common_name** | **str** | Common name | [optional] 
**common_name_int** | **str** |  | [optional] 
**device** | **str** | The device in which the resource is defined | [optional] 
**expiry_epoch** | **str** |  | [optional] 
**folder** | **str** | The folder in which the resource is defined | [optional] 
**id** | **str** | The UUID of the certificate | [optional] [readonly] 
**issuer** | **str** | Issuer | [optional] 
**issuer_hash** | **str** | Issue hash | [optional] 
**name** | **str** | The name of the certificate | [optional] 
**not_valid_after** | **date** | Not valid after this date | [optional] 
**not_valid_before** | **date** | Not valid before this date | [optional] 
**public_key** | **str** | Public key | [optional] 
**snippet** | **str** | The snippet in which the resource is defined | [optional] 
**subject** | **str** | Subject | [optional] 
**subject_hash** | **str** | Subject hash | [optional] 
**subject_int** | **str** |  | [optional] 

## Example

```python
from scm.identity_services.models.certificates_get import CertificatesGet

# TODO update the JSON string below
json = "{}"
# create an instance of CertificatesGet from a JSON string
certificates_get_instance = CertificatesGet.from_json(json)
# print the JSON string representation of the object
print(CertificatesGet.to_json())

# convert the object into a dict
certificates_get_dict = certificates_get_instance.to_dict()
# create an instance of CertificatesGet from a dict
certificates_get_from_dict = CertificatesGet.from_dict(certificates_get_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


