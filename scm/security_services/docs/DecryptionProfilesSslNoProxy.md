# DecryptionProfilesSslNoProxy


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**block_expired_certificate** | **bool** |  | [optional] [default to False]
**block_untrusted_issuer** | **bool** |  | [optional] [default to False]

## Example

```python
from scm_security_services.models.decryption_profiles_ssl_no_proxy import DecryptionProfilesSslNoProxy

# TODO update the JSON string below
json = "{}"
# create an instance of DecryptionProfilesSslNoProxy from a JSON string
decryption_profiles_ssl_no_proxy_instance = DecryptionProfilesSslNoProxy.from_json(json)
# print the JSON string representation of the object
print(DecryptionProfilesSslNoProxy.to_json())

# convert the object into a dict
decryption_profiles_ssl_no_proxy_dict = decryption_profiles_ssl_no_proxy_instance.to_dict()
# create an instance of DecryptionProfilesSslNoProxy from a dict
decryption_profiles_ssl_no_proxy_from_dict = DecryptionProfilesSslNoProxy.from_dict(decryption_profiles_ssl_no_proxy_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


