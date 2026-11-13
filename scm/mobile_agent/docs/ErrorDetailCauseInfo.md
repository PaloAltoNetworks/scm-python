# ErrorDetailCauseInfo

Detailed information about an error cause including code, message, and contextual details

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | Error code identifying the type of error | [optional] 
**details** | **object** | Additional error details as string or structured object | [optional] 
**help** | **str** | Help text for resolving the error | [optional] 
**message** | **str** | Human-readable error message | [optional] 

## Example

```python
from scm.mobile_agent.models.error_detail_cause_info import ErrorDetailCauseInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ErrorDetailCauseInfo from a JSON string
error_detail_cause_info_instance = ErrorDetailCauseInfo.from_json(json)
# print the JSON string representation of the object
print(ErrorDetailCauseInfo.to_json())

# convert the object into a dict
error_detail_cause_info_dict = error_detail_cause_info_instance.to_dict()
# create an instance of ErrorDetailCauseInfo from a dict
error_detail_cause_info_from_dict = ErrorDetailCauseInfo.from_dict(error_detail_cause_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


