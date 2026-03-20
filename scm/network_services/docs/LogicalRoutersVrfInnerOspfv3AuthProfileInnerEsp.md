# LogicalRoutersVrfInnerOspfv3AuthProfileInnerEsp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**authentication** | [**LogicalRoutersVrfInnerOspfv3AuthProfileInnerEspAuthentication**](LogicalRoutersVrfInnerOspfv3AuthProfileInnerEspAuthentication.md) |  | [optional] 
**encryption** | [**LogicalRoutersVrfInnerOspfv3AuthProfileInnerEspEncryption**](LogicalRoutersVrfInnerOspfv3AuthProfileInnerEspEncryption.md) |  | [optional] 

## Example

```python
from scm.network_services.models.logical_routers_vrf_inner_ospfv3_auth_profile_inner_esp import LogicalRoutersVrfInnerOspfv3AuthProfileInnerEsp

# TODO update the JSON string below
json = "{}"
# create an instance of LogicalRoutersVrfInnerOspfv3AuthProfileInnerEsp from a JSON string
logical_routers_vrf_inner_ospfv3_auth_profile_inner_esp_instance = LogicalRoutersVrfInnerOspfv3AuthProfileInnerEsp.from_json(json)
# print the JSON string representation of the object
print(LogicalRoutersVrfInnerOspfv3AuthProfileInnerEsp.to_json())

# convert the object into a dict
logical_routers_vrf_inner_ospfv3_auth_profile_inner_esp_dict = logical_routers_vrf_inner_ospfv3_auth_profile_inner_esp_instance.to_dict()
# create an instance of LogicalRoutersVrfInnerOspfv3AuthProfileInnerEsp from a dict
logical_routers_vrf_inner_ospfv3_auth_profile_inner_esp_from_dict = LogicalRoutersVrfInnerOspfv3AuthProfileInnerEsp.from_dict(logical_routers_vrf_inner_ospfv3_auth_profile_inner_esp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


