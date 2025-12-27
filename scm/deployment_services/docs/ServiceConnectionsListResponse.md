# ServiceConnectionsListResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[ServiceConnections]**](ServiceConnections.md) |  | 
**limit** | **int** | The maximum number of results per page | [default to 200]
**offset** | **int** | The offset into the list of results returned | [default to 0]
**total** | **int** | The total count of results | 

## Example

```python
from scm_deployment_services.models.service_connections_list_response import ServiceConnectionsListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceConnectionsListResponse from a JSON string
service_connections_list_response_instance = ServiceConnectionsListResponse.from_json(json)
# print the JSON string representation of the object
print(ServiceConnectionsListResponse.to_json())

# convert the object into a dict
service_connections_list_response_dict = service_connections_list_response_instance.to_dict()
# create an instance of ServiceConnectionsListResponse from a dict
service_connections_list_response_from_dict = ServiceConnectionsListResponse.from_dict(service_connections_list_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


