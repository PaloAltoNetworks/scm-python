# AuthenticationSequences


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**authentication_profiles** | **List[str]** | An ordered list of authentication profiles | [optional] 
**device** | **str** | The device in which the resource is defined | [optional] 
**folder** | **str** | The folder in which the resource is defined | [optional] 
**id** | **str** | The UUID of the authentication sequence | [optional] [readonly] 
**name** | **str** | The name of the authentication sequence | 
**snippet** | **str** | The snippet in which the resource is defined | [optional] 
**use_domain_find_profile** | **bool** | Use domain to determine authentication profile? | [optional] [default to True]

## Example

```python
from scm_identity_services.models.authentication_sequences import AuthenticationSequences

# TODO update the JSON string below
json = "{}"
# create an instance of AuthenticationSequences from a JSON string
authentication_sequences_instance = AuthenticationSequences.from_json(json)
# print the JSON string representation of the object
print(AuthenticationSequences.to_json())

# convert the object into a dict
authentication_sequences_dict = authentication_sequences_instance.to_dict()
# create an instance of AuthenticationSequences from a dict
authentication_sequences_from_dict = AuthenticationSequences.from_dict(authentication_sequences_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


