# DecryptionRulesType

The type of decryption

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ssl_forward_proxy** | **object** |  | [optional] 
**ssl_inbound_inspection** | **str** | add the certificate name for SSL inbound inspection | [optional] 

## Example

```python
from scm_security_services.models.decryption_rules_type import DecryptionRulesType

# TODO update the JSON string below
json = "{}"
# create an instance of DecryptionRulesType from a JSON string
decryption_rules_type_instance = DecryptionRulesType.from_json(json)
# print the JSON string representation of the object
print(DecryptionRulesType.to_json())

# convert the object into a dict
decryption_rules_type_dict = decryption_rules_type_instance.to_dict()
# create an instance of DecryptionRulesType from a dict
decryption_rules_type_from_dict = DecryptionRulesType.from_dict(decryption_rules_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


