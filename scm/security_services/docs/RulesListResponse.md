# RulesListResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[SecurityRules]**](SecurityRules.md) |  | 
**limit** | **int** | The maximum number of results per page | [default to 200]
**offset** | **int** | The offset into the list of results returned | [default to 0]
**total** | **int** | The total count of results | 

## Example

```python
from scm_security_services.models.rules_list_response import RulesListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of RulesListResponse from a JSON string
rules_list_response_instance = RulesListResponse.from_json(json)
# print the JSON string representation of the object
print(RulesListResponse.to_json())

# convert the object into a dict
rules_list_response_dict = rules_list_response_instance.to_dict()
# create an instance of RulesListResponse from a dict
rules_list_response_from_dict = RulesListResponse.from_dict(rules_list_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


