# Trusts


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**donor_tenant_name** | **str** |  | [optional] 
**psk** | **str** |  | [optional] 
**recipient_tenant_name** | **str** |  | [optional] 
**trust_id** | **int** |  | [optional] 
**tsg** | **str** |  | [optional] 

## Example

```python
from scm_config_setup.models.trusts import Trusts

# TODO update the JSON string below
json = "{}"
# create an instance of Trusts from a JSON string
trusts_instance = Trusts.from_json(json)
# print the JSON string representation of the object
print(Trusts.to_json())

# convert the object into a dict
trusts_dict = trusts_instance.to_dict()
# create an instance of Trusts from a dict
trusts_from_dict = Trusts.from_dict(trusts_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


