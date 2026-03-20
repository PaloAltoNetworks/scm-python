# SecurityRuleListResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[SecurityRules]**](SecurityRules.md) |  | [optional] 
**limit** | **int** |  | [optional] [default to 200]
**offset** | **int** |  | [optional] [default to 0]
**total** | **int** |  | [optional] 

## Example

```python
from scm.security_services.models.security_rule_list_response import SecurityRuleListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SecurityRuleListResponse from a JSON string
security_rule_list_response_instance = SecurityRuleListResponse.from_json(json)
# print the JSON string representation of the object
print(SecurityRuleListResponse.to_json())

# convert the object into a dict
security_rule_list_response_dict = security_rule_list_response_instance.to_dict()
# create an instance of SecurityRuleListResponse from a dict
security_rule_list_response_from_dict = SecurityRuleListResponse.from_dict(security_rule_list_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


