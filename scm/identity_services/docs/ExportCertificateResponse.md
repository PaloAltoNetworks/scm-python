# ExportCertificateResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**certificate** | **str** |  | [optional] 

## Example

```python
from scm.identity_services.models.export_certificate_response import ExportCertificateResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ExportCertificateResponse from a JSON string
export_certificate_response_instance = ExportCertificateResponse.from_json(json)
# print the JSON string representation of the object
print(ExportCertificateResponse.to_json())

# convert the object into a dict
export_certificate_response_dict = export_certificate_response_instance.to_dict()
# create an instance of ExportCertificateResponse from a dict
export_certificate_response_from_dict = ExportCertificateResponse.from_dict(export_certificate_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


