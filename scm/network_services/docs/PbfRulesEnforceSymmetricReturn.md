# PbfRulesEnforceSymmetricReturn


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | **bool** | Enforce symmetric return? | [optional] 
**nexthop_address_list** | [**List[PbfRulesEnforceSymmetricReturnNexthopAddressListInner]**](PbfRulesEnforceSymmetricReturnNexthopAddressListInner.md) | Next hop IP addresses | [optional] 

## Example

```python
from scm_network_services.models.pbf_rules_enforce_symmetric_return import PbfRulesEnforceSymmetricReturn

# TODO update the JSON string below
json = "{}"
# create an instance of PbfRulesEnforceSymmetricReturn from a JSON string
pbf_rules_enforce_symmetric_return_instance = PbfRulesEnforceSymmetricReturn.from_json(json)
# print the JSON string representation of the object
print(PbfRulesEnforceSymmetricReturn.to_json())

# convert the object into a dict
pbf_rules_enforce_symmetric_return_dict = pbf_rules_enforce_symmetric_return_instance.to_dict()
# create an instance of PbfRulesEnforceSymmetricReturn from a dict
pbf_rules_enforce_symmetric_return_from_dict = PbfRulesEnforceSymmetricReturn.from_dict(pbf_rules_enforce_symmetric_return_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


