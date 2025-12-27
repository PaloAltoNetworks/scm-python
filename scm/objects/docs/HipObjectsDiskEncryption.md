# HipObjectsDiskEncryption


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**criteria** | [**HipObjectsDiskEncryptionCriteria**](HipObjectsDiskEncryptionCriteria.md) |  | [optional] 
**exclude_vendor** | **bool** |  | [optional] [default to False]
**vendor** | [**List[HipObjectsAntiMalwareVendorInner]**](HipObjectsAntiMalwareVendorInner.md) | Vendor name | [optional] 

## Example

```python
from scm.objects.models.hip_objects_disk_encryption import HipObjectsDiskEncryption

# TODO update the JSON string below
json = "{}"
# create an instance of HipObjectsDiskEncryption from a JSON string
hip_objects_disk_encryption_instance = HipObjectsDiskEncryption.from_json(json)
# print the JSON string representation of the object
print(HipObjectsDiskEncryption.to_json())

# convert the object into a dict
hip_objects_disk_encryption_dict = hip_objects_disk_encryption_instance.to_dict()
# create an instance of HipObjectsDiskEncryption from a dict
hip_objects_disk_encryption_from_dict = HipObjectsDiskEncryption.from_dict(hip_objects_disk_encryption_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


