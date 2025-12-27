# ErrorDetailCauseInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** |  | [optional] 
**details** | **object** |  | [optional] 
**help** | **str** |  | [optional] 
**message** | **str** |  | [optional] 

## Example

```python
from scm_device_settings.models.error_detail_cause_info import ErrorDetailCauseInfo

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


