# LldpHighAvailability

LLDP high availability settings

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**passive_pre_negotiation** | **bool** |  | [optional] [default to False]

## Example

```python
from scm.network_services.models.lldp_high_availability import LldpHighAvailability

# TODO update the JSON string below
json = "{}"
# create an instance of LldpHighAvailability from a JSON string
lldp_high_availability_instance = LldpHighAvailability.from_json(json)
# print the JSON string representation of the object
print(LldpHighAvailability.to_json())

# convert the object into a dict
lldp_high_availability_dict = lldp_high_availability_instance.to_dict()
# create an instance of LldpHighAvailability from a dict
lldp_high_availability_from_dict = LldpHighAvailability.from_dict(lldp_high_availability_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


