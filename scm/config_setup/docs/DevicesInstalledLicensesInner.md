# DevicesInstalledLicensesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**authcode** | **str** |  | [optional] [readonly] 
**expired** | **str** |  | [optional] [readonly] 
**expires** | **str** |  | [optional] [readonly] 
**feature** | **str** |  | [optional] [readonly] 
**issued** | **date** |  | [optional] [readonly] 

## Example

```python
from scm.config_setup.models.devices_installed_licenses_inner import DevicesInstalledLicensesInner

# TODO update the JSON string below
json = "{}"
# create an instance of DevicesInstalledLicensesInner from a JSON string
devices_installed_licenses_inner_instance = DevicesInstalledLicensesInner.from_json(json)
# print the JSON string representation of the object
print(DevicesInstalledLicensesInner.to_json())

# convert the object into a dict
devices_installed_licenses_inner_dict = devices_installed_licenses_inner_instance.to_dict()
# create an instance of DevicesInstalledLicensesInner from a dict
devices_installed_licenses_inner_from_dict = DevicesInstalledLicensesInner.from_dict(devices_installed_licenses_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


