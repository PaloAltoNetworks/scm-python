# ApplicationFilters


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**category** | **List[str]** |  | [optional] 
**device** | **str** | The device in which the resource is defined | [optional] 
**evasive** | **bool** | only True is a valid value | [optional] 
**excessive_bandwidth_use** | **bool** | only True is a valid value | [optional] 
**exclude** | **List[str]** |  | [optional] 
**folder** | **str** | The folder in which the resource is defined | [optional] 
**has_known_vulnerabilities** | **bool** | only True is a valid value | [optional] 
**id** | **str** | UUID of the resource | [optional] [readonly] 
**is_saas** | **bool** | only True is a valid value | [optional] 
**name** | **str** | Alphanumeric string [ 0-9a-zA-Z._-] | 
**new_appid** | **bool** | only True is a valid value | [optional] 
**pervasive** | **bool** | only True is a valid value | [optional] 
**prone_to_misuse** | **bool** | only True is a valid value | [optional] 
**risk** | **List[int]** |  | [optional] 
**saas_certifications** | **List[str]** |  | [optional] 
**saas_risk** | **List[str]** |  | [optional] 
**snippet** | **str** | The snippet in which the resource is defined | [optional] 
**subcategory** | **List[str]** |  | [optional] 
**tagging** | [**ApplicationFiltersTagging**](ApplicationFiltersTagging.md) |  | [optional] 
**technology** | **List[str]** |  | [optional] 
**transfers_files** | **bool** | only True is a valid value | [optional] 
**tunnels_other_apps** | **bool** | only True is a valid value | [optional] 
**used_by_malware** | **bool** | only True is a valid value | [optional] 

## Example

```python
from scm.objects.models.application_filters import ApplicationFilters

# TODO update the JSON string below
json = "{}"
# create an instance of ApplicationFilters from a JSON string
application_filters_instance = ApplicationFilters.from_json(json)
# print the JSON string representation of the object
print(ApplicationFilters.to_json())

# convert the object into a dict
application_filters_dict = application_filters_instance.to_dict()
# create an instance of ApplicationFilters from a dict
application_filters_from_dict = ApplicationFilters.from_dict(application_filters_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


