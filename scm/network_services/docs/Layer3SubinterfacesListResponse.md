# Layer3SubinterfacesListResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[Layer3Subinterfaces]**](Layer3Subinterfaces.md) |  | 
**limit** | **int** | The maximum number of results per page | [default to 200]
**offset** | **int** | The offset into the list of results returned | [default to 0]
**total** | **int** | The total count of results | 

## Example

```python
from scm.network_services.models.layer3_subinterfaces_list_response import Layer3SubinterfacesListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of Layer3SubinterfacesListResponse from a JSON string
layer3_subinterfaces_list_response_instance = Layer3SubinterfacesListResponse.from_json(json)
# print the JSON string representation of the object
print(Layer3SubinterfacesListResponse.to_json())

# convert the object into a dict
layer3_subinterfaces_list_response_dict = layer3_subinterfaces_list_response_instance.to_dict()
# create an instance of Layer3SubinterfacesListResponse from a dict
layer3_subinterfaces_list_response_from_dict = Layer3SubinterfacesListResponse.from_dict(layer3_subinterfaces_list_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


