# DevicesListResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[Devices]**](Devices.md) |  | 
**limit** | **int** | The maximum number of results per page | [default to 200]
**offset** | **int** | The offset into the list of results returned | [default to 0]
**total** | **int** | The total count of results | 

## Example

```python
from scm.config_setup.models.devices_list_response import DevicesListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DevicesListResponse from a JSON string
devices_list_response_instance = DevicesListResponse.from_json(json)
# print the JSON string representation of the object
print(DevicesListResponse.to_json())

# convert the object into a dict
devices_list_response_dict = devices_list_response_instance.to_dict()
# create an instance of DevicesListResponse from a dict
devices_list_response_from_dict = DevicesListResponse.from_dict(devices_list_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


