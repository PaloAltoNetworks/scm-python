# RadiusServerProfilesProtocol

The RADIUS authentication protocol

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**chap** | **object** |  | [optional] 
**eap_ttls_with_pap** | [**RadiusServerProfilesProtocolEAPTTLSWithPAP**](RadiusServerProfilesProtocolEAPTTLSWithPAP.md) |  | [optional] 
**pap** | **object** |  | [optional] 
**peap_mschapv2** | [**RadiusServerProfilesProtocolPEAPMSCHAPv2**](RadiusServerProfilesProtocolPEAPMSCHAPv2.md) |  | [optional] 
**peap_with_gtc** | [**RadiusServerProfilesProtocolEAPTTLSWithPAP**](RadiusServerProfilesProtocolEAPTTLSWithPAP.md) |  | [optional] 

## Example

```python
from scm_identity_services.models.radius_server_profiles_protocol import RadiusServerProfilesProtocol

# TODO update the JSON string below
json = "{}"
# create an instance of RadiusServerProfilesProtocol from a JSON string
radius_server_profiles_protocol_instance = RadiusServerProfilesProtocol.from_json(json)
# print the JSON string representation of the object
print(RadiusServerProfilesProtocol.to_json())

# convert the object into a dict
radius_server_profiles_protocol_dict = radius_server_profiles_protocol_instance.to_dict()
# create an instance of RadiusServerProfilesProtocol from a dict
radius_server_profiles_protocol_from_dict = RadiusServerProfilesProtocol.from_dict(radius_server_profiles_protocol_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


