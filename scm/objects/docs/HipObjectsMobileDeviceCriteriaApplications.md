# HipObjectsMobileDeviceCriteriaApplications


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**has_malware** | [**HipObjectsMobileDeviceCriteriaApplicationsHasMalware**](HipObjectsMobileDeviceCriteriaApplicationsHasMalware.md) |  | [optional] 
**has_unmanaged_app** | **bool** | Has apps that are not managed | [optional] 
**includes** | [**List[HipObjectsMobileDeviceCriteriaApplicationsHasMalwareYesExcludesInner]**](HipObjectsMobileDeviceCriteriaApplicationsHasMalwareYesExcludesInner.md) |  | [optional] 

## Example

```python
from scm_objects.models.hip_objects_mobile_device_criteria_applications import HipObjectsMobileDeviceCriteriaApplications

# TODO update the JSON string below
json = "{}"
# create an instance of HipObjectsMobileDeviceCriteriaApplications from a JSON string
hip_objects_mobile_device_criteria_applications_instance = HipObjectsMobileDeviceCriteriaApplications.from_json(json)
# print the JSON string representation of the object
print(HipObjectsMobileDeviceCriteriaApplications.to_json())

# convert the object into a dict
hip_objects_mobile_device_criteria_applications_dict = hip_objects_mobile_device_criteria_applications_instance.to_dict()
# create an instance of HipObjectsMobileDeviceCriteriaApplications from a dict
hip_objects_mobile_device_criteria_applications_from_dict = HipObjectsMobileDeviceCriteriaApplications.from_dict(hip_objects_mobile_device_criteria_applications_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


