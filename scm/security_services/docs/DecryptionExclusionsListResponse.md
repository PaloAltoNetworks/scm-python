# DecryptionExclusionsListResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[DecryptionExclusions]**](DecryptionExclusions.md) |  | 
**limit** | **int** | The maximum number of results per page | [default to 200]
**offset** | **int** | The offset into the list of results returned | [default to 0]
**total** | **int** | The total count of results | 

## Example

```python
from scm_security_services.models.decryption_exclusions_list_response import DecryptionExclusionsListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DecryptionExclusionsListResponse from a JSON string
decryption_exclusions_list_response_instance = DecryptionExclusionsListResponse.from_json(json)
# print the JSON string representation of the object
print(DecryptionExclusionsListResponse.to_json())

# convert the object into a dict
decryption_exclusions_list_response_dict = decryption_exclusions_list_response_instance.to_dict()
# create an instance of DecryptionExclusionsListResponse from a dict
decryption_exclusions_list_response_from_dict = DecryptionExclusionsListResponse.from_dict(decryption_exclusions_list_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


