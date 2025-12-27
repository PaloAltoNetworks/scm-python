# IkeCryptoProfiles


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**authentication_multiple** | **int** | IKEv2 SA reauthentication interval equals authetication-multiple * rekey-lifetime; 0 means reauthentication disabled | [optional] [default to 0]
**device** | **str** | The device in which the resource is defined | [optional] 
**dh_group** | **List[str]** |  | 
**encryption** | **List[str]** | Encryption algorithm | 
**folder** | **str** | The folder in which the resource is defined | [optional] 
**hash** | **List[str]** |  | 
**id** | **str** | UUID of the resource | [optional] [readonly] 
**lifetime** | [**IkeCryptoProfilesLifetime**](IkeCryptoProfilesLifetime.md) |  | [optional] 
**name** | **str** | Alphanumeric string begin with letter: [0-9a-zA-Z._-] | 
**snippet** | **str** | The snippet in which the resource is defined | [optional] 

## Example

```python
from scm_network_services.models.ike_crypto_profiles import IkeCryptoProfiles

# TODO update the JSON string below
json = "{}"
# create an instance of IkeCryptoProfiles from a JSON string
ike_crypto_profiles_instance = IkeCryptoProfiles.from_json(json)
# print the JSON string representation of the object
print(IkeCryptoProfiles.to_json())

# convert the object into a dict
ike_crypto_profiles_dict = ike_crypto_profiles_instance.to_dict()
# create an instance of IkeCryptoProfiles from a dict
ike_crypto_profiles_from_dict = IkeCryptoProfiles.from_dict(ike_crypto_profiles_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


