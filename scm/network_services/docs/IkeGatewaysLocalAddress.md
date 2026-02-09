# IkeGatewaysLocalAddress


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**interface** | **str** | Interface variable or hardcoded vlan/loopback. vlan will be passed as default value | [optional] [default to 'vlan']
**ip** | **str** | IP Prefix of the assigned interface | [optional] 

## Example

```python
from scm.network_services.models.ike_gateways_local_address import IkeGatewaysLocalAddress

# TODO update the JSON string below
json = "{}"
# create an instance of IkeGatewaysLocalAddress from a JSON string
ike_gateways_local_address_instance = IkeGatewaysLocalAddress.from_json(json)
# print the JSON string representation of the object
print(IkeGatewaysLocalAddress.to_json())

# convert the object into a dict
ike_gateways_local_address_dict = ike_gateways_local_address_instance.to_dict()
# create an instance of IkeGatewaysLocalAddress from a dict
ike_gateways_local_address_from_dict = IkeGatewaysLocalAddress.from_dict(ike_gateways_local_address_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


