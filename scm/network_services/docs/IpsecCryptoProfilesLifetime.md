# IpsecCryptoProfilesLifetime

Ipsec crypto profile lifetime

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**days** | **int** | specify lifetime in days | [optional] 
**hours** | **int** | specify lifetime in hours | [optional] 
**minutes** | **int** | specify lifetime in minutes | [optional] 
**seconds** | **int** | specify lifetime in seconds | [optional] 

## Example

```python
from scm_network_services.models.ipsec_crypto_profiles_lifetime import IpsecCryptoProfilesLifetime

# TODO update the JSON string below
json = "{}"
# create an instance of IpsecCryptoProfilesLifetime from a JSON string
ipsec_crypto_profiles_lifetime_instance = IpsecCryptoProfilesLifetime.from_json(json)
# print the JSON string representation of the object
print(IpsecCryptoProfilesLifetime.to_json())

# convert the object into a dict
ipsec_crypto_profiles_lifetime_dict = ipsec_crypto_profiles_lifetime_instance.to_dict()
# create an instance of IpsecCryptoProfilesLifetime from a dict
ipsec_crypto_profiles_lifetime_from_dict = IpsecCryptoProfilesLifetime.from_dict(ipsec_crypto_profiles_lifetime_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


