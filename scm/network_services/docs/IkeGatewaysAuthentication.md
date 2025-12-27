# IkeGatewaysAuthentication


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**certificate** | [**IkeGatewaysAuthenticationCertificate**](IkeGatewaysAuthenticationCertificate.md) |  | [optional] 
**pre_shared_key** | [**IkeGatewaysAuthenticationPreSharedKey**](IkeGatewaysAuthenticationPreSharedKey.md) |  | [optional] 

## Example

```python
from scm.network_services.models.ike_gateways_authentication import IkeGatewaysAuthentication

# TODO update the JSON string below
json = "{}"
# create an instance of IkeGatewaysAuthentication from a JSON string
ike_gateways_authentication_instance = IkeGatewaysAuthentication.from_json(json)
# print the JSON string representation of the object
print(IkeGatewaysAuthentication.to_json())

# convert the object into a dict
ike_gateways_authentication_dict = ike_gateways_authentication_instance.to_dict()
# create an instance of IkeGatewaysAuthentication from a dict
ike_gateways_authentication_from_dict = IkeGatewaysAuthentication.from_dict(ike_gateways_authentication_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


