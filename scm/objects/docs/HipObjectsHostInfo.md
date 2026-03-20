# HipObjectsHostInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**criteria** | [**HipObjectsHostInfoCriteria**](HipObjectsHostInfoCriteria.md) |  | 

## Example

```python
from scm.objects.models.hip_objects_host_info import HipObjectsHostInfo

# TODO update the JSON string below
json = "{}"
# create an instance of HipObjectsHostInfo from a JSON string
hip_objects_host_info_instance = HipObjectsHostInfo.from_json(json)
# print the JSON string representation of the object
print(HipObjectsHostInfo.to_json())

# convert the object into a dict
hip_objects_host_info_dict = hip_objects_host_info_instance.to_dict()
# create an instance of HipObjectsHostInfo from a dict
hip_objects_host_info_from_dict = HipObjectsHostInfo.from_dict(hip_objects_host_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


