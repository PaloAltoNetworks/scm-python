# RadiusServerProfilesProtocolPEAPMSCHAPv2


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allow_pwd_change** | **bool** |  | [optional] 
**anon_outer_id** | **bool** |  | [optional] 
**radius_cert_profile** | **str** |  | [optional] 

## Example

```python
from scm_identity_services.models.radius_server_profiles_protocol_peapmschapv2 import RadiusServerProfilesProtocolPEAPMSCHAPv2

# TODO update the JSON string below
json = "{}"
# create an instance of RadiusServerProfilesProtocolPEAPMSCHAPv2 from a JSON string
radius_server_profiles_protocol_peapmschapv2_instance = RadiusServerProfilesProtocolPEAPMSCHAPv2.from_json(json)
# print the JSON string representation of the object
print(RadiusServerProfilesProtocolPEAPMSCHAPv2.to_json())

# convert the object into a dict
radius_server_profiles_protocol_peapmschapv2_dict = radius_server_profiles_protocol_peapmschapv2_instance.to_dict()
# create an instance of RadiusServerProfilesProtocolPEAPMSCHAPv2 from a dict
radius_server_profiles_protocol_peapmschapv2_from_dict = RadiusServerProfilesProtocolPEAPMSCHAPv2.from_dict(radius_server_profiles_protocol_peapmschapv2_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


