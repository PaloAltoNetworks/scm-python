# DecryptionRulesTypeSslInboundInspection

add the certificate name for SSL inbound inspection

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**certificates** | **List[str]** | List of certificate names for SSL inbound inspection | [optional] 

## Example

```python
from scm.security_services.models.decryption_rules_type_ssl_inbound_inspection import DecryptionRulesTypeSslInboundInspection

# TODO update the JSON string below
json = "{}"
# create an instance of DecryptionRulesTypeSslInboundInspection from a JSON string
decryption_rules_type_ssl_inbound_inspection_instance = DecryptionRulesTypeSslInboundInspection.from_json(json)
# print the JSON string representation of the object
print(DecryptionRulesTypeSslInboundInspection.to_json())

# convert the object into a dict
decryption_rules_type_ssl_inbound_inspection_dict = decryption_rules_type_ssl_inbound_inspection_instance.to_dict()
# create an instance of DecryptionRulesTypeSslInboundInspection from a dict
decryption_rules_type_ssl_inbound_inspection_from_dict = DecryptionRulesTypeSslInboundInspection.from_dict(decryption_rules_type_ssl_inbound_inspection_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


