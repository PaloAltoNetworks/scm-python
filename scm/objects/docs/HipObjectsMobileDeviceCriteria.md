# HipObjectsMobileDeviceCriteria


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**applications** | [**HipObjectsMobileDeviceCriteriaApplications**](HipObjectsMobileDeviceCriteriaApplications.md) |  | [optional] 
**disk_encrypted** | **bool** | If device&#39;s disk is encrypted | [optional] 
**imei** | [**HipObjectsHostInfoCriteriaClientVersion**](HipObjectsHostInfoCriteriaClientVersion.md) |  | [optional] 
**jailbroken** | **bool** | If device is by rooted/jailbroken | [optional] 
**last_checkin_time** | [**HipObjectsMobileDeviceCriteriaLastCheckinTime**](HipObjectsMobileDeviceCriteriaLastCheckinTime.md) |  | [optional] 
**model** | [**HipObjectsHostInfoCriteriaClientVersion**](HipObjectsHostInfoCriteriaClientVersion.md) |  | [optional] 
**passcode_set** | **bool** | If device&#39;s passcode is present | [optional] 
**phone_number** | [**HipObjectsHostInfoCriteriaClientVersion**](HipObjectsHostInfoCriteriaClientVersion.md) |  | [optional] 
**tag** | [**HipObjectsHostInfoCriteriaClientVersion**](HipObjectsHostInfoCriteriaClientVersion.md) |  | [optional] 

## Example

```python
from scm_objects.models.hip_objects_mobile_device_criteria import HipObjectsMobileDeviceCriteria

# TODO update the JSON string below
json = "{}"
# create an instance of HipObjectsMobileDeviceCriteria from a JSON string
hip_objects_mobile_device_criteria_instance = HipObjectsMobileDeviceCriteria.from_json(json)
# print the JSON string representation of the object
print(HipObjectsMobileDeviceCriteria.to_json())

# convert the object into a dict
hip_objects_mobile_device_criteria_dict = hip_objects_mobile_device_criteria_instance.to_dict()
# create an instance of HipObjectsMobileDeviceCriteria from a dict
hip_objects_mobile_device_criteria_from_dict = HipObjectsMobileDeviceCriteria.from_dict(hip_objects_mobile_device_criteria_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


