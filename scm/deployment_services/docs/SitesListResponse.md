# SitesListResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[Sites]**](Sites.md) |  | 
**limit** | **int** | The maximum number of results per page | [default to 200]
**offset** | **int** | The offset into the list of results returned | [default to 0]
**total** | **int** | The total count of results | 

## Example

```python
from scm_deployment_services.models.sites_list_response import SitesListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SitesListResponse from a JSON string
sites_list_response_instance = SitesListResponse.from_json(json)
# print the JSON string representation of the object
print(SitesListResponse.to_json())

# convert the object into a dict
sites_list_response_dict = sites_list_response_instance.to_dict()
# create an instance of SitesListResponse from a dict
sites_list_response_from_dict = SitesListResponse.from_dict(sites_list_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


