# RegionsGeoLocation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**latitude** | **float** | The latitudinal position of the region | 
**longitude** | **float** | The longitudinal postition of the region | 

## Example

```python
from scm_objects.models.regions_geo_location import RegionsGeoLocation

# TODO update the JSON string below
json = "{}"
# create an instance of RegionsGeoLocation from a JSON string
regions_geo_location_instance = RegionsGeoLocation.from_json(json)
# print the JSON string representation of the object
print(RegionsGeoLocation.to_json())

# convert the object into a dict
regions_geo_location_dict = regions_geo_location_instance.to_dict()
# create an instance of RegionsGeoLocation from a dict
regions_geo_location_from_dict = RegionsGeoLocation.from_dict(regions_geo_location_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


