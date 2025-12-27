# Layer2SubinterfacesListResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[Layer2Subinterfaces]**](Layer2Subinterfaces.md) |  | 
**limit** | **int** | The maximum number of results per page | [default to 200]
**offset** | **int** | The offset into the list of results returned | [default to 0]
**total** | **int** | The total count of results | 

## Example

```python
from scm_network_services.models.layer2_subinterfaces_list_response import Layer2SubinterfacesListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of Layer2SubinterfacesListResponse from a JSON string
layer2_subinterfaces_list_response_instance = Layer2SubinterfacesListResponse.from_json(json)
# print the JSON string representation of the object
print(Layer2SubinterfacesListResponse.to_json())

# convert the object into a dict
layer2_subinterfaces_list_response_dict = layer2_subinterfaces_list_response_instance.to_dict()
# create an instance of Layer2SubinterfacesListResponse from a dict
layer2_subinterfaces_list_response_from_dict = Layer2SubinterfacesListResponse.from_dict(layer2_subinterfaces_list_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


