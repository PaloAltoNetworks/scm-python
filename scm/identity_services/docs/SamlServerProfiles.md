# SamlServerProfiles


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**certificate** | **str** | The identity provider certificate | 
**device** | **str** | The device in which the resource is defined | [optional] 
**entity_id** | **str** | The identity provider ID | 
**folder** | **str** | The folder in which the resource is defined | [optional] 
**id** | **str** | The UUID of the SAML server profile | [readonly] 
**max_clock_skew** | **int** | Maxiumum clock skew | [optional] 
**name** | **str** | The name of the SAML server profile | 
**slo_bindings** | **str** | SAML HTTP binding for SLO requests to the identity provider | [optional] 
**snippet** | **str** | The snippet in which the resource is defined | [optional] 
**sso_bindings** | **str** | SAML HTTP binding for SSO requests to the identity provider | 
**sso_url** | **str** | Identity provider SSO URL | 
**validate_idp_certificate** | **bool** | Validate the identity provider certificate? | [optional] 
**want_auth_requests_signed** | **bool** | Sign SAML message to the identity provider? | [optional] 

## Example

```python
from scm_identity_services.models.saml_server_profiles import SamlServerProfiles

# TODO update the JSON string below
json = "{}"
# create an instance of SamlServerProfiles from a JSON string
saml_server_profiles_instance = SamlServerProfiles.from_json(json)
# print the JSON string representation of the object
print(SamlServerProfiles.to_json())

# convert the object into a dict
saml_server_profiles_dict = saml_server_profiles_instance.to_dict()
# create an instance of SamlServerProfiles from a dict
saml_server_profiles_from_dict = SamlServerProfiles.from_dict(saml_server_profiles_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


