# ScepProfiles


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**algorithm** | [**ScepProfilesAlgorithm**](ScepProfilesAlgorithm.md) |  | 
**ca_identity_name** | **str** | Certificate Authority identity | 
**certificate_attributes** | [**ScepProfilesCertificateAttributes**](ScepProfilesCertificateAttributes.md) |  | [optional] 
**device** | **str** | The device in which the resource is defined | [optional] 
**digest** | **str** | Digest for CSR | 
**fingerprint** | **str** | CA certificate fingerprint | [optional] 
**folder** | **str** | The folder in which the resource is defined | [optional] 
**id** | **str** | The UUID of the SCEP profile | [readonly] 
**name** | **str** | The name of the SCEP profile | 
**scep_ca_cert** | **str** | SCEP server CA certificate | [optional] 
**scep_challenge** | [**ScepProfilesScepChallenge**](ScepProfilesScepChallenge.md) |  | 
**scep_client_cert** | **str** | SCEP client ceertificate | [optional] 
**scep_url** | **str** | SCEP server URL | 
**snippet** | **str** | The snippet in which the resource is defined | [optional] 
**subject** | **str** | Subject | [default to 'CN=$USERNAME']
**use_as_digital_signature** | **bool** | Use as digital signature? | [optional] 
**use_for_key_encipherment** | **bool** | Use for key encipherment? | [optional] 

## Example

```python
from scm_identity_services.models.scep_profiles import ScepProfiles

# TODO update the JSON string below
json = "{}"
# create an instance of ScepProfiles from a JSON string
scep_profiles_instance = ScepProfiles.from_json(json)
# print the JSON string representation of the object
print(ScepProfiles.to_json())

# convert the object into a dict
scep_profiles_dict = scep_profiles_instance.to_dict()
# create an instance of ScepProfiles from a dict
scep_profiles_from_dict = ScepProfiles.from_dict(scep_profiles_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


