# IpsecCryptoProfilesLifesize


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gb** | **int** | specify lifesize in gigabytes(GB) | [optional] 
**kb** | **int** | specify lifesize in kilobytes(KB) | [optional] 
**mb** | **int** | specify lifesize in megabytes(MB) | [optional] 
**tb** | **int** | specify lifesize in terabytes(TB) | [optional] 

## Example

```python
from scm.network_services.models.ipsec_crypto_profiles_lifesize import IpsecCryptoProfilesLifesize

# TODO update the JSON string below
json = "{}"
# create an instance of IpsecCryptoProfilesLifesize from a JSON string
ipsec_crypto_profiles_lifesize_instance = IpsecCryptoProfilesLifesize.from_json(json)
# print the JSON string representation of the object
print(IpsecCryptoProfilesLifesize.to_json())

# convert the object into a dict
ipsec_crypto_profiles_lifesize_dict = ipsec_crypto_profiles_lifesize_instance.to_dict()
# create an instance of IpsecCryptoProfilesLifesize from a dict
ipsec_crypto_profiles_lifesize_from_dict = IpsecCryptoProfilesLifesize.from_dict(ipsec_crypto_profiles_lifesize_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


