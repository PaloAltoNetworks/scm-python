# LacpHighAvailability

High Availability settings

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**passive_pre_negotiation** | **bool** |  | [optional] [default to False]

## Example

```python
from scm.network_services.models.lacp_high_availability import LacpHighAvailability

# TODO update the JSON string below
json = "{}"
# create an instance of LacpHighAvailability from a JSON string
lacp_high_availability_instance = LacpHighAvailability.from_json(json)
# print the JSON string representation of the object
print(LacpHighAvailability.to_json())

# convert the object into a dict
lacp_high_availability_dict = lacp_high_availability_instance.to_dict()
# create an instance of LacpHighAvailability from a dict
lacp_high_availability_from_dict = LacpHighAvailability.from_dict(lacp_high_availability_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


