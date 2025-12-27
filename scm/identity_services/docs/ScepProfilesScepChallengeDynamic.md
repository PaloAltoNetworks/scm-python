# ScepProfilesScepChallengeDynamic


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**otp_server_url** | **str** | OTP server URL | [optional] 
**password** | **str** | OTP password | [optional] 
**username** | **str** | OTP username | [optional] 

## Example

```python
from scm_identity_services.models.scep_profiles_scep_challenge_dynamic import ScepProfilesScepChallengeDynamic

# TODO update the JSON string below
json = "{}"
# create an instance of ScepProfilesScepChallengeDynamic from a JSON string
scep_profiles_scep_challenge_dynamic_instance = ScepProfilesScepChallengeDynamic.from_json(json)
# print the JSON string representation of the object
print(ScepProfilesScepChallengeDynamic.to_json())

# convert the object into a dict
scep_profiles_scep_challenge_dynamic_dict = scep_profiles_scep_challenge_dynamic_instance.to_dict()
# create an instance of ScepProfilesScepChallengeDynamic from a dict
scep_profiles_scep_challenge_dynamic_from_dict = ScepProfilesScepChallengeDynamic.from_dict(scep_profiles_scep_challenge_dynamic_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


