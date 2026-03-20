# IkeCryptoProfilesLifetime

Ike crypto profile lifetime

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**days** | **int** | specify lifetime in days | [optional] 
**hours** | **int** | specify lifetime in hours | [optional] 
**minutes** | **int** | specify lifetime in minutes | [optional] 
**seconds** | **int** | specify lifetime in seconds | [optional] 

## Example

```python
from scm.network_services.models.ike_crypto_profiles_lifetime import IkeCryptoProfilesLifetime

# TODO update the JSON string below
json = "{}"
# create an instance of IkeCryptoProfilesLifetime from a JSON string
ike_crypto_profiles_lifetime_instance = IkeCryptoProfilesLifetime.from_json(json)
# print the JSON string representation of the object
print(IkeCryptoProfilesLifetime.to_json())

# convert the object into a dict
ike_crypto_profiles_lifetime_dict = ike_crypto_profiles_lifetime_instance.to_dict()
# create an instance of IkeCryptoProfilesLifetime from a dict
ike_crypto_profiles_lifetime_from_dict = IkeCryptoProfilesLifetime.from_dict(ike_crypto_profiles_lifetime_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


