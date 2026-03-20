# RemoteNetworksListResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[RemoteNetworks]**](RemoteNetworks.md) |  | 
**limit** | **int** | The maximum number of results per page | [default to 200]
**offset** | **int** | The offset into the list of results returned | [default to 0]
**total** | **int** | The total count of results | 

## Example

```python
from scm.deployment_services.models.remote_networks_list_response import RemoteNetworksListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of RemoteNetworksListResponse from a JSON string
remote_networks_list_response_instance = RemoteNetworksListResponse.from_json(json)
# print the JSON string representation of the object
print(RemoteNetworksListResponse.to_json())

# convert the object into a dict
remote_networks_list_response_dict = remote_networks_list_response_instance.to_dict()
# create an instance of RemoteNetworksListResponse from a dict
remote_networks_list_response_from_dict = RemoteNetworksListResponse.from_dict(remote_networks_list_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


