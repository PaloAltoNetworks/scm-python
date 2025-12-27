# ApplicationFiltersTagging


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**no_tag** | **bool** |  | [optional] 
**tag** | **List[str]** |  | [optional] 

## Example

```python
from scm_objects.models.application_filters_tagging import ApplicationFiltersTagging

# TODO update the JSON string below
json = "{}"
# create an instance of ApplicationFiltersTagging from a JSON string
application_filters_tagging_instance = ApplicationFiltersTagging.from_json(json)
# print the JSON string representation of the object
print(ApplicationFiltersTagging.to_json())

# convert the object into a dict
application_filters_tagging_dict = application_filters_tagging_instance.to_dict()
# create an instance of ApplicationFiltersTagging from a dict
application_filters_tagging_from_dict = ApplicationFiltersTagging.from_dict(application_filters_tagging_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


