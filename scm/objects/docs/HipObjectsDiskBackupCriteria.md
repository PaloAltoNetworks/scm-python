# HipObjectsDiskBackupCriteria


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_installed** | **bool** | Is Installed | [optional] [default to True]
**last_backup_time** | [**HipObjectsAntiMalwareCriteriaLastScanTime**](HipObjectsAntiMalwareCriteriaLastScanTime.md) |  | [optional] 

## Example

```python
from scm_objects.models.hip_objects_disk_backup_criteria import HipObjectsDiskBackupCriteria

# TODO update the JSON string below
json = "{}"
# create an instance of HipObjectsDiskBackupCriteria from a JSON string
hip_objects_disk_backup_criteria_instance = HipObjectsDiskBackupCriteria.from_json(json)
# print the JSON string representation of the object
print(HipObjectsDiskBackupCriteria.to_json())

# convert the object into a dict
hip_objects_disk_backup_criteria_dict = hip_objects_disk_backup_criteria_instance.to_dict()
# create an instance of HipObjectsDiskBackupCriteria from a dict
hip_objects_disk_backup_criteria_from_dict = HipObjectsDiskBackupCriteria.from_dict(hip_objects_disk_backup_criteria_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


