# Sites


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address_line_1** | **str** | The address in which the site exists | [optional] 
**address_line_2** | **str** | The address in which the site exists (continued) | [optional] 
**city** | **str** | The city in which the site exists | [optional] 
**country** | **str** | The country in which the site exists | [optional] 
**id** | **str** | The UUID of the site | [optional] [readonly] 
**latitude** | **str** | The latitude coordinate for the site | [optional] 
**license_type** | **str** | The license type of the site | [optional] 
**longitude** | **str** | The longitude coordinate for the site | [optional] 
**members** | [**List[SitesMembersInner]**](SitesMembersInner.md) |  | [optional] 
**name** | **str** | The name of the site | 
**qos** | [**SitesQos**](SitesQos.md) |  | [optional] 
**state** | **str** | The state in which the site exists | [optional] 
**type** | **str** | The site type | [optional] 
**zip_code** | **str** | The postal code in which the site exists | [optional] 

## Example

```python
from scm.deployment_services.models.sites import Sites

# TODO update the JSON string below
json = "{}"
# create an instance of Sites from a JSON string
sites_instance = Sites.from_json(json)
# print the JSON string representation of the object
print(Sites.to_json())

# convert the object into a dict
sites_dict = sites_instance.to_dict()
# create an instance of Sites from a dict
sites_from_dict = Sites.from_dict(sites_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


