# IkeGatewaysLocalId


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Local ID string | [optional] 
**type** | **str** |  | [optional] 

## Example

```python
from scm.network_services.models.ike_gateways_local_id import IkeGatewaysLocalId

# TODO update the JSON string below
json = "{}"
# create an instance of IkeGatewaysLocalId from a JSON string
ike_gateways_local_id_instance = IkeGatewaysLocalId.from_json(json)
# print the JSON string representation of the object
print(IkeGatewaysLocalId.to_json())

# convert the object into a dict
ike_gateways_local_id_dict = ike_gateways_local_id_instance.to_dict()
# create an instance of IkeGatewaysLocalId from a dict
ike_gateways_local_id_from_dict = IkeGatewaysLocalId.from_dict(ike_gateways_local_id_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


