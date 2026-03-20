# LicenseResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**configured_licenses** | [**List[LicenseInfo]**](LicenseInfo.md) |  | [optional] 
**license_model** | **List[str]** |  | [optional] 
**operational_license** | **str** | Indicates the currently active license model.  Can be \&quot;agg-bandwidth\&quot;, \&quot;site\&quot;, or \&quot;none\&quot;.  | [optional] 
**purchased_licenses** | [**List[LicenseInfo]**](LicenseInfo.md) |  | [optional] 

## Example

```python
from scm.network_services.models.license_result import LicenseResult

# TODO update the JSON string below
json = "{}"
# create an instance of LicenseResult from a JSON string
license_result_instance = LicenseResult.from_json(json)
# print the JSON string representation of the object
print(LicenseResult.to_json())

# convert the object into a dict
license_result_dict = license_result_instance.to_dict()
# create an instance of LicenseResult from a dict
license_result_from_dict = LicenseResult.from_dict(license_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


