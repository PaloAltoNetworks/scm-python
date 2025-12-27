# PBFRulesListResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[PbfRules]**](PbfRules.md) |  | 
**limit** | **int** | The maximum number of results per page | [default to 200]
**offset** | **int** | The offset into the list of results returned | [default to 0]
**total** | **int** | The total count of results | 

## Example

```python
from scm_network_services.models.pbf_rules_list_response import PBFRulesListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PBFRulesListResponse from a JSON string
pbf_rules_list_response_instance = PBFRulesListResponse.from_json(json)
# print the JSON string representation of the object
print(PBFRulesListResponse.to_json())

# convert the object into a dict
pbf_rules_list_response_dict = pbf_rules_list_response_instance.to_dict()
# create an instance of PBFRulesListResponse from a dict
pbf_rules_list_response_from_dict = PBFRulesListResponse.from_dict(pbf_rules_list_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


