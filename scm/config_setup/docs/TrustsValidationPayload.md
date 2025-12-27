# TrustsValidationPayload


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**donor_tenant_name** | **str** |  | 
**psk** | **str** |  | 
**recipient_tenant_name** | **str** |  | 
**trust_id** | **int** |  | 
**tsg** | **str** |  | 

## Example

```python
from scm_config_setup.models.trusts_validation_payload import TrustsValidationPayload

# TODO update the JSON string below
json = "{}"
# create an instance of TrustsValidationPayload from a JSON string
trusts_validation_payload_instance = TrustsValidationPayload.from_json(json)
# print the JSON string representation of the object
print(TrustsValidationPayload.to_json())

# convert the object into a dict
trusts_validation_payload_dict = trusts_validation_payload_instance.to_dict()
# create an instance of TrustsValidationPayload from a dict
trusts_validation_payload_from_dict = TrustsValidationPayload.from_dict(trusts_validation_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


