# AntiSpywareSignaturesListResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[AntiSpywareSignatures]**](AntiSpywareSignatures.md) |  | 
**limit** | **int** | The maximum number of results per page | [default to 200]
**offset** | **int** | The offset into the list of results returned | [default to 0]
**total** | **int** | The total count of results | 

## Example

```python
from scm.security_services.models.anti_spyware_signatures_list_response import AntiSpywareSignaturesListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AntiSpywareSignaturesListResponse from a JSON string
anti_spyware_signatures_list_response_instance = AntiSpywareSignaturesListResponse.from_json(json)
# print the JSON string representation of the object
print(AntiSpywareSignaturesListResponse.to_json())

# convert the object into a dict
anti_spyware_signatures_list_response_dict = anti_spyware_signatures_list_response_instance.to_dict()
# create an instance of AntiSpywareSignaturesListResponse from a dict
anti_spyware_signatures_list_response_from_dict = AntiSpywareSignaturesListResponse.from_dict(anti_spyware_signatures_list_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


