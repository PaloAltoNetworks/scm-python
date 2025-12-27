# TacacsServerProfiles


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**device** | **str** | The device in which the resource is defined | [optional] 
**folder** | **str** | The folder in which the resource is defined | [optional] 
**id** | **str** | The UUID of the TACACS+ server profile | [readonly] 
**name** | **str** | The name of the TACACS+ server profile | 
**protocol** | **str** | The TACACS+ authentication protocol | 
**server** | [**List[TacacsServerProfilesServerInner]**](TacacsServerProfilesServerInner.md) | The TACACS+ server configuration | 
**snippet** | **str** | The snippet in which the resource is defined | [optional] 
**timeout** | **int** | The TACACS+ timeout (seconds) | [optional] 
**use_single_connection** | **bool** | Use a single TACACS+ connection? | [optional] 

## Example

```python
from scm_identity_services.models.tacacs_server_profiles import TacacsServerProfiles

# TODO update the JSON string below
json = "{}"
# create an instance of TacacsServerProfiles from a JSON string
tacacs_server_profiles_instance = TacacsServerProfiles.from_json(json)
# print the JSON string representation of the object
print(TacacsServerProfiles.to_json())

# convert the object into a dict
tacacs_server_profiles_dict = tacacs_server_profiles_instance.to_dict()
# create an instance of TacacsServerProfiles from a dict
tacacs_server_profiles_from_dict = TacacsServerProfiles.from_dict(tacacs_server_profiles_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


