# HipObjectsDiskEncryptionCriteria

Encryption locations

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**encrypted_locations** | [**List[HipObjectsDiskEncryptionCriteriaEncryptedLocationsInner]**](HipObjectsDiskEncryptionCriteriaEncryptedLocationsInner.md) |  | [optional] 
**is_installed** | **bool** | Is Installed | [optional] [default to True]

## Example

```python
from scm.objects.models.hip_objects_disk_encryption_criteria import HipObjectsDiskEncryptionCriteria

# TODO update the JSON string below
json = "{}"
# create an instance of HipObjectsDiskEncryptionCriteria from a JSON string
hip_objects_disk_encryption_criteria_instance = HipObjectsDiskEncryptionCriteria.from_json(json)
# print the JSON string representation of the object
print(HipObjectsDiskEncryptionCriteria.to_json())

# convert the object into a dict
hip_objects_disk_encryption_criteria_dict = hip_objects_disk_encryption_criteria_instance.to_dict()
# create an instance of HipObjectsDiskEncryptionCriteria from a dict
hip_objects_disk_encryption_criteria_from_dict = HipObjectsDiskEncryptionCriteria.from_dict(hip_objects_disk_encryption_criteria_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


