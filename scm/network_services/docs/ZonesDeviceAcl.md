# ZonesDeviceAcl


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**exclude_list** | **List[str]** |  | [optional] 
**include_list** | **List[str]** |  | [optional] 

## Example

```python
from scm.network_services.models.zones_device_acl import ZonesDeviceAcl

# TODO update the JSON string below
json = "{}"
# create an instance of ZonesDeviceAcl from a JSON string
zones_device_acl_instance = ZonesDeviceAcl.from_json(json)
# print the JSON string representation of the object
print(ZonesDeviceAcl.to_json())

# convert the object into a dict
zones_device_acl_dict = zones_device_acl_instance.to_dict()
# create an instance of ZonesDeviceAcl from a dict
zones_device_acl_from_dict = ZonesDeviceAcl.from_dict(zones_device_acl_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


