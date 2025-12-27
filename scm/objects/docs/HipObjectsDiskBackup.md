# HipObjectsDiskBackup


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**criteria** | [**HipObjectsDiskBackupCriteria**](HipObjectsDiskBackupCriteria.md) |  | [optional] 
**exclude_vendor** | **bool** |  | [optional] [default to False]
**vendor** | [**List[HipObjectsAntiMalwareVendorInner]**](HipObjectsAntiMalwareVendorInner.md) | Vendor name | [optional] 

## Example

```python
from scm_objects.models.hip_objects_disk_backup import HipObjectsDiskBackup

# TODO update the JSON string below
json = "{}"
# create an instance of HipObjectsDiskBackup from a JSON string
hip_objects_disk_backup_instance = HipObjectsDiskBackup.from_json(json)
# print the JSON string representation of the object
print(HipObjectsDiskBackup.to_json())

# convert the object into a dict
hip_objects_disk_backup_dict = hip_objects_disk_backup_instance.to_dict()
# create an instance of HipObjectsDiskBackup from a dict
hip_objects_disk_backup_from_dict = HipObjectsDiskBackup.from_dict(hip_objects_disk_backup_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


