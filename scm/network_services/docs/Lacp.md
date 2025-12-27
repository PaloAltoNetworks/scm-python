# Lacp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enable** | **bool** | Enable LACP? | [optional] [default to False]
**fast_failover** | **bool** | Fast failover | [optional] [default to False]
**max_ports** | **int** | Maximum number of physical ports bundled in the LAG | [optional] [default to 8]
**mode** | **str** | Mode | [optional] [default to 'passive']
**system_priority** | **int** | LACP system priority in system ID | [optional] [default to 32768]
**transmission_rate** | **str** | Transmission mode | [optional] [default to 'slow']

## Example

```python
from scm.network_services.models.lacp import Lacp

# TODO update the JSON string below
json = "{}"
# create an instance of Lacp from a JSON string
lacp_instance = Lacp.from_json(json)
# print the JSON string representation of the object
print(Lacp.to_json())

# convert the object into a dict
lacp_dict = lacp_instance.to_dict()
# create an instance of Lacp from a dict
lacp_from_dict = Lacp.from_dict(lacp_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


