# ScepProfilesScepChallenge

One Time Password challenge

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dynamic** | [**ScepProfilesScepChallengeDynamic**](ScepProfilesScepChallengeDynamic.md) |  | [optional] 
**fixed** | **str** | Challenge to use for SCEP server on mobile clients | [optional] 
**var_none** | **str** | No OTP | [optional] 

## Example

```python
from scm.identity_services.models.scep_profiles_scep_challenge import ScepProfilesScepChallenge

# TODO update the JSON string below
json = "{}"
# create an instance of ScepProfilesScepChallenge from a JSON string
scep_profiles_scep_challenge_instance = ScepProfilesScepChallenge.from_json(json)
# print the JSON string representation of the object
print(ScepProfilesScepChallenge.to_json())

# convert the object into a dict
scep_profiles_scep_challenge_dict = scep_profiles_scep_challenge_instance.to_dict()
# create an instance of ScepProfilesScepChallenge from a dict
scep_profiles_scep_challenge_from_dict = ScepProfilesScepChallenge.from_dict(scep_profiles_scep_challenge_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


