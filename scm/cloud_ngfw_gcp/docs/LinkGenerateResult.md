# LinkGenerateResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cspid** | **str** | The Customer Support Portal account ID of the TSG. | [optional] 
**code** | **str** | The one-time link code. Treat it as a secret. | 
**expires_at** | **int** | When the link code expires, in Unix epoch seconds. | 
**tsgid** | **str** | The TSG the Google Cloud tenant is linked to. | [optional] 

## Example

```python
from scm.cloud_ngfw_gcp.models.link_generate_result import LinkGenerateResult

# TODO update the JSON string below
json = "{}"
# create an instance of LinkGenerateResult from a JSON string
link_generate_result_instance = LinkGenerateResult.from_json(json)
# print the JSON string representation of the object
print(LinkGenerateResult.to_json())

# convert the object into a dict
link_generate_result_dict = link_generate_result_instance.to_dict()
# create an instance of LinkGenerateResult from a dict
link_generate_result_from_dict = LinkGenerateResult.from_dict(link_generate_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


