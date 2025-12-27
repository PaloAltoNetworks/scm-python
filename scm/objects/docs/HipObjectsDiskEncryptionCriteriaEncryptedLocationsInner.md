# HipObjectsDiskEncryptionCriteriaEncryptedLocationsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**encryption_state** | [**HipObjectsDiskEncryptionCriteriaEncryptedLocationsInnerEncryptionState**](HipObjectsDiskEncryptionCriteriaEncryptedLocationsInnerEncryptionState.md) |  | [optional] 
**name** | **str** | Encryption location | 

## Example

```python
from scm_objects.models.hip_objects_disk_encryption_criteria_encrypted_locations_inner import HipObjectsDiskEncryptionCriteriaEncryptedLocationsInner

# TODO update the JSON string below
json = "{}"
# create an instance of HipObjectsDiskEncryptionCriteriaEncryptedLocationsInner from a JSON string
hip_objects_disk_encryption_criteria_encrypted_locations_inner_instance = HipObjectsDiskEncryptionCriteriaEncryptedLocationsInner.from_json(json)
# print the JSON string representation of the object
print(HipObjectsDiskEncryptionCriteriaEncryptedLocationsInner.to_json())

# convert the object into a dict
hip_objects_disk_encryption_criteria_encrypted_locations_inner_dict = hip_objects_disk_encryption_criteria_encrypted_locations_inner_instance.to_dict()
# create an instance of HipObjectsDiskEncryptionCriteriaEncryptedLocationsInner from a dict
hip_objects_disk_encryption_criteria_encrypted_locations_inner_from_dict = HipObjectsDiskEncryptionCriteriaEncryptedLocationsInner.from_dict(hip_objects_disk_encryption_criteria_encrypted_locations_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


