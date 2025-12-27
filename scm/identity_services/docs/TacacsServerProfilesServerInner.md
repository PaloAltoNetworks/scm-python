# TacacsServerProfilesServerInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | **str** | The IP address of the TACACS+ server | [optional] 
**name** | **str** | The name of the TACACS+ server | [optional] 
**port** | **int** | The TACACS+ server port | [optional] 
**secret** | **str** | The TACACS+ secret | [optional] 

## Example

```python
from scm_identity_services.models.tacacs_server_profiles_server_inner import TacacsServerProfilesServerInner

# TODO update the JSON string below
json = "{}"
# create an instance of TacacsServerProfilesServerInner from a JSON string
tacacs_server_profiles_server_inner_instance = TacacsServerProfilesServerInner.from_json(json)
# print the JSON string representation of the object
print(TacacsServerProfilesServerInner.to_json())

# convert the object into a dict
tacacs_server_profiles_server_inner_dict = tacacs_server_profiles_server_inner_instance.to_dict()
# create an instance of TacacsServerProfilesServerInner from a dict
tacacs_server_profiles_server_inner_from_dict = TacacsServerProfilesServerInner.from_dict(tacacs_server_profiles_server_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


