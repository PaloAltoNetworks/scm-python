# DevicesAvailableLicensessInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**authcode** | **str** |  | [optional] [readonly] 
**expires** | **date** |  | [optional] [readonly] 
**feature** | **str** |  | [optional] [readonly] 
**issued** | **date** |  | [optional] [readonly] 

## Example

```python
from scm_config_setup.models.devices_available_licensess_inner import DevicesAvailableLicensessInner

# TODO update the JSON string below
json = "{}"
# create an instance of DevicesAvailableLicensessInner from a JSON string
devices_available_licensess_inner_instance = DevicesAvailableLicensessInner.from_json(json)
# print the JSON string representation of the object
print(DevicesAvailableLicensessInner.to_json())

# convert the object into a dict
devices_available_licensess_inner_dict = devices_available_licensess_inner_instance.to_dict()
# create an instance of DevicesAvailableLicensessInner from a dict
devices_available_licensess_inner_from_dict = DevicesAvailableLicensessInner.from_dict(devices_available_licensess_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


