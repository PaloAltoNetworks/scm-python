# DoSProtectionRulesListResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[DosProtectionRules]**](DosProtectionRules.md) |  | 
**limit** | **int** | The maximum number of results per page | [default to 200]
**offset** | **int** | The offset into the list of results returned | [default to 0]
**total** | **int** | The total count of results | 

## Example

```python
from scm_security_services.models.do_s_protection_rules_list_response import DoSProtectionRulesListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DoSProtectionRulesListResponse from a JSON string
do_s_protection_rules_list_response_instance = DoSProtectionRulesListResponse.from_json(json)
# print the JSON string representation of the object
print(DoSProtectionRulesListResponse.to_json())

# convert the object into a dict
do_s_protection_rules_list_response_dict = do_s_protection_rules_list_response_instance.to_dict()
# create an instance of DoSProtectionRulesListResponse from a dict
do_s_protection_rules_list_response_from_dict = DoSProtectionRulesListResponse.from_dict(do_s_protection_rules_list_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


