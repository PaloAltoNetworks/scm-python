# TenantTrustInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created** | **datetime** |  | [optional] [readonly] 
**created_by** | **str** |  | [optional] [readonly] 
**current_status** | **str** |  | [optional] [readonly] 
**donor_cluster** | **str** |  | [optional] [readonly] 
**donor_msg_uuid** | **str** |  | [optional] [readonly] 
**donor_project** | **str** |  | [optional] [readonly] 
**donor_region** | **str** |  | [optional] [readonly] 
**donor_tenant_id** | **str** |  | [optional] 
**donor_tenant_name** | **str** |  | [optional] 
**donor_trust_info_id** | **int** |  | [optional] [readonly] 
**donor_tsg** | **str** |  | [optional] [readonly] 
**error_details** | **str** |  | [optional] [readonly] 
**last_updated** | **datetime** |  | [optional] [readonly] 
**psk** | **str** |  | [optional] 
**recipient_cluster** | **str** |  | [optional] [readonly] 
**recipient_msg_uuid** | **str** |  | [optional] [readonly] 
**recipient_project** | **str** |  | [optional] [readonly] 
**recipient_region** | **str** |  | [optional] [readonly] 
**recipient_tenant_id** | **str** |  | [optional] [readonly] 
**recipient_tenant_name** | **str** |  | [optional] 
**recipient_trust_info_id** | **int** |  | [optional] [readonly] 
**recipient_tsg** | **str** |  | [optional] [readonly] 
**trust_id** | **int** |  | [optional] 
**updated_by** | **str** |  | [optional] [readonly] 

## Example

```python
from scm_config_setup.models.tenant_trust_info import TenantTrustInfo

# TODO update the JSON string below
json = "{}"
# create an instance of TenantTrustInfo from a JSON string
tenant_trust_info_instance = TenantTrustInfo.from_json(json)
# print the JSON string representation of the object
print(TenantTrustInfo.to_json())

# convert the object into a dict
tenant_trust_info_dict = tenant_trust_info_instance.to_dict()
# create an instance of TenantTrustInfo from a dict
tenant_trust_info_from_dict = TenantTrustInfo.from_dict(tenant_trust_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


