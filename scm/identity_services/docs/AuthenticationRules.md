# AuthenticationRules


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**authentication_enforcement** | **str** | The authentication profile name | [optional] 
**category** | **List[str]** | The destination URL categories | [optional] 
**description** | **str** | The description of the authentication rule | [optional] 
**destination** | **List[str]** | The destination addresses | 
**destination_hip** | **List[str]** | The destination Host Integrity Profile (HIP) | [optional] 
**device** | **str** |  | [optional] 
**disabled** | **bool** | Is the authentication rule disabled? | [optional] [default to False]
**folder** | **str** |  | [optional] 
**var_from** | **List[str]** | The source security zones | 
**group_tag** | **str** |  | [optional] 
**hip_profiles** | **List[str]** | The source Host Integrity Profile (HIP) | [optional] 
**id** | **str** | The UUID of the authentication rule | [optional] [readonly] 
**log_authentication_timeout** | **bool** | Log authentication timeouts? | [optional] [default to False]
**log_setting** | **str** | The log forwarding profile name | [optional] 
**name** | **str** | The name of the authentication rule | 
**negate_destination** | **bool** | Are the destination addresses negated? | [optional] [default to False]
**negate_source** | **bool** | Are the source addresses negated? | [optional] [default to False]
**service** | **List[str]** | The destination ports | 
**snippet** | **str** |  | [optional] 
**source** | **List[str]** | The source addresses | 
**source_hip** | **List[str]** | The source Host Integrity Profile (HIP) | [optional] 
**source_user** | **List[str]** | The source users | [optional] 
**tag** | **List[str]** | The authentication rule tags | [optional] 
**timeout** | **int** | The authentication session timeout (seconds) | [optional] 
**to** | **List[str]** | The destination security zones | 

## Example

```python
from scm.identity_services.models.authentication_rules import AuthenticationRules

# TODO update the JSON string below
json = "{}"
# create an instance of AuthenticationRules from a JSON string
authentication_rules_instance = AuthenticationRules.from_json(json)
# print the JSON string representation of the object
print(AuthenticationRules.to_json())

# convert the object into a dict
authentication_rules_dict = authentication_rules_instance.to_dict()
# create an instance of AuthenticationRules from a dict
authentication_rules_from_dict = AuthenticationRules.from_dict(authentication_rules_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


