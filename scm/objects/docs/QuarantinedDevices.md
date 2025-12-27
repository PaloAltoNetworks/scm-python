# QuarantinedDevices


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**host_id** | **str** | Device host ID | 
**serial_number** | **str** | Device serial number | [optional] 

## Example

```python
from scm.objects.models.quarantined_devices import QuarantinedDevices

# TODO update the JSON string below
json = "{}"
# create an instance of QuarantinedDevices from a JSON string
quarantined_devices_instance = QuarantinedDevices.from_json(json)
# print the JSON string representation of the object
print(QuarantinedDevices.to_json())

# convert the object into a dict
quarantined_devices_dict = quarantined_devices_instance.to_dict()
# create an instance of QuarantinedDevices from a dict
quarantined_devices_from_dict = QuarantinedDevices.from_dict(quarantined_devices_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


