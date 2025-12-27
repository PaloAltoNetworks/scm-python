# HipObjects


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**anti_malware** | [**HipObjectsAntiMalware**](HipObjectsAntiMalware.md) |  | [optional] 
**certificate** | [**HipObjectsCertificate**](HipObjectsCertificate.md) |  | [optional] 
**custom_checks** | [**HipObjectsCustomChecks**](HipObjectsCustomChecks.md) |  | [optional] 
**data_loss_prevention** | [**HipObjectsDataLossPrevention**](HipObjectsDataLossPrevention.md) |  | [optional] 
**description** | **str** |  | [optional] 
**device** | **str** | The device in which the resource is defined | [optional] 
**disk_backup** | [**HipObjectsDiskBackup**](HipObjectsDiskBackup.md) |  | [optional] 
**disk_encryption** | [**HipObjectsDiskEncryption**](HipObjectsDiskEncryption.md) |  | [optional] 
**firewall** | [**HipObjectsFirewall**](HipObjectsFirewall.md) |  | [optional] 
**folder** | **str** | The folder in which the resource is defined | [optional] 
**host_info** | [**HipObjectsHostInfo**](HipObjectsHostInfo.md) |  | [optional] 
**id** | **str** | UUID of the resource | [readonly] 
**mobile_device** | [**HipObjectsMobileDevice**](HipObjectsMobileDevice.md) |  | [optional] 
**name** | **str** | The name of the HIP object | 
**network_info** | [**HipObjectsNetworkInfo**](HipObjectsNetworkInfo.md) |  | [optional] 
**patch_management** | [**HipObjectsPatchManagement**](HipObjectsPatchManagement.md) |  | [optional] 
**snippet** | **str** | The snippet in which the resource is defined | [optional] 

## Example

```python
from scm_objects.models.hip_objects import HipObjects

# TODO update the JSON string below
json = "{}"
# create an instance of HipObjects from a JSON string
hip_objects_instance = HipObjects.from_json(json)
# print the JSON string representation of the object
print(HipObjects.to_json())

# convert the object into a dict
hip_objects_dict = hip_objects_instance.to_dict()
# create an instance of HipObjects from a dict
hip_objects_from_dict = HipObjects.from_dict(hip_objects_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


