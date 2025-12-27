# HipObjectsDataLossPrevention


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**criteria** | [**HipObjectsDataLossPreventionCriteria**](HipObjectsDataLossPreventionCriteria.md) |  | [optional] 
**exclude_vendor** | **bool** |  | [optional] [default to False]
**vendor** | [**List[HipObjectsDataLossPreventionVendorInner]**](HipObjectsDataLossPreventionVendorInner.md) | Vendor name | [optional] 

## Example

```python
from scm_objects.models.hip_objects_data_loss_prevention import HipObjectsDataLossPrevention

# TODO update the JSON string below
json = "{}"
# create an instance of HipObjectsDataLossPrevention from a JSON string
hip_objects_data_loss_prevention_instance = HipObjectsDataLossPrevention.from_json(json)
# print the JSON string representation of the object
print(HipObjectsDataLossPrevention.to_json())

# convert the object into a dict
hip_objects_data_loss_prevention_dict = hip_objects_data_loss_prevention_instance.to_dict()
# create an instance of HipObjectsDataLossPrevention from a dict
hip_objects_data_loss_prevention_from_dict = HipObjectsDataLossPrevention.from_dict(hip_objects_data_loss_prevention_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


