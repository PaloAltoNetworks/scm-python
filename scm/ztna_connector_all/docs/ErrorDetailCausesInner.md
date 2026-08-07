# ErrorDetailCausesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** | Cause message | [optional] 
**module** | **str** | Module where the cause originated | [optional] 

## Example

```python
from scm.ztna_connector_all.models.error_detail_causes_inner import ErrorDetailCausesInner

# TODO update the JSON string below
json = "{}"
# create an instance of ErrorDetailCausesInner from a JSON string
error_detail_causes_inner_instance = ErrorDetailCausesInner.from_json(json)
# print the JSON string representation of the object
print(ErrorDetailCausesInner.to_json())

# convert the object into a dict
error_detail_causes_inner_dict = error_detail_causes_inner_instance.to_dict()
# create an instance of ErrorDetailCausesInner from a dict
error_detail_causes_inner_from_dict = ErrorDetailCausesInner.from_dict(error_detail_causes_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


