# DiscoveredApplicationsApplicationsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**app_spec** | [**List[DiscoveredApplicationsApplicationsInnerAppSpecInner]**](DiscoveredApplicationsApplicationsInnerAppSpecInner.md) |  | [optional] 
**fqdn** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**port** | **str** |  | [optional] 
**protocol** | **str** |  | [optional] 
**provider** | **str** |  | [optional] 

## Example

```python
from scm.ztna_connector_all.models.discovered_applications_applications_inner import DiscoveredApplicationsApplicationsInner

# TODO update the JSON string below
json = "{}"
# create an instance of DiscoveredApplicationsApplicationsInner from a JSON string
discovered_applications_applications_inner_instance = DiscoveredApplicationsApplicationsInner.from_json(json)
# print the JSON string representation of the object
print(DiscoveredApplicationsApplicationsInner.to_json())

# convert the object into a dict
discovered_applications_applications_inner_dict = discovered_applications_applications_inner_instance.to_dict()
# create an instance of DiscoveredApplicationsApplicationsInner from a dict
discovered_applications_applications_inner_from_dict = DiscoveredApplicationsApplicationsInner.from_dict(discovered_applications_applications_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


