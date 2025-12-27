# DNSSecurityProfilesListResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[DnsSecurityProfiles]**](DnsSecurityProfiles.md) |  | 
**limit** | **int** | The maximum number of results per page | [default to 200]
**offset** | **int** | The offset into the list of results returned | [default to 0]
**total** | **int** | The total count of results | 

## Example

```python
from scm.security_services.models.dns_security_profiles_list_response import DNSSecurityProfilesListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DNSSecurityProfilesListResponse from a JSON string
dns_security_profiles_list_response_instance = DNSSecurityProfilesListResponse.from_json(json)
# print the JSON string representation of the object
print(DNSSecurityProfilesListResponse.to_json())

# convert the object into a dict
dns_security_profiles_list_response_dict = dns_security_profiles_list_response_instance.to_dict()
# create an instance of DNSSecurityProfilesListResponse from a dict
dns_security_profiles_list_response_from_dict = DNSSecurityProfilesListResponse.from_dict(dns_security_profiles_list_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


