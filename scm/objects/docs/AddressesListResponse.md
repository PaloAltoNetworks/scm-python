# AddressesListResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[Addresses]**](Addresses.md) |  | 
**limit** | **int** | The maximum number of results per page | [default to 200]
**offset** | **int** | The offset into the list of results returned | [default to 0]
**total** | **int** | The total count of results | 

## Example

```python
from scm_objects.models.addresses_list_response import AddressesListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AddressesListResponse from a JSON string
addresses_list_response_instance = AddressesListResponse.from_json(json)
# print the JSON string representation of the object
print(AddressesListResponse.to_json())

# convert the object into a dict
addresses_list_response_dict = addresses_list_response_instance.to_dict()
# create an instance of AddressesListResponse from a dict
addresses_list_response_from_dict = AddressesListResponse.from_dict(addresses_list_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


