# Locations


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**aggregate_region** | **str** |  | [optional] 
**continent** | **str** | The continent in which the location exists | [optional] 
**display** | **str** | The location as displayed in the Strata Cloud Manager portal | [optional] 
**latitude** | **float** | The latitudinal position of the location | [optional] 
**longitude** | **float** | The longitudinal position of the location | [optional] 
**region** | **str** |  | [optional] 
**value** | **str** |  | [optional] 

## Example

```python
from scm_deployment_services.models.locations import Locations

# TODO update the JSON string below
json = "{}"
# create an instance of Locations from a JSON string
locations_instance = Locations.from_json(json)
# print the JSON string representation of the object
print(Locations.to_json())

# convert the object into a dict
locations_dict = locations_instance.to_dict()
# create an instance of Locations from a dict
locations_from_dict = Locations.from_dict(locations_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


