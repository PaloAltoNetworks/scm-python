# AuthenticationPortalsListResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[AuthenticationPortals]**](AuthenticationPortals.md) |  | 
**limit** | **int** | The maximum number of results per page | [default to 200]
**offset** | **int** | The offset into the list of results returned | [default to 0]
**total** | **int** | The total count of results | 

## Example

```python
from scm.identity_services.models.authentication_portals_list_response import AuthenticationPortalsListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AuthenticationPortalsListResponse from a JSON string
authentication_portals_list_response_instance = AuthenticationPortalsListResponse.from_json(json)
# print the JSON string representation of the object
print(AuthenticationPortalsListResponse.to_json())

# convert the object into a dict
authentication_portals_list_response_dict = authentication_portals_list_response_instance.to_dict()
# create an instance of AuthenticationPortalsListResponse from a dict
authentication_portals_list_response_from_dict = AuthenticationPortalsListResponse.from_dict(authentication_portals_list_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


