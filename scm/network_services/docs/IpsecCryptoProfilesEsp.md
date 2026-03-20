# IpsecCryptoProfilesEsp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**authentication** | **List[str]** | Authentication algorithm | 
**encryption** | **List[str]** | Encryption algorithm | 

## Example

```python
from scm.network_services.models.ipsec_crypto_profiles_esp import IpsecCryptoProfilesEsp

# TODO update the JSON string below
json = "{}"
# create an instance of IpsecCryptoProfilesEsp from a JSON string
ipsec_crypto_profiles_esp_instance = IpsecCryptoProfilesEsp.from_json(json)
# print the JSON string representation of the object
print(IpsecCryptoProfilesEsp.to_json())

# convert the object into a dict
ipsec_crypto_profiles_esp_dict = ipsec_crypto_profiles_esp_instance.to_dict()
# create an instance of IpsecCryptoProfilesEsp from a dict
ipsec_crypto_profiles_esp_from_dict = IpsecCryptoProfilesEsp.from_dict(ipsec_crypto_profiles_esp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


