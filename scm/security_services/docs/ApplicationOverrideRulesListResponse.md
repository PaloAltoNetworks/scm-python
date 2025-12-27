# ApplicationOverrideRulesListResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[AppOverrideRules]**](AppOverrideRules.md) |  | 
**limit** | **int** | The maximum number of results per page | [default to 200]
**offset** | **int** | The offset into the list of results returned | [default to 0]
**total** | **int** | The total count of results | 

## Example

```python
from scm_security_services.models.application_override_rules_list_response import ApplicationOverrideRulesListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ApplicationOverrideRulesListResponse from a JSON string
application_override_rules_list_response_instance = ApplicationOverrideRulesListResponse.from_json(json)
# print the JSON string representation of the object
print(ApplicationOverrideRulesListResponse.to_json())

# convert the object into a dict
application_override_rules_list_response_dict = application_override_rules_list_response_instance.to_dict()
# create an instance of ApplicationOverrideRulesListResponse from a dict
application_override_rules_list_response_from_dict = ApplicationOverrideRulesListResponse.from_dict(application_override_rules_list_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


