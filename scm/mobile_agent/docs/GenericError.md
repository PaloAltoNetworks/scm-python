# GenericError

Generic error response structure

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**errors** | [**List[ErrorDetailCauseInfo]**](ErrorDetailCauseInfo.md) | Array of detailed error cause information | [optional] 
**request_id** | **str** | Unique identifier for the API request | [optional] 

## Example

```python
from scm.mobile_agent.models.generic_error import GenericError

# TODO update the JSON string below
json = "{}"
# create an instance of GenericError from a JSON string
generic_error_instance = GenericError.from_json(json)
# print the JSON string representation of the object
print(GenericError.to_json())

# convert the object into a dict
generic_error_dict = generic_error_instance.to_dict()
# create an instance of GenericError from a dict
generic_error_from_dict = GenericError.from_dict(generic_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


