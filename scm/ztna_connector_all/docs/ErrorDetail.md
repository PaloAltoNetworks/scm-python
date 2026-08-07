# ErrorDetail

Error detail information following Google Cloud API CauseInfo format

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Type identifier for the detail object | [optional] 
**causes** | [**List[ErrorDetailCausesInner]**](ErrorDetailCausesInner.md) | Array of cause information objects | [optional] 
**message** | **str** | Detailed error message | [optional] 

## Example

```python
from scm.ztna_connector_all.models.error_detail import ErrorDetail

# TODO update the JSON string below
json = "{}"
# create an instance of ErrorDetail from a JSON string
error_detail_instance = ErrorDetail.from_json(json)
# print the JSON string representation of the object
print(ErrorDetail.to_json())

# convert the object into a dict
error_detail_dict = error_detail_instance.to_dict()
# create an instance of ErrorDetail from a dict
error_detail_from_dict = ErrorDetail.from_dict(error_detail_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


