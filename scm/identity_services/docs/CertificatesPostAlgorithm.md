# CertificatesPostAlgorithm

Encryption algorithm

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ecdsa_number_of_bits** | **float** |  | [optional] 
**rsa_number_of_bits** | **float** |  | [optional] 

## Example

```python
from scm_identity_services.models.certificates_post_algorithm import CertificatesPostAlgorithm

# TODO update the JSON string below
json = "{}"
# create an instance of CertificatesPostAlgorithm from a JSON string
certificates_post_algorithm_instance = CertificatesPostAlgorithm.from_json(json)
# print the JSON string representation of the object
print(CertificatesPostAlgorithm.to_json())

# convert the object into a dict
certificates_post_algorithm_dict = certificates_post_algorithm_instance.to_dict()
# create an instance of CertificatesPostAlgorithm from a dict
certificates_post_algorithm_from_dict = CertificatesPostAlgorithm.from_dict(certificates_post_algorithm_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


