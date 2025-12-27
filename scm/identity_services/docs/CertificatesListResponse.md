# CertificatesListResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[CertificatesGet]**](CertificatesGet.md) |  | 
**limit** | **int** | The maximum number of results per page | [default to 200]
**offset** | **int** | The offset into the list of results returned | [default to 0]
**total** | **int** | The total count of results | 

## Example

```python
from scm_identity_services.models.certificates_list_response import CertificatesListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CertificatesListResponse from a JSON string
certificates_list_response_instance = CertificatesListResponse.from_json(json)
# print the JSON string representation of the object
print(CertificatesListResponse.to_json())

# convert the object into a dict
certificates_list_response_dict = certificates_list_response_instance.to_dict()
# create an instance of CertificatesListResponse from a dict
certificates_list_response_from_dict = CertificatesListResponse.from_dict(certificates_list_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


