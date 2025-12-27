# ApplicationsDefault


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ident_by_icmp6_type** | [**ApplicationsDefaultIdentByIcmp6Type**](ApplicationsDefaultIdentByIcmp6Type.md) |  | [optional] 
**ident_by_icmp_type** | [**ApplicationsDefaultIdentByIcmp6Type**](ApplicationsDefaultIdentByIcmp6Type.md) |  | [optional] 
**ident_by_ip_protocol** | **str** |  | [optional] 
**port** | **List[str]** |  | [optional] 

## Example

```python
from scm.objects.models.applications_default import ApplicationsDefault

# TODO update the JSON string below
json = "{}"
# create an instance of ApplicationsDefault from a JSON string
applications_default_instance = ApplicationsDefault.from_json(json)
# print the JSON string representation of the object
print(ApplicationsDefault.to_json())

# convert the object into a dict
applications_default_dict = applications_default_instance.to_dict()
# create an instance of ApplicationsDefault from a dict
applications_default_from_dict = ApplicationsDefault.from_dict(applications_default_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


