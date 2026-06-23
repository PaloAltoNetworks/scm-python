# DiscoveredApplications


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**applications** | [**List[DiscoveredApplicationsApplicationsInner]**](DiscoveredApplicationsApplicationsInner.md) |  | [optional] 
**cie_tenant_id** | **str** |  | [optional] 
**count** | **float** |  | [optional] 
**tenant_id** | **str** |  | [optional] 

## Example

```python
from scm.ztna_connector_all.models.discovered_applications import DiscoveredApplications

# TODO update the JSON string below
json = "{}"
# create an instance of DiscoveredApplications from a JSON string
discovered_applications_instance = DiscoveredApplications.from_json(json)
# print the JSON string representation of the object
print(DiscoveredApplications.to_json())

# convert the object into a dict
discovered_applications_dict = discovered_applications_instance.to_dict()
# create an instance of DiscoveredApplications from a dict
discovered_applications_from_dict = DiscoveredApplications.from_dict(discovered_applications_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


