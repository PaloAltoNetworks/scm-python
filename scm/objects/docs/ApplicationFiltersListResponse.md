# ApplicationFiltersListResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[ApplicationFilters]**](ApplicationFilters.md) |  | 
**limit** | **int** | The maximum number of results per page | [default to 200]
**offset** | **int** | The offset into the list of results returned | [default to 0]
**total** | **int** | The total count of results | 

## Example

```python
from scm.objects.models.application_filters_list_response import ApplicationFiltersListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ApplicationFiltersListResponse from a JSON string
application_filters_list_response_instance = ApplicationFiltersListResponse.from_json(json)
# print the JSON string representation of the object
print(ApplicationFiltersListResponse.to_json())

# convert the object into a dict
application_filters_list_response_dict = application_filters_list_response_instance.to_dict()
# create an instance of ApplicationFiltersListResponse from a dict
application_filters_list_response_from_dict = ApplicationFiltersListResponse.from_dict(application_filters_list_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


