# IKEGatewaysListResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[IkeGateways]**](IkeGateways.md) |  | 
**limit** | **int** | The maximum number of results per page | [default to 200]
**offset** | **int** | The offset into the list of results returned | [default to 0]
**total** | **int** | The total count of results | 

## Example

```python
from scm.network_services.models.ike_gateways_list_response import IKEGatewaysListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of IKEGatewaysListResponse from a JSON string
ike_gateways_list_response_instance = IKEGatewaysListResponse.from_json(json)
# print the JSON string representation of the object
print(IKEGatewaysListResponse.to_json())

# convert the object into a dict
ike_gateways_list_response_dict = ike_gateways_list_response_instance.to_dict()
# create an instance of IKEGatewaysListResponse from a dict
ike_gateways_list_response_from_dict = IKEGatewaysListResponse.from_dict(ike_gateways_list_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


