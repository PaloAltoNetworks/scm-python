# IkeGatewaysAuthenticationCertificate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allow_id_payload_mismatch** | **bool** |  | [optional] 
**certificate_profile** | **str** |  | [optional] 
**local_certificate** | [**IkeGatewaysAuthenticationCertificateLocalCertificate**](IkeGatewaysAuthenticationCertificateLocalCertificate.md) |  | [optional] 
**strict_validation_revocation** | **bool** |  | [optional] 
**use_management_as_source** | **bool** |  | [optional] 

## Example

```python
from scm_network_services.models.ike_gateways_authentication_certificate import IkeGatewaysAuthenticationCertificate

# TODO update the JSON string below
json = "{}"
# create an instance of IkeGatewaysAuthenticationCertificate from a JSON string
ike_gateways_authentication_certificate_instance = IkeGatewaysAuthenticationCertificate.from_json(json)
# print the JSON string representation of the object
print(IkeGatewaysAuthenticationCertificate.to_json())

# convert the object into a dict
ike_gateways_authentication_certificate_dict = ike_gateways_authentication_certificate_instance.to_dict()
# create an instance of IkeGatewaysAuthenticationCertificate from a dict
ike_gateways_authentication_certificate_from_dict = IkeGatewaysAuthenticationCertificate.from_dict(ike_gateways_authentication_certificate_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


