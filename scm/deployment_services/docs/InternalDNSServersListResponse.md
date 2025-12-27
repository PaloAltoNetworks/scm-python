# InternalDNSServersListResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[InternalDnsServers]**](InternalDnsServers.md) |  | 
**limit** | **int** | The maximum number of results per page | [default to 200]
**offset** | **int** | The offset into the list of results returned | [default to 0]
**total** | **int** | The total count of results | 

## Example

```python
from scm_deployment_services.models.internal_dns_servers_list_response import InternalDNSServersListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of InternalDNSServersListResponse from a JSON string
internal_dns_servers_list_response_instance = InternalDNSServersListResponse.from_json(json)
# print the JSON string representation of the object
print(InternalDNSServersListResponse.to_json())

# convert the object into a dict
internal_dns_servers_list_response_dict = internal_dns_servers_list_response_instance.to_dict()
# create an instance of InternalDNSServersListResponse from a dict
internal_dns_servers_list_response_from_dict = InternalDNSServersListResponse.from_dict(internal_dns_servers_list_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


