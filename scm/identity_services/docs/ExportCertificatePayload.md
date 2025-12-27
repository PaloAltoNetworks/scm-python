# ExportCertificatePayload


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**format** | **str** |  | 
**passphrase** | **str** |  | [optional] 

## Example

```python
from scm_identity_services.models.export_certificate_payload import ExportCertificatePayload

# TODO update the JSON string below
json = "{}"
# create an instance of ExportCertificatePayload from a JSON string
export_certificate_payload_instance = ExportCertificatePayload.from_json(json)
# print the JSON string representation of the object
print(ExportCertificatePayload.to_json())

# convert the object into a dict
export_certificate_payload_dict = export_certificate_payload_instance.to_dict()
# create an instance of ExportCertificatePayload from a dict
export_certificate_payload_from_dict = ExportCertificatePayload.from_dict(export_certificate_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


