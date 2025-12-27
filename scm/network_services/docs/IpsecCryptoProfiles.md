# IpsecCryptoProfiles


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ah** | [**IpsecCryptoProfilesAh**](IpsecCryptoProfilesAh.md) |  | [optional] 
**device** | **str** | The device in which the resource is defined | [optional] 
**dh_group** | **str** | phase-2 DH group (PFS DH group) | [optional] [default to 'group2']
**esp** | [**IpsecCryptoProfilesEsp**](IpsecCryptoProfilesEsp.md) |  | [optional] 
**folder** | **str** | The folder in which the resource is defined | [optional] 
**id** | **str** | UUID of the resource | [optional] [readonly] 
**lifesize** | [**IpsecCryptoProfilesLifesize**](IpsecCryptoProfilesLifesize.md) |  | [optional] 
**lifetime** | [**IpsecCryptoProfilesLifetime**](IpsecCryptoProfilesLifetime.md) |  | 
**name** | **str** | Alphanumeric string begin with letter: [0-9a-zA-Z._-] | 
**snippet** | **str** | The snippet in which the resource is defined | [optional] 

## Example

```python
from scm_network_services.models.ipsec_crypto_profiles import IpsecCryptoProfiles

# TODO update the JSON string below
json = "{}"
# create an instance of IpsecCryptoProfiles from a JSON string
ipsec_crypto_profiles_instance = IpsecCryptoProfiles.from_json(json)
# print the JSON string representation of the object
print(IpsecCryptoProfiles.to_json())

# convert the object into a dict
ipsec_crypto_profiles_dict = ipsec_crypto_profiles_instance.to_dict()
# create an instance of IpsecCryptoProfiles from a dict
ipsec_crypto_profiles_from_dict = IpsecCryptoProfiles.from_dict(ipsec_crypto_profiles_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


