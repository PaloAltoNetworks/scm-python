# DecryptionExclusions


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** |  | [optional] 
**device** | **str** | The device in which the resource is defined | [optional] 
**folder** | **str** | The folder in which the resource is defined | [optional] 
**id** | **str** | UUID of the resource | [optional] [readonly] 
**name** | **str** |  | 
**snippet** | **str** | The snippet in which the resource is defined | [optional] 

## Example

```python
from scm.security_services.models.decryption_exclusions import DecryptionExclusions

# TODO update the JSON string below
json = "{}"
# create an instance of DecryptionExclusions from a JSON string
decryption_exclusions_instance = DecryptionExclusions.from_json(json)
# print the JSON string representation of the object
print(DecryptionExclusions.to_json())

# convert the object into a dict
decryption_exclusions_dict = decryption_exclusions_instance.to_dict()
# create an instance of DecryptionExclusions from a dict
decryption_exclusions_from_dict = DecryptionExclusions.from_dict(decryption_exclusions_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


