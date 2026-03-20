# CompareTloPayload


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**comparing_version** | **int** |  | [optional] 
**object_id** | **str** |  | 
**snippet_id** | **str** |  | 
**version** | **int** |  | 

## Example

```python
from scm.config_setup.models.compare_tlo_payload import CompareTloPayload

# TODO update the JSON string below
json = "{}"
# create an instance of CompareTloPayload from a JSON string
compare_tlo_payload_instance = CompareTloPayload.from_json(json)
# print the JSON string representation of the object
print(CompareTloPayload.to_json())

# convert the object into a dict
compare_tlo_payload_dict = compare_tlo_payload_instance.to_dict()
# create an instance of CompareTloPayload from a dict
compare_tlo_payload_from_dict = CompareTloPayload.from_dict(compare_tlo_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


