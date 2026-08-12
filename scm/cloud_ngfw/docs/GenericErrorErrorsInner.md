# GenericErrorErrorsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** |  | [optional] 
**details** | **object** |  | [optional] 
**help** | **str** |  | [optional] 
**message** | **str** |  | [optional] 

## Example

```python
from scm.cloud_ngfw.models.generic_error_errors_inner import GenericErrorErrorsInner

# TODO update the JSON string below
json = "{}"
# create an instance of GenericErrorErrorsInner from a JSON string
generic_error_errors_inner_instance = GenericErrorErrorsInner.from_json(json)
# print the JSON string representation of the object
print(GenericErrorErrorsInner.to_json())

# convert the object into a dict
generic_error_errors_inner_dict = generic_error_errors_inner_instance.to_dict()
# create an instance of GenericErrorErrorsInner from a dict
generic_error_errors_inner_from_dict = GenericErrorErrorsInner.from_dict(generic_error_errors_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


