# PushCandidateConfigVersionsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**admin** | **List[str]** | List the administrators and/or service accounts in this field. If you want to push folder named All, please do not add this admin field at all and list each of the folders under All in the folder field. | [optional] 
**description** | **str** | A description of the changes being pushed | [optional] 
**devices** | **List[str]** | The target devices for the configuration push | [optional] 
**folder** | **List[str]** | The target folders for the configuration push | [optional] 

## Example

```python
from scm.config_operations.models.push_candidate_config_versions_request import PushCandidateConfigVersionsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PushCandidateConfigVersionsRequest from a JSON string
push_candidate_config_versions_request_instance = PushCandidateConfigVersionsRequest.from_json(json)
# print the JSON string representation of the object
print(PushCandidateConfigVersionsRequest.to_json())

# convert the object into a dict
push_candidate_config_versions_request_dict = push_candidate_config_versions_request_instance.to_dict()
# create an instance of PushCandidateConfigVersionsRequest from a dict
push_candidate_config_versions_request_from_dict = PushCandidateConfigVersionsRequest.from_dict(push_candidate_config_versions_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


